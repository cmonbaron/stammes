import streamlit_authenticator as stauth

passwords = ['bruder2026'] * 9
hashed_passwords = stauth.Hasher(passwords).generate()

usernames = ["timo", "constantin", "carsten", "marcel", "marco", "christof", "luca", "paddi", "simon"]

for u, h in zip(usernames, hashed_passwords):
    print(f"{u} = \"{h}\"")
