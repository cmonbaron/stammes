import streamlit as st

# In einer echten Anwendung sollten Sie die Anmeldeinformationen sicher speichern,
# z.B. mit st.secrets oder Umgebungsvariablen.
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "123"

def show_login_page():
    """Zeigt die Anmeldeseite an."""
    st.set_page_config(layout="centered")
    
    st.markdown(f"""
        <style>
            .stApp {{
                background-color: #f0f2f6;
            }}
            .main .block-container {{
                padding-top: 2rem;
                padding-bottom: 2rem;
            }}
            .st-emotion-cache-18ni7ap {{
                border: 1px solid #e6e6e6;
                border-radius: 10px;
                padding: 2rem;
                background-color: white;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.title("Login")
        
        with st.form("login_form", clear_on_submit=True):
            username = st.text_input("Benutzername", placeholder="Geben Sie Ihren Benutzernamen ein")
            password = st.text_input("Passwort", type="password", placeholder="Geben Sie Ihr Passwort ein")
            
            submitted = st.form_submit_button("Anmelden")

            if submitted:
                if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Benutzername oder Passwort ist falsch")

def show_welcome_page():
    """Zeigt die Willkommensseite nach erfolgreicher Anmeldung."""
    st.set_page_config(layout="wide")
    st.title(f"Willkommen, {st.session_state.username}!")
    st.write("Sie haben sich erfolgreich angemeldet.")
    
    if st.button("Abmelden"):
        # Clear the entire session state on logout
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


# --- Hauptlogik der App ---
# Initialisieren des Session State, falls noch nicht geschehen
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ''


# Bedingtes Rendern der Seiten
if st.session_state.logged_in:
    show_welcome_page()
else:
    show_login_page()
