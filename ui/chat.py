"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

import streamlit as st
from utils.processors import hide_think_tags

def display_message(message: dict):
    """Display a single chat message with processing."""
    with st.chat_message(message["role"]):
        processed_content = hide_think_tags(
            message["content"],
            st.session_state.hide_think_tags
        )
        st.markdown(processed_content, unsafe_allow_html=True)

def render_chat_interface():
    """Render the main chat interface container"""
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.message_log:
            display_message(message)
    return chat_container