import streamlit as st

# --- Konfiguration ---
st.set_page_config(
    page_title="Heilige Bruderschaft",
    page_icon="⚜️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Daten der Bruderschaft ---
BRUEDER = {
    "timo": "bruder2026",
    "constantin": "bruder2026",
    "carsten": "bruder2026",
    "marcel": "bruder2026",
    "marco": "bruder2026",
    "christof": "bruder2026",
    "luca": "bruder2026",
    "paddi": "bruder2026",
    "simon": "bruder2026"
}

STAMMES_DATA = [
    {
        "id": 1,
        "titel": "Der Frühlings-Stammes",
        "datum": "15. April 2026",
        "raetsel": "Suche den Ort, der nach dem Patron der Jäger benannt ist und wo das Wild am besten schmeckt.",
        "loesung": "hubertus",
        "ergebnis": "📍 Gasthaus St. Hubertus, Hauptstraße 12. Beginn: 19:30 Uhr."
    },
    {
        "id": 2,
        "titel": "Die Versammlung im Mai",
        "datum": "20. Mai 2026",
        "raetsel": "Dort, wo der Fluss eine scharfe Kurve macht und der Anker für immer ruht.",
        "loesung": "rheinkurve",
        "ergebnis": "📍 Restaurant Rheinkurve (Hintereingang). Beginn: 20:00 Uhr."
    },
    {
        "id": 3,
        "titel": "Sonnwend-Stammes",
        "datum": "21. Juni 2026",
        "raetsel": "Einst wurden hier Schienen verlegt, heute wird hier das Hopfen-Gold ausgeschenkt. Wo enden die Gleise?",
        "loesung": "bahnhof",
        "ergebnis": "📍 Alter Bahnhof (Gleis 1 Bar). Beginn: 21:00 Uhr."
    }
]

# --- CSS Injektion ---
def inject_login_css():
    """Moderner Login-Look."""
    st.markdown("""
        <style>
            .stApp { background-color: #f1f5f9; }
            .main .block-container { padding-top: 5rem; max-width: 450px; }
            div[data-testid="stForm"] {
                border: 1px solid #e2e8f0;
                border-radius: 16px;
                padding: 2.5rem;
                background-color: #ffffff !important;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            }
            h1 { color: #0f172a !important; font-weight: 800; text-align: center; }
            label p { color: #334155 !important; font-weight: 600 !important; }
            input { background-color: #f8fafc !important; color: #1e293b !important; }
            .stButton > button {
                width: 100%;
                background-color: #4f46e5 !important;
                color: #ffffff !important;
                border-radius: 8px !important;
                font-weight: 700 !important;
            }
            footer {visibility: hidden;}
            #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

def inject_bruderschaft_css():
    """Edler Bruderschafts-Look: Dark & Gold."""
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
            
            .stApp {
                background-color: #0c0e12;
                background-image: radial-gradient(circle at center, #1a1d23 0%, #0c0e12 100%);
            }
            
            .main .block-container {
                max-width: 800px;
                padding-top: 3rem;
            }
            
            h1, h2, h3 {
                font-family: 'Cinzel', serif !important;
                color: #d4af37 !important;
                text-align: center;
                letter-spacing: 2px;
            }
            
            p, div {
                font-family: 'Playfair Display', serif;
                color: #e2e8f0;
            }
            
            /* Event Karten */
            .event-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid #d4af37;
                border-radius: 12px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                transition: transform 0.3s ease;
            }
            
            .event-card:hover {
                transform: translateY(-5px);
                background: rgba(212, 175, 55, 0.05);
            }
            
            /* Buttons */
            .stButton > button {
                background-color: transparent !important;
                color: #d4af37 !important;
                border: 1px solid #d4af37 !important;
                border-radius: 4px !important;
                font-family: 'Cinzel', serif !important;
                font-weight: 700 !important;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            .stButton > button:hover {
                background-color: #d4af37 !important;
                color: #0c0e12 !important;
            }

            hr { border-color: #d4af37 !important; opacity: 0.3; }
            
            /* Input für Rätsel */
            .stTextInput input {
                background-color: rgba(255, 255, 255, 0.05) !important;
                border: 1px solid #d4af37 !important;
                color: #ffffff !important;
            }
            
            footer {visibility: hidden;}
            #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# --- App Logik ---

def show_login_page():
    inject_login_css()
    st.title("Heilige Bruderschaft")
    
    with st.form("login_form"):
        username = st.text_input("Name eines Bruders", placeholder="Dein Vorname").lower().strip()
        password = st.text_input("Geheimes Wort", type="password", placeholder="••••••••")
        submitted = st.form_submit_button("Eintreten")

        if submitted:
            if username in BRUEDER and BRUEDER[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username.capitalize()
                st.rerun()
            else:
                st.error("Der Zugang bleibt verwehrt. Name oder Wort ist falsch.")

def show_event_list():
    inject_bruderschaft_css()
    st.title("Die Versammlungen")
    st.markdown(f"<p style='text-align: center; font-style: italic;'>Sei gegrüßt, Bruder {st.session_state.username}.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    for event in STAMMES_DATA:
        with st.container():
            # Wir nutzen HTML für die Karten-Optik
            st.markdown(f"""
                <div class="event-card">
                    <h3 style="margin-top: 0;">{event['titel']}</h3>
                    <p>📅 <b>Datum:</b> {event['datum']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Das Rätsel lösen", key=f"btn_{event['id']}"):
                st.session_state.current_event = event['id']
                st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Den Zirkel verlassen"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

def show_riddle_page():
    inject_bruderschaft_css()
    event = next(e for e in STAMMES_DATA if e['id'] == st.session_state.current_event)
    
    if st.button("← Zurück"):
        del st.session_state.current_event
        st.rerun()
        
    st.title(event['titel'])
    st.markdown(f"<p style='text-align: center;'>{event['datum']}</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("Das Rätsel")
    st.info(event['raetsel'])
    
    # Zustand des Rätsels prüfen
    solved_key = f"solved_{event['id']}"
    if solved_key not in st.session_state:
        st.session_state[solved_key] = False
        
    if not st.session_state[solved_key]:
        answer = st.text_input("Deine Antwort", placeholder="Ein Wort...").lower().strip()
        if st.button("Antwort prüfen"):
            if answer == event['loesung']:
                st.session_state[solved_key] = True
                st.success("Richtig! Die Bruderschaft offenbart den Ort.")
                st.rerun()
            else:
                st.error("Das ist nicht die Antwort, die wir suchen.")
    else:
        st.markdown(f"""
            <div style="background: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; padding: 20px; border-radius: 12px; text-align: center;">
                <h2 style="margin:0;">OFFENBARUNG</h2>
                <p style="font-size: 1.2rem; color: #d4af37; font-weight: bold; margin-top: 10px;">
                    {event['ergebnis']}
                </p>
            </div>
        """, unsafe_allow_html=True)

# --- Session State Initialisierung ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- Routing ---
if not st.session_state.logged_in:
    show_login_page()
elif 'current_event' in st.session_state:
    show_riddle_page()
else:
    show_event_list()
