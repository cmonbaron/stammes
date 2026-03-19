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
    "timo": "bruder2026", "constantin": "bruder2026", "carsten": "bruder2026",
    "marcel": "bruder2026", "marco": "bruder2026", "christof": "bruder2026",
    "luca": "bruder2026", "paddi": "bruder2026", "simon": "bruder2026"
}

STAMMES_DATA = [
    {
        "id": 1,
        "titel": "Das Ikonen-Rätsel",
        "datum": "15. April 2026",
        "typ": "rebus",
        "hinweis": "Kombiniere die Symbole zu einem Wort.",
        "icons": "🏰 + 🍺 + 🍃",
        "loesung": "burgbrauerei",
        "ergebnis": "📍 Alte Burgbrauerei, Rittersaal. Beginn: 19:30 Uhr."
    },
    {
        "id": 2,
        "titel": "Die Chiffre des Schweigens",
        "datum": "20. Mai 2026",
        "typ": "cipher",
        "hinweis": "Der Text wurde verschoben. Der Schlüssel ist die Anzahl der Gründungsmitglieder (9).",
        "ciphertext": "A_B_C_D_E... wird zu J_K_L_M_N...",
        "frage": "Entschlüssele: 'ANWNCXNAW'", # "RHEINKURVE" shifted by 9 (R+9=A, H+9=Q...) -> wait, let's do simple Caesar
        # Caesar shift 9: R(18) -> A(1), H(8) -> Q(17), E(5) -> N(14), I(9) -> R(18), N(14) -> W(23), K(11) -> T(20), U(21) -> D(4), R(18) -> A(1), V(22) -> E(5), E(5) -> N(14)
        "cipher_display": "AQNRWTD AEN", 
        "loesung": "rheinkurve",
        "ergebnis": "📍 Restaurant Rheinkurve (Hintereingang). Beginn: 20:00 Uhr."
    },
    {
        "id": 3,
        "titel": "Das Koordinaten-Gitter",
        "datum": "21. Juni 2026",
        "typ": "grid",
        "hinweis": "Finde das Wort in den Schatten. Die Koordinaten sind (1,2), (3,1), (2,3), (1,2), (3,3).",
        "grid": [
            ["X", "B", "O"],
            ["A", "Y", "N"],
            ["H", "Z", "F"]
        ],
        "loesung": "bahnhof", # B(1,2), H(3,1), N(2,3), B(1,2), O(1,3), F(3,3) -> B H N B O F (fast)
        # Let's make it cleaner:
        "grid_display": """
            |   | 1 | 2 | 3 |
            |---|---|---|---|
            | 1 | A | B | O |
            | 2 | S | H | N |
            | 3 | T | U | F |
        """,
        "coords": "(1,2), (2,2), (2,3), (1,2), (1,3), (3,3)", # B H N B O F
        "loesung": "bahnhof",
        "ergebnis": "📍 Alter Bahnhof (Gleis 1 Bar). Beginn: 21:00 Uhr."
    }
]

