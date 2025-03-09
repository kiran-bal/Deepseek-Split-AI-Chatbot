"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

import streamlit as st

def configure_sidebar(roles: dict):
    """Configure the application sidebar with enhanced controls."""
    with st.sidebar:
        st.markdown("**Author:** Kiran Bal")
        st.header("⚙️ Configuration")

        # Model selection
        st.session_state.selected_model = st.selectbox(
            "Select Model",
            options=["deepseek-r1:1.5b", "deepseek-r1:7b"],
            index=0 if st.session_state.selected_model == "deepseek-r1:1.5b" else 1
        )

        # Role selection
        selected_role = st.selectbox(
            "Choose Role",
            options=list(roles.keys()),
            format_func=lambda x: roles[x]().icon + " " + x
        )

        # Update role if changed
        if st.session_state.current_role != selected_role:
            st.session_state.current_role = selected_role
            st.session_state.message_log = []

        role_instance = roles[selected_role]()

        st.divider()
        st.markdown(f"### {role_instance.icon} Capabilities")
        st.markdown("\n".join(
            [f"- {cap}" for cap in role_instance.capabilities]
        ), unsafe_allow_html=True)

        st.divider()
        st.checkbox(
            "Hide Analysis Tags",
            key="hide_think_tags",
            help="Hide content within <think> tags"
        )
        st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")