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

# Sidebar for Theme Control
st.sidebar.title("Theme Controls")
theme_btn_label = "☀️ Light Mode" if st.session_state.theme == "dark" else "🌙 Dark Mode"
st.sidebar.button(theme_btn_label, on_click=toggle_theme)

# In Streamlit, every time the user interacts with a widget (button, slider, text input, etc.),
# the entire script reruns from top to bottom. Because of this behavior,
# normal Python variables do not remember their values between interactions.

# st.session_state is a special dictionary-like object in Streamlit
# that stores data for a particular user session.

# It helps your app:
# - Remember values
# - Maintain app state
# - Store user progress
# - Preserve variables between reruns
# - Without session state, variables reset after every interaction.

temp_counter = 0
if "perm_counter" not in st.session_state:
    st.session_state.perm_counter = 0

def incr():
    global temp_counter
    temp_counter += 1
    st.session_state.perm_counter += 1

st.button("Increment", on_click=incr)

st.write(f"TEMP = {temp_counter}")
st.write(f"PERM = {st.session_state.perm_counter}")