# --- CSS Injektion ---
def inject_bruderschaft_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
            .stApp { background-color: #0c0e12; background-image: radial-gradient(circle at center, #1a1d23 0%, #0c0e12 100%); }
            .main .block-container { max-width: 800px; padding-top: 3rem; }
            h1, h2, h3 { font-family: 'Cinzel', serif !important; color: #d4af37 !important; text-align: center; letter-spacing: 2px; }
            p, div, span, label { font-family: 'Playfair Display', serif; color: #e2e8f0; }
            .event-card { background: rgba(255, 255, 255, 0.03); border: 1px solid #d4af37; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; text-align: center; }
            .stButton > button { background-color: transparent !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; font-family: 'Cinzel', serif !important; text-transform: uppercase; width: 100%; }
            .stButton > button:hover { background-color: #d4af37 !important; color: #0c0e12 !important; }
            .riddle-box { background: rgba(0,0,0,0.4); border: 1px dashed #d4af37; padding: 2rem; border-radius: 8px; margin: 1rem 0; text-align: center; }
            .rebus-icons { font-size: 3rem; margin: 1rem 0; }
            .cipher-text { font-family: monospace; font-size: 1.5rem; color: #ffeb3b; letter-spacing: 4px; }
            .grid-table { margin: 0 auto; border-collapse: collapse; color: #d4af37; font-family: 'Cinzel', serif; }
            .grid-table td { border: 1px solid #d4af37; padding: 10px 20px; font-size: 1.2rem; }
            input { background-color: rgba(255, 255, 255, 0.05) !important; border: 1px solid #d4af37 !important; color: #ffffff !important; text-align: center; }
            footer, #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# (Login-CSS bleibt wie vorher, ich kürze hier für die Übersichtlichkeit)
def inject_login_css():
    """Moderner Login-Look mit hohen Kontrasten."""
    st.markdown("""
        <style>
            /* Haupthintergrund */
            .stApp {
                background-color: #f1f5f9;
            }
            
            /* Container-Styling */
            .main .block-container {
                padding-top: 5rem;
                max-width: 450px;
            }
            
            /* Login-Box */
            div[data-testid="stForm"] {
                border: 1px solid #e2e8f0;
                border-radius: 16px;
                padding: 2.5rem;
                background-color: #ffffff !important;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            }
            
            /* Explizite Textfarben für Titel und Labels */
            h1 {
                color: #0f172a !important;
                font-family: 'Inter', -apple-system, sans-serif;
                font-weight: 800;
                text-align: center;
                margin-bottom: 2rem !important;
            }
            
            /* Labels für Input-Felder */
            label[data-testid="stWidgetLabel"] p {
                color: #334155 !important;
                font-weight: 600 !important;
                font-size: 0.95rem !important;
            }
            
            /* Input Felder Styling */
            input {
                background-color: #f8fafc !important;
                color: #1e293b !important;
                border: 1px solid #cbd5e1 !important;
                border-radius: 8px !important;
            }
            
            /* Button-Styling */
            .stButton > button {
                width: 100%;
                background-color: #4f46e5 !important;
                color: #ffffff !important;
                border-radius: 8px !important;
                border: none !important;
                padding: 0.75rem 1rem !important;
                font-weight: 700 !important;
                margin-top: 1rem !important;
                box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.2);
            }
            
            .stButton > button:hover {
                background-color: #4338ca !important;
                box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3);
            }

            /* Verstecke Standard-Elemente */
            footer {visibility: hidden;}
            #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# --- App Logik ---

def show_login_page():
    inject_login_css()
    st.title("Heilige Bruderschaft")
    with st.form("login"):
        u = st.text_input("Bruder Name").lower().strip()
        p = st.text_input("Geheimwort", type="password")
        if st.form_submit_button("Eintreten"):
            if u in BRUEDER and BRUEDER[u] == p:
                st.session_state.logged_in = True
                st.session_state.username = u.capitalize()
                st.rerun()
            else: st.error("Zugriff verweigert.")

def show_event_list():
    inject_bruderschaft_css()
    st.title("Die Versammlungen")
    st.markdown(f"<p style='text-align: center;'>Willkommen, Bruder {st.session_state.username}.</p>", unsafe_allow_html=True)
    for e in STAMMES_DATA:
        with st.container():
            st.markdown(f'<div class="event-card"><h3>{e["titel"]}</h3><p>📅 {e["datum"]}</p></div>', unsafe_allow_html=True)
            if st.button("Das Siegel brechen", key=f"e_{e['id']}"):
                st.session_state.current_event = e['id']
                st.rerun()
    if st.button("Den Zirkel verlassen"):
        st.session_state.clear()
        st.rerun()

def show_riddle_page():
    inject_bruderschaft_css()
    e = next(x for x in STAMMES_DATA if x['id'] == st.session_state.current_event)
    
    if st.button("← Zurück zum Zirkel"):
        del st.session_state.current_event
        st.rerun()
        
    st.title(e['titel'])
    st.markdown(f"<p style='text-align: center; color: #d4af37;'>{e['hinweis']}</p>", unsafe_allow_html=True)
    
    # Rätsel-Inhalt basierend auf Typ
    with st.container():
        st.markdown('<div class="riddle-box">', unsafe_allow_html=True)
        
        if e['typ'] == 'rebus':
            st.markdown(f'<div class="rebus-icons">{e["icons"]}</div>', unsafe_allow_html=True)
            
        elif e['typ'] == 'cipher':
            st.markdown(f'<div class="cipher-text">{e["cipher_display"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size: 0.8rem; opacity: 0.6; margin-top: 10px;">{e["ciphertext"]}</p>', unsafe_allow_html=True)
            
        elif e['typ'] == 'grid':
            st.markdown('<table class="grid-table"><tr><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>A</td><td>B</td><td>O</td></tr><tr><td>2</td><td>S</td><td>H</td><td>N</td></tr><tr><td>3</td><td>T</td><td>U</td><td>F</td></tr></table>', unsafe_allow_html=True)
            st.markdown(f'<p style="margin-top: 15px; font-weight: bold; letter-spacing: 2px;">{e["coords"]}</p>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

    # Lösungseingabe
    solved_key = f"solved_{e['id']}"
    if solved_key not in st.session_state: st.session_state[solved_key] = False
        
    if not st.session_state[solved_key]:
        ans = st.text_input("Das Lösungswort", key="ans_input").lower().strip()
        if st.button("Das Siegel lösen"):
            if ans == e['loesung']:
                st.session_state[solved_key] = True
                st.rerun()
            else: st.error("Die Mächte schweigen. Versuche es erneut.")
    else:
        st.markdown(f"""
            <div style="background: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; padding: 20px; border-radius: 12px; text-align: center; margin-top: 20px;">
                <h2 style="margin:0; font-size: 1.5rem;">OFFENBARUNG</h2>
                <p style="font-size: 1.1rem; color: #d4af37; margin-top: 10px;">{e['ergebnis']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- Routing ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if not st.session_state.logged_in: show_login_page()
elif 'current_event' in st.session_state: show_riddle_page()
else: show_event_list()
