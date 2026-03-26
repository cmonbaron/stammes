# views/riddle.py
import streamlit as st
from modules.data import STAMMES_DATA
from modules.ui_helper import inject_bruderschaft_style

def show_riddle():
    inject_bruderschaft_style()
    e = next(x for x in STAMMES_DATA if x['id'] == st.session_state.current_event)
    
    if st.button("← Zurück zum Zirkel"):
        del st.session_state.current_event
        st.rerun()
        
    st.title(e['titel'])
    st.markdown(f"<p style='text-align: center; color: #d4af37;'>{e['hinweis']}</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="riddle-box">', unsafe_allow_html=True)
        if e['typ'] == 'rebus':
            st.markdown(f'<div class="rebus-icons">{e["icons"]}</div>', unsafe_allow_html=True)
        elif e['typ'] == 'cipher':
            st.markdown(f'<div class="cipher-text">{e["cipher_display"]}</div>', unsafe_allow_html=True)
        elif e['typ'] == 'grid':
            # Dynamisches Gitter generieren
            grid_data = e.get('grid', [])
            if grid_data:
                rows = len(grid_data)
                cols = len(grid_data[0]) if rows > 0 else 0
                
                html = '<table class="grid-table">'
                # Header
                html += '<tr><td></td>' + ''.join([f'<td>{i+1}</td>' for i in range(cols)]) + '</tr>'
                # Rows
                for r in range(rows):
                    html += f'<tr><td>{r+1}</td>'
                    for c in range(cols):
                        html += f'<td>{grid_data[r][c]}</td>'
                    html += '</tr>'
                html += '</table>'
                st.markdown(html, unsafe_allow_html=True)
            st.markdown(f'<p style="margin-top: 15px; font-weight: bold; letter-spacing: 2px;">{e["coords"]}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    solved_key = f"solved_{e['id']}"
    if solved_key not in st.session_state: st.session_state[solved_key] = False
        
    if not st.session_state[solved_key]:
        ans = st.text_input("Das Lösungswort", key="ans_input").lower().strip()
        if st.button("Das Siegel lösen"):
            if ans == e['loesung']:
                st.session_state[solved_key] = True
                st.rerun()
            else: st.error("Die Mächte schweigen.")
    else:
        st.markdown(f"""
            <div style="background: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; padding: 20px; border-radius: 12px; text-align: center; margin-top: 20px;">
                <h2 style="margin:0; font-size: 1.5rem;">OFFENBARUNG</h2>
                <p style="font-size: 1.1rem; color: #d4af37; margin-top: 10px;">{e['ergebnis']}</p>
            </div>
        """, unsafe_allow_html=True)
