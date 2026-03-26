# Spec: Hintergrund-Audio Integration

## 🛠️ Technische Umsetzung
1.  **Dateiquelle:** `data/song.mp3` (wird als Base64 in das HTML-Snippet eingebettet oder via Streamlit Static Serving bereitgestellt).
2.  **Platzierung:** `streamlit_app.py`, im Bereich für authentifizierte Nutzer.
3.  **Komponente:** 
    - Einbettung eines HTML5 `<audio>` Tags mit JavaScript-Logik.
    - JavaScript versucht `audio.play()` beim Laden.
    - Bei Fehlern (NotAllowedError) wird dem Nutzer ein unauffälliger "Musik aktivieren" Button angezeigt.
4.  **Zustandsverwaltung:** `st.session_state.audio_playing` zur Steuerung des Zustands.

## 🎨 UI/UX
- Platzierung idealerweise in der Sidebar ganz unten.
- Ein dezentes Icon (🔊/🔇) zeigt den aktuellen Status an.
