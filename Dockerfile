# Use an official Python image as the base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the app code into the container
COPY . /app

# Install dependencies
RUN pip install  -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Set environment variables
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
