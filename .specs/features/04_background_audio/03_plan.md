# Plan: Hintergrund-Audio Implementierung

## 1. Vorbereitung
- Audio-Datei `data/song.mp3` einlesen und in Base64 umwandeln (um sie direkt im HTML-Snippet zu nutzen, was robuster gegenüber Pfadproblemen in Streamlit ist).

## 2. UI-Komponente (Sidebar)
- In `streamlit_app.py` eine Funktion `inject_background_audio()` implementieren.
- Diese Funktion nutzt `st.components.v1.html`, um ein `<audio>` Element mit `autoplay` und `loop` Attributen einzufügen.
- JavaScript-Snippet hinzufügen:
  ```javascript
  const audio = document.getElementById('bg-audio');
  audio.play().catch(error => {
    // Autoplay blocked: Zeige einen kleinen "Play" Button in der UI
    document.getElementById('play-hint').style.display = 'block';
  });
  ```

## 3. Integration
- Aufruf von `inject_background_audio()` in der Hauptdatei, sobald `st.session_state["authentication_status"]` wahr ist.
- Sicherstellen, dass die Komponente bei jedem Rerun (Seitenwechsel zwischen Dashboard/Rätsel) erhalten bleibt.

## 4. Validierung
- Test mit Chrome/Safari (strenge Autoplay-Regeln).
- Test des Übergangs vom Login zum Dashboard.
