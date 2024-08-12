# smartinternz08-genAI-NutritionAppGeminiAI-Shahib

# NutriSense AI
## About
NutriSense AI is an innovative web application designed to provide personalized dietary recommendations and nutritional advice using the advanced capabilities of the Gemini Pro model. This app leverages artificial intelligence to analyze user data, dietary preferences, and health goals, delivering tailored meal plans, nutritional insights, and wellness tips. The primary aim of NutriSense AI is to promote healthier eating habits and improve overall well-being through intelligent and data-driven recommendations.

## Features
**Image Analysis:** Capture or upload images of your meals for nutritional analysis.
### Personalized Recommendations: Provide dietary input to receive tailored meal plans and advice.
### Nutritional Breakdown: Get detailed nutritional information, including carbohydrates, fats, fibers, sugars, and other dietary components.
### Visual Representation: View a pie chart of nutritional components and their percentages.

## Technologies Used
### Streamlit: A framework for creating interactive web applications in Python. It is used for building the user interface of NutriSense AI.
### Google Generative AI (Gemini Pro Vision API): Provides advanced image analysis and content generation capabilities to analyze meal images and generate nutritional insights.
### Python-dotenv: Loads environment variables from a .env file to manage API keys and other sensitive data.
### Base64: Encodes and decodes binary data to handle image files and background images.
### Matplotlib: Creates visualizations, specifically pie charts, to display nutritional breakdowns.


## Requirements
### Create a requirements.txt file with the following content:
streamlit
google.generativeai
python-dotenv
base64
matplotlib.pyplot

## Setup
### Clone the Repository:
git clone <repository-url>
cd <repository-directory>

## Install Dependencies:
pip install -r requirements.txt

## Create a .env File:
### Add your Google API key to a file named .env:
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"

## Run the Application:
streamlit run app.py


## Code Overview
The code sets up a Streamlit application with the following key functionalities:

### Image Upload or Capture: Allows users to either upload an image of their meal or capture one using their camera.

### Image Processing: Processes the image for analysis using the Google Gemini Pro Vision API.

### Nutritional Data Parsing: Extracts and parses nutritional data from the API response.
### Pie Chart Visualization: Generates a pie chart representing the nutritional breakdown of the meal.


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or issues, please contact sahibsaifi12291@gmail.com.com.
