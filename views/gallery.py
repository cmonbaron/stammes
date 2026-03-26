# views/gallery.py
import streamlit as st
from modules.data import STAMMES_DATA
from modules.ui_helper import inject_bruderschaft_style

def show_gallery():
    inject_bruderschaft_style()
    st.title("Die Offenbarungen")
    st.markdown("<p style='text-align: center;'>Ein Archiv eures Wissens, Brüder.</p>", unsafe_allow_html=True)
    
    solved_any = False
    for e in STAMMES_DATA:
        if st.session_state.get(f"solved_{e['id']}", False):
            solved_any = True
            with st.container():
                st.markdown(f"""
                    <div style="background: rgba(212, 175, 55, 0.05); border-left: 3px solid #d4af37; padding: 20px; border-radius: 4px; margin-bottom: 20px;">
                        <h4 style="margin:0; color: #d4af37;">{e['titel']}</h4>
                        <p style="margin-top: 10px; font-style: italic; color: #e2e8f0;">{e['ergebnis']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
    if not solved_any:
        st.info("Noch wurden keine Siegel gebrochen. Kehrt zum Zirkel zurück.")
        
    if st.button("← Zurück zum Zirkel"):
        st.session_state.page = "dashboard"
        st.rerun()
