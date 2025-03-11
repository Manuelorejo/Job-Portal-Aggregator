import streamlit as st
from Homepage import show_homepage
from search_page import show_search_page

# Set page title and description
st.set_page_config(
    page_title="Nigerian Job Search Aggregator",
    page_icon="🔍",
    layout="wide"
)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Enhanced CSS for styling with updated colors and borders
st.markdown("""
<style>
    body {
        background-color: #f5f5f5;
    }
    .job-card {
        background-color: #f0f0f0;  /* Changed to light grey background */
        border: 2px solid #000000;
        border-radius: 10px;
        padding: 24px;
        margin-bottom: 24px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    .job-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        border-color: #333333;
    }
    .job-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 12px;
        color: #000000;
    }
    .job-meta {
        font-size: 15px;
        margin: 8px 0;
        color: #444444;
    }
    .job-source {
        font-weight: 500;
        color: #000000;
        background-color: #ffffff;  /* Changed to white background */
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    .job-mode {
        font-weight: 500;
        color: #000000;
        background-color: #e6f7ff;  /* Light blue background for job mode */
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-left: 10px;
    }
    .apply-btn {
        background-color: #d3d3d3;  /* Changed to light grey color */
        color: black;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 15px;
        margin-top: 15px;
        border-radius: 5px;
        font-weight: 500;
        transition: background-color 0.2s ease;
    }
    .apply-btn:hover {
        background-color: #c0c0c0;  /* Slightly darker grey on hover */
    }
    .main-title {
        text-align: center;
        padding: 25px 0;
        margin-bottom: 35px;
        background: #000000;
        color: white;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .search-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    .feature-card {
        background-color: #f8f8f8;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .get-started-btn {
        background-color: #000000;
        color: white;
        padding: 12px 30px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 30px 0;
        border-radius: 5px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .get-started-btn:hover {
        background-color: #333333;
    }
    .home-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    .home-welcome {
        font-size: 20px;
        margin: 30px 0;
        text-align: center;
        line-height: 1.6;
    }
    .home-image {
        width: 100%;
        border-radius: 10px;
        margin: 20px 0;
    }
    .back-btn {
        background-color: #f0f0f0;
        color: #333;
        padding: 8px 15px;
        border-radius: 5px;
        cursor: pointer;
        margin-bottom: 20px;
        display: inline-block;
        text-decoration: none;
    }
    .back-btn:hover {
        background-color: #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# Determine which page to show
if st.session_state.page == "home":
    show_homepage()
else:
    show_search_page()

# Footer (shown on both pages)
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p>© 2025 Nigerian Job Search Aggregator | Data from LinkedIn, Jobberman, JobsGuru, HotNigerianJobs, and MyJobMag</p>
</div>
""", unsafe_allow_html=True)