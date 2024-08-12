import streamlit as st 
import os
import base64
import google.generativeai as genai
from PIL import Image
import matplotlib.pyplot as plt

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to read the Image and set the image format for Gemini Pro model Input
def input_image_setup(upload_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded!")

# Function to parse the Gemini AI response and extract nutritional data for pie chart
def parse_nutritional_data(response_text):
    lines = response_text.splitlines()
    nutritional_data = {}
    found_data = False
    for line in lines:
        if '%' in line:
            found_data = True
            try:
                item, percentage = line.split('-')
                item = item.strip()
                percentage = float(percentage.replace('%', '').strip())
                nutritional_data[item] = percentage
            except ValueError:
                continue
    if not found_data:
        st.write("Nutritional breakdown data not found in the response.")
    return nutritional_data

# Function to create and display a pie chart
def display_pie_chart(data):
    if data:
        labels = data.keys()
        sizes = data.values()
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
        
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        
        st.pyplot(fig)
    else:
        st.write("No data available for pie chart.")

# Writing a prompt for gemini model 
input_prompt = """As an expert nutritionist known as NutriSense AI, your task is to analyze the food items presented in the image provided. 
Please calculate the total caloric content and offer a detailed breakdown of each food item with its corresponding calorie count in the following format:
1. Item1 - number of calories
2. Item2 - number of calories
...
...
Additionally, provide an assessment of the meal's overall healthiness. Finally, include a percentage-based breakdown of the meal's nutritional components, including carbohydrates, fats, fibers, sugars, and other essential dietary elements necessary for a balanced diet.
After analyzing a meal, you could rate it on to 5 ⭐ Star for healthiness.
"""

# Initialize our streamlit app
st.set_page_config(page_title="NutriSense AI", page_icon="🍎")

# Custom HTML for a multicolored header
st.markdown(
    """
    <style>
    .custom-header {
        font-size: 48px;
        font-weight: bold;
        background: rgb(2,0,36);
        background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    <div class="custom-header">
        NutriSense AI
    </div>
    """,
    unsafe_allow_html=True
)

# Apply custom CSS for white text, except for the button and subheader
st.markdown(
    """
    <style>
    .stApp {
        background: url(data:image/jpeg;base64,{encoded_background_image}) no-repeat center center fixed;
        background-size: cover;
    }
    .stMarkdown, .stTextInput, .stHeader, .stSubheader, .stCaption {
        color: white;
    }
    .stButton>button {
        color: black !important;
        background-color: #f0f0f0 !important;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }
    .custom-subheader {
        color: yellow !important;
        font-weight: bold;
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

input = st.text_input("Tell me about Yourself and Your Diet Plan and Food recipe or ingredients: ", key="input")

# Option to select image source: Capture or Upload
image_source = st.radio("Choose image source:", ('Capture from Camera', 'Upload from File'))

if image_source == 'Capture from Camera':
    captured_image = st.camera_input("Capture an image of your meal:")
    uploaded_file = captured_image
else:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("TELL ME ABOUT THIS MEAL!!")

# If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.markdown('<div class="custom-subheader">Description of Your Meal:</div>', unsafe_allow_html=True)
    st.write(response)
    
    # Parse response and display pie chart
    nutritional_data = parse_nutritional_data(response)
    st.markdown('<div class="custom-subheader">Nutritional Breakdown:</div>', unsafe_allow_html=True)
    display_pie_chart(nutritional_data)

# Setting the default background image
background_image_path = "BackgroundAI.jpg"

with open(background_image_path, "rb") as file:
    background_image = file.read()

encoded_background_image = base64.b64encode(background_image).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url(data:image/jpeg;base64,{encoded_background_image}) no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
