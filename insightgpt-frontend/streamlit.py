import streamlit as st
from PIL import Image
import io
import base64
import requests

def home():
    st.title("Welcome to InsightGPT")
    st.write("InsightGPT is a cutting-edge platform designed to harness the power of Gemini API for extracting actionable insights from complex data sets. Our project aims to revolutionize data analysis by providing businesses and researchers with an intuitive, AI-driven tool that transforms raw data into meaningful narratives and visualizations.")
    
    image = Image.open("Image/image1.jpeg")
    new_width = 600
    new_height = int((new_width / image.width) * image.height)
    resized_image = image.resize((new_width, new_height))
    buffered = io.BytesIO()
    resized_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    st.markdown(
        f"""
        <div style='display: flex; justify-content: center;'>
            <img src='data:image/jpeg;base64,{img_str}' alt='resized image'>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.header("Key Features")
    features = {
        "Natural Language Query Interface": "The Natural Language Query Interface in InsightGPT allows users to ask questions about their data in plain language and receive clear, comprehensive responses, making data analysis accessible to non-technical users.",
        "Automated Data Cleaning": "InsightGPT uses advanced algorithms to automatically clean and preprocess data, ensuring analyses are based on accurate and high-quality inputs, thus reducing data preparation time and effort.",
        "Dynamic Data Visualization": "The platform creates dynamic and interactive visualizations that update in real-time, helping users quickly identify trends, patterns, and outliers.",
        "Insight Generation": "InsightGPT leverages the Gemini API to provide detailed insights and recommendations in a narrative format, making complex data comprehensible and actionable."
    }

    st.markdown("""
        <style>
        .custom-heading {
            font-size: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    for heading, description in features.items():
        st.markdown(f"<h2 class='custom-heading'>{heading}</h2>", unsafe_allow_html=True)
        st.write(description)

def insights_visualizations():
    st.title("Upload Your Data")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
    else:
        st.info("Drag and drop a file or click to select.")
    
    st.title("Insights & Visualizations")
    query = st.text_input("Ask a question about your data")
    if st.button("Generate Insights"):
        st.write(f"Generating insights for: {query}")
        data = {"query": query}
        
        try:
            response = requests.post("http://127.0.0.1:5001/analyze", json=data)
            if response.status_code == 200:
                insights = response.json().get("insights")
                st.write("Insights:")
                st.write(insights)
            else:
                st.error(f"Failed to fetch insights from the API. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the API: {e}")

def main():
    st.set_page_config(page_title="InsightGPT", layout="wide")
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'
    st.sidebar.title("InsightGPT")
    menu = ["Home", "Data visualization"]
    for page in menu:
        if st.sidebar.button(page):
            st.session_state.page = page
    if st.session_state.page == "Home":
        home()
    elif st.session_state.page == "Data visualization":
        insights_visualizations()

if __name__ == '__main__':
    main()
