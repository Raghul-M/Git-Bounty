import time
import requests
import streamlit as st
from dotenv import load_dotenv  # type: ignore
import os
from huggingface_hub import InferenceClient

load_dotenv()
gh_token = st.secrets.GH_TOKEN
hf_token = st.secrets.HF_TOKEN
st.set_page_config(page_title="Git Bounty", page_icon="💰")
st.title("Git Bounty 💰")

# Description
st.write("""
Welcome to **Git Bounty 🏴‍☠️**, a fun and creative tool that transforms GitHub profiles into vibrant anime-style bounty posters. 
Simply enter a GitHub username to generate a unique poster based on contributions, favorite programming languages, and more!
""")

"[![Open in GitHub](https://github.com/codespaces/badge.svg)](https://github.com/Raghul-M/Git-Bounty/)"

def github():
    badge(type="github", name="streamlit/streamlit")
    
# GitHub Username Input
username = st.text_input("Enter Your Github Username 🔍 : ")

# Initialize variables
followers = 0
avatar_url = "No profile picture"
location = "N/A"
button = None

# Fetch user data only if username is entered
if username:
    button = st.button("Fetch & Generate Image")
    

def graphql_call(username):
    graphql_url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer {gh_token}"}
    query = """
    query($username: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $username) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            totalContributions
          }
        }
        repositories(first: 100, orderBy: { field: STARGAZERS, direction: DESC }) {
          edges {
            node {
              primaryLanguage {
                name
              }
            }
          }
        }
      }
    }
    """
    variables = {
        "username": username,
        "from": "2024-01-01T00:00:00Z",
        "to": "2024-12-31T23:59:59Z",
    }
    response = requests.post(graphql_url, json={"query": query, "variables": variables}, headers=headers)
    data = response.json()

    total_contributions = 0
    most_used_language = "None"
    
    if "data" in data and data["data"].get("user"):
        user_data = data["data"]["user"]

        contributions_data = user_data.get("contributionsCollection")
        if contributions_data:
            total_contributions = contributions_data["contributionCalendar"]["totalContributions"]

        repositories = user_data.get("repositories", {}).get("edges", [])
        language_count = {}
        for repo in repositories:
            language = repo["node"]["primaryLanguage"]
            if language:
                lang_name = language["name"]
                language_count[lang_name] = language_count.get(lang_name, 0) + 1
        most_used_language = max(language_count, key=language_count.get) if language_count else "None"
    else:
        st.write("Error: User not found or insufficient data.")
        if "errors" in data:
            st.write("GraphQL Errors:", data["errors"])
    
    return total_contributions, most_used_language

def rest_call(username):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {gh_token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    name = data.get('login', 'N/A')
    avatar_url = data.get('avatar_url', 'No profile picture')
    followers = data.get('followers', 0)
    location = data.get('location', 'N/A')

    return followers, location, avatar_url

def image_generation(username, total_contributions, most_used_language):
    with st.spinner("Generating bounty poster..."):
        client = InferenceClient("stabilityai/stable-diffusion-3.5-large", token=hf_token)
        description = (
            f"Create an anime-style pirate bounty poster for a character named {username}, inspired by their 2024 GitHub "
            f"contributions totaling {total_contributions}. The character wears a futuristic, tech-themed pirate outfit featuring "
            f"glowing symbols of programming languages {most_used_language}, integrated into their attire as patches or emblems. "
            f"They wield a unique weapon, such as a keyboard sword or a tech hammer, symbolizing their problem-solving and innovative nature. "
            f"The bounty is styled as {total_contributions} million bounty, prominently displayed on the poster. Include the text 'WANTED' "
            f"in bold, classic bounty poster font, with a weathered parchment texture for the background. Add small logos of {most_used_language} "
            f"near the bounty text, subtly highlighting their coding expertise. The character should exude energy, confidence, and an adventurous "
            f"spirit, depicted in a bold, exaggerated anime art style with vibrant colors and dynamic posing."
        )
        image = client.text_to_image(description)
        file_path = f"{username}_bounty_poster.png"
        image.save(file_path)
        st.success("Done")
        st.image(file_path)
        

def data_visual(username, avatar_url, followers, location, total_contributions, most_used_language):
    st.markdown("---")
    st.subheader("User Info:")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(avatar_url, width=220, caption="Profile Picture")
    with col2:
        st.markdown(f"""
        **Username:** {username}
        \n**Followers:** {followers}
        \n**Total contributions in 2024:** {total_contributions or 'N/A'}
        \n**Most used Language:** {most_used_language or 'N/A'}
        \n**Location:** {location or 'N/A'}
        """)
    st.markdown("---")

if username and button:
    followers, location, avatar_url = rest_call(username)
    total_contributions, most_used_language = graphql_call(username)
    data_visual(username=username, total_contributions=total_contributions, 
                most_used_language=most_used_language, followers=followers, 
                avatar_url=avatar_url, location=location)
    image_generation(username=username, total_contributions=total_contributions, 
                     most_used_language=most_used_language)
