# Spec: Dashboard
- **Komponente:** `views/dashboard.py`.
- **Datenquelle:** `modules/data.py` (`STAMMES_DATA`).
- **UI:** CSS-Klasse `.event-card` (in `styles/bruderschaft.css`).
- **Logik:** 
    - Prüft `st.session_state["name"]` für Begrüßung.
    - Iteriert über `STAMMES_DATA`.
    - Button-Klick setzt `st.session_state.current_event = id` und triggert `st.rerun()`.
- **Styling:** Injektion von `bruderschaft.css`.
