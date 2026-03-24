# 🤖 KI-Kontext: Heilige Bruderschaft

Dieses Dokument ist der Einstiegspunkt für KI-Assistenten. Das Projekt folgt dem **Spec-Driven Development (SDD)** Ansatz.

## 📁 Projektstruktur & Specs
Der gesamte Funktionsumfang, die Architektur und der aktuelle Fortschritt sind im Ordner `.specs/` dokumentiert:

- **`.specs/features/01_authentication/`**: Login-System, PINs und QR-Codes.
- **`.specs/features/02_dashboard/`**: Event-Übersicht und Navigation.
- **`.specs/features/03_riddles/`**: Rätsel-Logik und Belohnungssystem.

## ⚙️ Workflow (SDD)
Für jede Änderung (Feature oder Bugfix) folgen wir diesem Prozess:
1. **Requirements** definieren (`01_requirements.md`).
2. **Spec** technisch präzisieren (`02_spec.md`).
3. **Plan** für die Umsetzung erstellen (`03_plan.md`).
4. **Tasks** Schritt für Schritt abarbeiten (`04_tasks.md`).

## 🔑 Wichtige Projekt-Anker
- **Entry Point:** `streamlit_app.py`.
- **Daten:** `modules/data.py` (Zentrale Liste `STAMMES_DATA`).
- **Styling:** `styles/` (Bruderschaft-Design mit Gold-Akzenten).
- **Session States:** `authentication_status`, `current_event`, `solved_<id>`.
