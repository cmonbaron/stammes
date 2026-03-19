# views/dashboard.py
import streamlit as st
from modules.data import STAMMES_DATA
from modules.ui_helper import inject_bruderschaft_style

def show_dashboard(authenticator):
    inject_bruderschaft_style()
    st.title("Die Versammlungen")
    st.markdown(f"<p style='text-align: center;'>Sei gegrüßt, Bruder {st.session_state['name']}.</p>", unsafe_allow_html=True)
    
    for e in STAMMES_DATA:
        with st.container():
            st.markdown(f'<div class="event-card"><h3>{e["titel"]}</h3><p>📅 {e["datum"]}</p></div>', unsafe_allow_html=True)
            if st.button("Das Siegel brechen", key=f"e_{e['id']}"):
                st.session_state.current_event = e['id']
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    authenticator.logout('Den Zirkel verlassen', 'main')
