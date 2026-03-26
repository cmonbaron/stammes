import streamlit as st
import streamlit_authenticator as stauth
from modules.ui_helper import inject_login_style, inject_background_audio
from views.dashboard import show_dashboard
from views.riddle import show_riddle
from views.gallery import show_gallery

# --- Konfiguration ---
st.set_page_config(
    page_title="Heilige Bruderschaft",
    page_icon="⚜️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Authentifizierung Initialisierung ---
# WICHTIG: Credentials und Cookie-Einstellungen müssen exakt mit secrets.toml übereinstimmen
authenticator = stauth.Authenticate(
    st.secrets['credentials'].to_dict(),
    st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
    st.secrets['cookie']['expiry_days']
)

# --- Authenticator ausführen ---
# Die login-Methode prüft automatisch das Cookie und setzt den session_state
# Wir nutzen benannte Argumente, um Fehler in der Argument-Reihenfolge zu vermeiden
authenticator.login(location='main')

# --- Main Entry Point (Routing) ---

if st.session_state["authentication_status"]:
    # 1. Globales Hintergrund-Audio laden
    inject_background_audio("data/song.mp3")
    
    # 2. Sidebar Navigation
    with st.sidebar:
        st.title("Navigation")
        if st.button("🏠 Zirkel (Dashboard)"):
            st.session_state.page = "dashboard"
            if 'current_event' in st.session_state: 
                del st.session_state.current_event
            st.rerun()
        if st.button("📜 Offenbarungen (Galerie)"):
            st.session_state.page = "gallery"
            if 'current_event' in st.session_state: 
                del st.session_state.current_event
            st.rerun()
        st.markdown("---")

    # 3. Routing
    if 'current_event' in st.session_state:
        show_riddle()
    elif st.session_state.get('page') == 'gallery':
        show_gallery()
    else:
        show_dashboard(authenticator)

elif st.session_state["authentication_status"] is False:
    inject_login_style()
    st.title("Heilige Bruderschaft")
    st.error('Der Zugang wurde verwehrt. Codename oder Schlüssel ist falsch.')

elif st.session_state["authentication_status"] is None:
    inject_login_style()
    st.title("Heilige Bruderschaft")
    st.info('Identifiziere dich, Bruder.')
