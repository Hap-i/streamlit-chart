
import streamlit as st

# Import custom utility functions
from utils.get_data import get_data
from app_brain.handle_openai_query import handle_openai_query
from dotenv import load_dotenv
import os

load_dotenv()
# Suppress deprecation warnings related to Pyplot's global use
st.set_option("deprecation.showPyplotGlobalUse", False)


# Cache the header of the app to prevent re-rendering on each load
@st.cache_resource
def display_app_header():
    """Display the header of the Streamlit app."""
    st.title("Chart APP")
    st.markdown(
        "***Prompt about your data, and see it visualized** ✨ This app runs on the power of your prompting.*")


# Display the header of the app
display_app_header()

API = os.environ.get('OPENAI_API_KEY')

if API:
    os.environ["OPENAI_API_KEY"] = API

    df = get_data()

    # If data is uploaded successfully
    if df is not None:
        # Create an expander to optionally display the uploaded data
        with st.expander("Show data"):
            st.write(df)

        # Extract column names for further processing
        column_names = ", ".join(df.columns)

        # Check if the uploaded DataFrame is not empty
        if not df.empty:
            # Handle the OpenAI query and display results
            handle_openai_query(df, column_names)
        else:
            # Display a warning if the uploaded data is empty
            st.warning("The given data is empty.")
