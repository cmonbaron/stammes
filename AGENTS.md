# Projekt-Kontext: Heilige Bruderschaft (Streamlit App)

Dieses Dokument dient als Schnellstart-Referenz für KI-Assistenten, um den Aufbau und die Logik der Anwendung sofort zu verstehen.

## 🚀 Projektübersicht
Eine thematische Streamlit-Anwendung für eine geschlossene Gruppe ("Heilige Bruderschaft"). Die App dient zur Verwaltung von Versammlungen, die erst nach dem Lösen von Rätseln (Rebus, Chiffre, Koordinaten) freigeschaltet werden.

## 🔑 Authentifizierung
- **Bibliothek:** `streamlit-authenticator` (Version 0.4.x).
- **Konfiguration:** Gespeichert in `.streamlit/secrets.toml` (`credentials`, `cookie`).
- **Nutzer:** 9 vordefinierte Brüder (siehe `hash_gen.py`).
- **Passwort-Hashing:** Über `stauth.Hasher`.

## 📂 Ordnerstruktur & Logik
- **`streamlit_app.py`**: Zentraler Entry-Point. Handhabt das Login-System und das Routing zwischen Dashboard und Rätsel-Ansicht basierend auf dem `session_state`.
- **`modules/`**:
    - `data.py`: Enthält `STAMMES_DATA` (Liste von Dictionaries mit Rätseln, Lösungen und Ergebnissen).
    - `ui_helper.py`: Funktionen zum Injizieren von CSS (`load_css`).
- **`views/`**:
    - `dashboard.py`: Zeigt die Liste der Versammlungen als Karten ("Das Siegel brechen").
    - `riddle.py`: Die Logik zum Lösen der Rätsel. Prüft Eingaben gegen `data.py` und speichert den Fortschritt im `session_state`.
- **`styles/`**:
    - `login.css` & `bruderschaft.css`: Sorgen für das dunkle/geheimnisvolle "Bruderschafts"-Design.
- **`hash_gen.py`**: Hilfsskript zum Generieren der Passwort-Hashes für die `secrets.toml`.

## 🛠 Wichtige Session-States
- `authentication_status`: `True` (eingeloggt), `False` (Fehler), `None` (kein Login).
- `current_event`: ID des aktuell ausgewählten Rätsels.
- `solved_<id>`: Boolean, ob ein spezifisches Rätsel bereits gelöst wurde.

## 💡 Entwicklungshinweise
- Neue Rätsel werden einfach in `modules/data.py` hinzugefügt.
- Layout-Anpassungen erfolgen primär über die CSS-Dateien in `styles/`.
- Für lokale Tests müssen die Secrets in `.streamlit/secrets.toml` vorhanden sein.
