"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

import streamlit as st

APP_STYLES = """
<style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    .sidebar .sidebar-content { background-color: #2d2d2d; }
    .stTextInput textarea { color: #ffffff !important; }
    .stSelectbox div[data-baseweb="select"] { 
        color: white !important; 
        background-color: #3d3d3d !important; 
    }
    .stSelectbox svg { fill: white !important; }
    .role-header { font-size: 1.5em; margin-bottom: 20px; }
    .capability-list { padding-left: 20px; }
    .think-tag { color: #6c757d; font-style: italic; }
</style>
"""

def inject_styles():
    """Inject custom CSS styles into the Streamlit app"""
    st.markdown(APP_STYLES, unsafe_allow_html=True)