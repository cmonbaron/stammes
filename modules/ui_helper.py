# modules/ui_helper.py
import streamlit as st
import os

def load_css(file_path):
    """Liest eine CSS-Datei ein und injiziert sie."""
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def inject_login_style():
    load_css("styles/login.css")

def inject_bruderschaft_style():
    load_css("styles/bruderschaft.css")
