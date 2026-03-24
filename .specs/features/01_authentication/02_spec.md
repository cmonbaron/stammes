# Spec: Authentifizierung
- **Authentifizierung:** `streamlit-authenticator` (v0.4.x).
- **Datenquelle:** `.streamlit/secrets.toml`.
- **Hashes:** bcrypt (12 rounds).
- **Cookie-Parameter:**
    - `name`: bruderschaft_cookie
    - `expiry_days`: 30
- **User-PINS:** Individuell (4-stellig), in `zugangsdaten.md` referenziert.
