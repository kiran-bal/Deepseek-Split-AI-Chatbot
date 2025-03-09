"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

from langchain_ollama.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from utils.processors import format_streaming_response, hide_think_tags
import streamlit as st


def initialize_chat_engine():
    """Initialize the LLM chat engine based on current configuration"""
    return ChatOllama(
        model=st.session_state.selected_model,
        system=st.session_state.current_role_class().system_prompt,
        temperature=0.3,
        base_url="http://localhost:11434"
    ) | StrOutputParser()


def handle_user_query(user_query: str, roles: dict):
    """Process user query and generate streaming response"""
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})

    # Generate prompt chain
    prompt_chain = ChatPromptTemplate.from_messages([
        ("system", roles[st.session_state.current_role]().system_prompt),
        *[(msg["role"], msg["content"]) for msg in st.session_state.message_log]
    ])

    # Stream response
    processing_chain = initialize_chat_engine()

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        for chunk in processing_chain.stream(prompt_chain.format_messages()):
            processed_chunk = format_streaming_response(chunk)
            if processed_chunk:
                full_response += processed_chunk
                displayed_chunk = hide_think_tags(
                    full_response,
                    st.session_state.hide_think_tags
                )
                response_placeholder.markdown(displayed_chunk + "▌", unsafe_allow_html=True)

        # Finalize response
        response_placeholder.markdown(full_response)
        st.session_state.message_log.append({"role": "assistant", "content": full_response})