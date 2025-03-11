import streamlit as st

# Set page title and description - this must be the first Streamlit command
st.set_page_config(
    page_title="Nigerian Job Search Aggregator",
    page_icon="🔍",
    layout="wide"
)

# Enhanced CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f5f5f5;
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
    .main-title {
        text-align: center;
        padding: 25px 0;
        margin-bottom: 35px;
        background: #000000;
        color: white;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
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
    .nav-btn {
        background-color: #000000;
        color: white;
        padding: 12px 30px;
        text-align: center;
        display: inline-block;
        font-size: 18px;
        margin: 30px 0;
        border-radius: 5px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .nav-btn:hover {
        background-color: #333333;
    }
    .center-btn {
        display: flex;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<div class="main-title"><h1>Nigerian Job Search Aggregator</h1><p>Your one-stop portal for finding the best jobs in Nigeria</p></div>', unsafe_allow_html=True)

# Welcome message
st.markdown('<div class="home-container">', unsafe_allow_html=True)
st.markdown('<p class="home-welcome">Welcome to Nigerian Job Search Aggregator, the most comprehensive job search tool for Nigerian professionals. Our platform aggregates job listings from top recruitment websites including LinkedIn, Jobberman, JobsGuru, HotNigerianJobs, and MyJobMag, giving you access to thousands of opportunities with just one search.</p>', unsafe_allow_html=True)

# Key features section
st.markdown("<h2>Key Features</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🔎 Unified Search</h3>
        <p>Search across multiple job portals with a single query, saving you time and effort.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Comprehensive Results</h3>
        <p>Get results from Nigeria's top job sites in one organized interface.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📍 Location-Based Search</h3>
        <p>Find jobs in specific cities or remote opportunities across Nigeria.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🚀 Fast Application</h3>
        <p>Apply directly to jobs with a single click through to the original posting.</p>
    </div>
    """, unsafe_allow_html=True)

# How it works section
st.markdown("<h2>How It Works</h2>", unsafe_allow_html=True)
st.markdown("""
<ol>
    <li><strong>Enter Keywords</strong> - Type in job titles, skills, or keywords</li>
    <li><strong>Specify Location</strong> - Enter a city or "Remote" for work-from-home positions</li>
    <li><strong>Search</strong> - Click the search button to aggregate results</li>
    <li><strong>Apply</strong> - Click "Apply Now" on any job listing to go directly to the application page</li>
</ol>
""", unsafe_allow_html=True)

# Navigation button to search page
st.markdown('<div class="center-btn">', unsafe_allow_html=True)
if st.button("Start Searching Now", key="go_to_search"):
    st.switch_page("pages/search_page.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close home-container

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p>© 2025 Nigerian Job Search Aggregator | Data from LinkedIn, Jobberman, JobsGuru, HotNigerianJobs, and MyJobMag</p>
</div>
""", unsafe_allow_html=True)