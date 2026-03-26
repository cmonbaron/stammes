# modules/ui_helper.py
import streamlit as st
import os
import base64

def load_css(file_path):
    """Liest eine CSS-Datei ein und injiziert sie."""
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def inject_login_style():
    load_css("styles/login.css")

def inject_bruderschaft_style():
    load_css("styles/bruderschaft.css")

def inject_background_audio(audio_path):
    """Injiziert ein verstecktes Audio-Element mit Autoplay-Versuch und manuellem Fallback."""
    if not os.path.exists(audio_path):
        st.error(f"Audio-Datei nicht gefunden: {audio_path}")
        return

    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    
    audio_base64 = base64.b64encode(audio_bytes).decode()
    
    # HTML5 Audio Snippet
    # - Autoplay + Loop
    # - JavaScript versucht Play()
    # - Falls Play() fehlschlägt (Browser-Block), wird ein Button in der Sidebar angezeigt
    audio_html = f"""
        <audio id="bg-audio" loop autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        
        <script>
            const audio = document.getElementById('bg-audio');
            audio.volume = 0.5;
            
            // Versuch Autoplay
            const playPromise = audio.play();
            
            if (playPromise !== undefined) {{
                playPromise.catch(error => {{
                    // Autoplay wurde vom Browser blockiert
                    console.log("Autoplay blockiert. Warte auf Benutzerinteraktion.");
                    // Wir informieren Streamlit über den Zustand (optional via Hidden Component)
                    // Hier nutzen wir primär den manuellen Play-Button in der Sidebar
                }});
            }}
        </script>
    """
    
    # In der Sidebar platzieren wir einen manuellen Button als Fallback/Control
    with st.sidebar:
        st.markdown("---")
        st.write("🎵 **Ambiente**")
        col1, col2 = st.columns([1, 3])
        if col1.button("▶️", help="Musik manuell starten"):
            st.components.v1.html(f"""
                <script>
                    window.parent.document.getElementById('bg-audio').play();
                </script>
            """, height=0)
        if col2.button("⏸️", help="Musik pausieren"):
            st.components.v1.html(f"""
                <script>
                    window.parent.document.getElementById('bg-audio').pause();
                </script>
            """, height=0)
            
    # Das eigentliche Audio-Tag (unsichtbar)
    st.components.v1.html(audio_html, height=0)
