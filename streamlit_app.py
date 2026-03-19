import streamlit as st
import streamlit_authenticator as stauth
from modules.ui_helper import inject_login_style
from views.dashboard import show_dashboard
from views.riddle import show_riddle

# --- Konfiguration ---
st.set_page_config(
    page_title="Heilige Bruderschaft",
    page_icon="⚜️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Authentifizierung Initialisierung ---
authenticator = stauth.Authenticate(
    st.secrets['credentials'].to_dict(),
    st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
    st.secrets['cookie']['expiry_days']
)

# --- Main Entry Point (Routing) ---

# 1. Login-Status prüfen
if not st.session_state.get('authentication_status'):
    inject_login_style()
    st.title("Heilige Bruderschaft")

# 2. Authenticator ausführen
authenticator.login(location='main')

# 3. Seiten-Routing basierend auf Status
if st.session_state["authentication_status"]:
    # Eingeloggt: Entweder Rätsel oder Dashboard
    if 'current_event' in st.session_state:
        show_riddle()
    else:
        show_dashboard(authenticator)

elif st.session_state["authentication_status"] is False:
    st.error('Name oder PIN ist falsch')

elif st.session_state["authentication_status"] is None:
    st.info('Bitte gib deinen Namen und deine PIN ein')
