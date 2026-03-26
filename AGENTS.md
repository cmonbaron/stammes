# 🤖 KI-Kontext: Heilige Bruderschaft

Dieses Dokument ist der Einstiegspunkt für KI-Assistenten. Das Projekt folgt dem **Spec-Driven Development (SDD)** Ansatz und einer modularen Streamlit-Architektur.

## 🛠️ Technologie-Stack
- **Framework:** [Streamlit](https://streamlit.io/) (Python).
- **Authentifizierung:** `streamlit-authenticator`.
- **Styling:** Custom CSS (in `styles/`) via `st.markdown(unsafe_allow_html=True)`.
- **Datenhaltung:** In-Memory via `st.session_state` (für die Session) und statische Daten in `modules/data.py`.

## 📁 Projektstruktur & Konventionen
Jeder KI-Assistent MUSS diese Struktur respektieren und neue Logik entsprechend einordnen:

- **`streamlit_app.py`**: Zentraler Entry Point, Routing und globale Injections (wie Audio/CSS).
- **`modules/`**: Reine Logik, Datenverarbeitung und Hilfsfunktionen (z. B. `data.py`, `ui_helper.py`). Hier gehört kein UI-Code hin, der direkt `st.write` nutzt, es sei denn als dedizierte UI-Komponente.
- **`views/`**: Die einzelnen "Seiten" oder Ansichten der App (z. B. `dashboard.py`, `riddle.py`). Diese werden von `streamlit_app.py` aufgerufen.
- **`styles/`**: Alle CSS-Dateien. Diese werden über Hilfsfunktionen geladen und injiziert.
- **`.specs/`**: Dokumentation des Fortschritts und der Anforderungen nach SDD.

## ⚙️ Workflow (Spec-Driven Development)
Für jede Änderung folgen wir diesem Prozess:
1. **Requirements** definieren (`01_requirements.md`).
2. **Spec** technisch präzisieren (`02_spec.md`).
3. **Plan** für die Umsetzung erstellen (`03_plan.md`).
4. **Tasks** Schritt für Schritt abarbeiten (`04_tasks.md`).

## 🔑 Wichtige Projekt-Anker
- **Entry Point:** `streamlit_app.py`.
- **Zentrale Daten:** `modules/data.py` (Zentrale Liste `STAMMES_DATA`).
- **Styling-Leitfaden:** Bruderschaft-Design (Schwarz/Gold/Dunkelrot).
- **Session States:** `authentication_status`, `current_event`, `solved_<id>`, `audio_playing`.
