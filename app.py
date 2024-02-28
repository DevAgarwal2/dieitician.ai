from dotenv import load_dotenv
from os import system

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input,image[0],prompt])
    return response.text
def get_gemini_response2(input,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([input,prompt])
    return response.text

def input_image(image_file):
    if image_file is not None:
        byte_data = image_file.getvalue()

        image_parts = [
            {
                "mime_type":image_file.type,
                "data": byte_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File not there")

st.set_page_config("Dietician Ai")

st.header("Ai Health Expert")

input2 = st.text_input("Enter the text: ",key="input2")
input = st.text_input("Enter the text: ",key="input")

upload_file = st.file_uploader("Choose a File: ",type=["jpeg","jpg","png"])

image_file=""

if upload_file is not None:
    image_file = Image.open(upload_file)
    st.image(image_file,caption="Upload The Image",use_column_width=True)

submit = st.button("Submit")
submit2 = st.button("Text Submit")


inputPrompt = """
You are a Health Expert. You will recieve Image of Food and you have to give the calories
of each food image
"""
inputPrompt2 = """
You are a Dietician Expert tasked with generating
 a 7-day meal plan featuring authentic Indian vegetarian dishes, 
 with the aim of supporting weight reduction. Focus on traditional recipes from various
   regions of India, incorporating staple ingredients like
     vegetables, grains, and spices commonly used in Indian cuisine. Emphasize nutritious,
       low-calorie options while still providing flavorful and satisfying meals. 
       Include a variety of breakfast, lunch, and dinner options.
       Also give the calories of each food and give the total in the end
"""

if submit:
    image_data = input_image(upload_file)
    response = get_gemini_response(inputPrompt,image_data,input)
    st.write(response)

if submit2:
    response = get_gemini_response2(inputPrompt2,input2)
    st.write(response)
    ok = st.button("Voice")
    


