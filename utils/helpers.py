"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

from typing import Type, Dict, List
import importlib
import inspect
from pathlib import Path
import streamlit as st

from roles.base_role import BaseRole


def load_roles(roles_dir: str = "roles") -> Dict[str, Type]:
    """Dynamically load all available roles from roles directory."""
    roles = {}
    for file_path in Path(roles_dir).glob("*.py"):
        if file_path.stem == "__init__":
            continue

        module = importlib.import_module(f"{roles_dir}.{file_path.stem}")
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, BaseRole) and obj != BaseRole:
                roles[obj().role_name] = obj
    return roles


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    default_state = {
        "message_log": [],
        "current_role": None,
        "selected_model": "deepseek-r1:1.5b",
        "hide_think_tags": False
    }

    for key, value in default_state.items():
        if key not in st.session_state:
            st.session_state[key] = value