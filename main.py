"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

import streamlit as st
from ui.styles import inject_styles
from ui.sidebar import configure_sidebar
from ui.chat import render_chat_interface
from controllers.chat_controller import handle_user_query
from utils.helpers import initialize_session_state, load_roles

def main():
    """Main application entry point"""
    # Configure UI
    st.set_page_config(page_title="Split")
    inject_styles()
    st.title("🧠 DeepSeek Multi-Role Assistant")

    # Initialize core components
    initialize_session_state()
    roles = load_roles()

    # Configure sidebar
    configure_sidebar(roles)

    # Set current role class
    if st.session_state.current_role:
        st.session_state.current_role_class = roles[st.session_state.current_role]

    # Render chat interface
    render_chat_interface()

    # Handle user input
    user_query = st.chat_input("Type your message here...")
    if user_query and st.session_state.current_role:
        handle_user_query(user_query, roles)

if __name__ == "__main__":
    main()