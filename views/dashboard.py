# views/dashboard.py
import streamlit as st
from modules.data import STAMMES_DATA
from modules.ui_helper import inject_bruderschaft_style

def show_dashboard(authenticator):
    inject_bruderschaft_style()
    st.title("Die Versammlungen")
    st.markdown(f"<p style='text-align: center;'>Sei gegrüßt, Bruder {st.session_state['name']}.</p>", unsafe_allow_html=True)
    
    for e in STAMMES_DATA:
        solved = st.session_state.get(f"solved_{e['id']}", False)
        card_class = "event-card solved" if solved else "event-card"
        badge = '<div class="solved-badge">⚜️ ENTSCHLÜSSELT</div>' if solved else ""
        
        with st.container():
            st.markdown(f'''
                <div class="{card_class}">
                    <h3>{e["titel"]}</h3>
                    <p>📅 {e["datum"]}</p>
                    {badge}
                </div>
            ''', unsafe_allow_html=True)
            
            button_label = "Die Offenbarung ansehen" if solved else "Das Siegel brechen"
            if st.button(button_label, key=f"e_{e['id']}"):
                st.session_state.current_event = e['id']
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    authenticator.logout('Den Zirkel verlassen', 'main')
