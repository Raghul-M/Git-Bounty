# Git Bounty 💰

**Git Bounty** generates a personalized anime-style pirate bounty posters based on a user's GitHub activity. Simply input a GitHub username, and the app pulls relevant data like contributions, favorite programming languages, and more to create a unique bounty poster.

![image](https://github.com/user-attachments/assets/f20459f6-3a9e-465c-93c4-051e29d09dfe)

## 🖥️ Features
- **Profile Integration**: Fetches GitHub profile details such as username, followers, location, and contributions.
- **Anime-Style Poster**: Generates a bounty poster with a tech-pirate theme based on GitHub activity.
- **Programming Flair**: Highlights the user's most used programming languages.
- **Custom Bounty**: Sets the bounty amount to match total contributions.
- **Downloadable Poster**: Save and share your personalized bounty poster.

## 🚀 Live Demo
Check out the live app Git Bounty : [ https://gitbounty.streamlit.app/](https://gitbounty.streamlit.app/)

## 🛠️ How It Works
1. Enter a GitHub username.
2. The app fetches user details and contribution data from the GitHub API.
3. It generates an anime-style bounty poster using the Hugging Face Stable Diffusion model.
4. The poster is displayed and ready for download.

### **Home Page**
![Screenshot 2025-01-22 at 10 52 22 AM](https://github.com/user-attachments/assets/99dc1a5c-9333-440b-b1bf-abd341e35c89)


### **Generated Bounty Poster**
![Screenshot 2025-01-22 at 10 52 52 AM](https://github.com/user-attachments/assets/ce740694-983d-4bf8-9c46-12ac0318b36c)


## 🧩 Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/) for an interactive web app.
- **Backend APIs**:
  - [GitHub REST API](https://docs.github.com/en/rest) for fetching user profile data.
  - [GitHub GraphQL API](https://docs.github.com/en/graphql) for contribution and language statistics.
  - [Hugging Face Model (stabilityai/stable-diffusion-3.5-large)](https://huggingface.co/stabilityai) for image generation.
  -  [Docker](https://www.docker.com/) for Conatinerizing the Application
- **Deployment**: Hosted on [Streamlit Cloud](https://streamlit.io/cloud).

## 🛠️ Local Setup
1. Clone this repository:
   ```bash
   $ git clone https://github.com/Raghul-M/Git-Bounty.git
   $ cd git-bounty
   ```

2. Create a virtual environment and activate it:
   ```bash
   $ python -m venv venv
   $ source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root with the following content:
     ```env
     GH_TOKEN= "your_github_api_token"
     
     HF_TOKEN= "your_huggingface_api_token"
     ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## 🧳 Deployment
### Streamlit Cloud
1. Push the code to a public/private repository on GitHub.
2. Connect the repository to [Streamlit Cloud](https://streamlit.io/cloud) and deploy the app.

### Docker (Optional)
1. Build the Docker image:
   ```bash
   $ docker build -t git-bounty .
   ```
2. Run the Docker container:
   ```bash
   $ docker run -p 8501:8501 git-bounty
   ```

## 🌟 Contributing
Contributions are welcome! If you have suggestions, bug reports, or want to add new features, feel free to submit a pull request.

Feel free to explore, contribute, and adapt this project to suit your needs. If you encounter any issues or have suggestions for improvement, please raise them in the GitHub repository's issues section. Happy coding! 🚀

Connect with me on linkedin: [Raghul M](https://www.linkedin.com/in/m-raghul/)


## ✨ Acknowledgments
- Inspired by the creativity of the One Piece universe.
- Special thanks to [Streamlit](https://streamlit.io/) and [Hugging Face](https://huggingface.co/) for their awesome tools.

---

Bring your GitHub activity to life with **Git Bounty** — the ultimate developer's bounty poster generator! 🏴‍☠️

