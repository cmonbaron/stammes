# Spec: Galerie der Offenbarungen

## 🛠️ Technische Umsetzung
1.  **Komponente:** `views/gallery.py`.
2.  **Datenquelle:** `modules/data.py` (`STAMMES_DATA`).
3.  **Logik:** 
    - Iteration über alle Events.
    - Prüfung des Session-States `st.session_state[f"solved_{e['id']}"]`.
    - Anzeige von Titel und `ergebnis` für gelöste Events.
4.  **Navigation:** 
    - Integration in die Sidebar von `streamlit_app.py`.
    - Button zum Zurückkehren zum Dashboard (`st.session_state.page = "dashboard"`).

## 🎨 UI/UX
- Klassisches Bruderschaft-Design.
- Karten- oder Listenansicht mit goldenen Akzenten.
