# To run this file via terminal, use any of these commands
# streamlit run file.py
# python -m streamlit run file.py
# py -m streamlit run file.py
# python3 -m streamlit run file.py
# py -m streamlit run file.py
import streamlit as st

# Theme Configuration and Styling Injection
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

def inject_theme():
    if st.session_state.theme == "dark":
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            /* Global Font and Colors */
            html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
                font-family: 'Inter', sans-serif !important;
                background-color: #0f172a !important;
                color: #f8fafc !important;
            }
            
            /* Sidebar Styling */
            [data-testid="stSidebar"] {
                background-color: #1e293b !important;
                border-right: 1px solid #334155 !important;
            }
            
            /* Text Color Overrides */
            p, span, label, h1, h2, h3, h4, h5, h6, li {
                color: #f8fafc !important;
                font-family: 'Inter', sans-serif !important;
            }
            
            /* Inputs, Selectboxes, Textareas */
            input, select, textarea, div[role="listbox"], div[data-baseweb="select"] > div {
                background-color: #1e293b !important;
                color: #f8fafc !important;
                border: 1px solid #334155 !important;
                border-radius: 8px !important;
            }
            
            /* Custom styled Buttons */
            .stButton>button {
                background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 8px !important;
                padding: 0.5rem 1rem !important;
                font-weight: 600 !important;
                transition: all 0.2s ease-in-out !important;
                box-shadow: 0 4px 6px -1px rgba(99, 102, 241, 0.4) !important;
            }
            .stButton>button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.5) !important;
            }
            .stButton>button:active {
                transform: translateY(0px) !important;
            }
            
            /* Radio and Checkboxes */
            div[role="radiogroup"] label {
                color: #f8fafc !important;
            }
            
            /* Success, Info, Warning, Error boxes */
            div[data-testid="stNotification"] {
                border-radius: 8px !important;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            /* Global Font and Colors */
            html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
                font-family: 'Inter', sans-serif !important;
                background-color: #f8fafc !important;
                color: #0f172a !important;
            }
            
            /* Sidebar Styling */
            [data-testid="stSidebar"] {
                background-color: #ffffff !important;
                border-right: 1px solid #e2e8f0 !important;
            }
            
            /* Text Color Overrides */
            p, span, label, h1, h2, h3, h4, h5, h6, li {
                color: #0f172a !important;
                font-family: 'Inter', sans-serif !important;
            }
            
            /* Inputs, Selectboxes, Textareas */
            input, select, textarea, div[role="listbox"], div[data-baseweb="select"] > div {
                background-color: #ffffff !important;
                color: #0f172a !important;
                border: 1px solid #e2e8f0 !important;
                border-radius: 8px !important;
            }
            
            /* Custom styled Buttons */
            .stButton>button {
                background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 8px !important;
                padding: 0.5rem 1rem !important;
                font-weight: 600 !important;
                transition: all 0.2s ease-in-out !important;
                box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.4) !important;
            }
            .stButton>button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.5) !important;
            }
            .stButton>button:active {
                transform: translateY(0px) !important;
            }
            
            /* Radio and Checkboxes */
            div[role="radiogroup"] label {
                color: #0f172a !important;
            }
            </style>
        """, unsafe_allow_html=True)

# Inject the selected theme stylesheet
inject_theme()

# Sidebar
st.sidebar.title("Sidebar title")
theme_btn_label = "☀️ Light Mode" if st.session_state.theme == "dark" else "🌙 Dark Mode"
st.sidebar.button(theme_btn_label, on_click=toggle_theme)

choice = st.sidebar.radio("Select a view:", ["Home", "About", "Contact", "Exit"])

# Headings
st.title(f"{choice} Page")      # main title
st.header("This is a Header")   # section header
st.write("This is a body text")
st.write("---")

# Body Texts
st.text("- **Some text**")     # to display plain text
st.write("- **Some text**")    # more versatile than text, can handle (dataframes, markdowns, etc.)
st.write("---")

# Special Messages, Colorful texts
st.header("Colored messages")
st.success("Success msgs are in Green")
st.error("Error msgs are in Red")
st.warning("Warning msgs are in Yellow")
st.info("Info msgs are in Blue")
st.write("---")

# Text input
st.header("Text input")
name = st.text_input("Enter your name")

# Number input
st.header("Number input")
age = st.number_input("Enter your age", min_value=0, max_value=100, value=50)

# Button, on click events
st.header("Button")
if st.button("Show Details"):
    st.write(f"Your name is {name} and your age is {age}")
st.write("---")

# Slider
st.header("Slider")
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write(f"Slider value: {value}")
st.write("---")

# Checkbox
st.header("Checkbox")
value = st.checkbox("Show Text")
st.write(f"Checkbox value: {value}")
st.write("---")

# Radio
st.header("Radio")
value = st.radio("Pick one:", ["A", "B", "C"])
st.write(f"Radio value: {value}")
st.write("---")

# Selectbox
st.header("Selectbox")
value = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selectbox value: {value}")
st.write("---")

# Multiselect
st.header("Multiselect")
value = st.multiselect("Choose multiple options", ["Option 1", "Option 2", "Option 3"])
st.write(f"Multiselect value: {value}")
st.write("---")

# Table
import pandas as pd
st.header("Dataframe Tables")
df = pd.DataFrame({"A": [1, 2, 3], "B": [5, 6, 4], "C": [9, 7, 8]})
st.write(df)
st.write("---")


# Load images from URL
st.header("Image from URL")
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/250px-Python-logo-notext.svg.png"
st.image(img_url, caption="Python Logo")
st.write("---")

# Load audio from URL
st.header("Audio from URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url, start_time=30, loop=True)
st.write("---")

# Load video from URL
st.header("Video from URL")
video_url = "https://youtu.be/dQw4w9WgXcQ?si=twGniNRaP866vwoA"
st.video(video_url)
st.write("---")