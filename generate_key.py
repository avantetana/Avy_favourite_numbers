import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Avyattana", "Stefano Guanziroli"]
usernames = ["avy27", "stef_g"]
passwords = ['avy27', 'stef_g']
hashed_passwords = stauth.Hasher(passwords).generate()
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

#----USER AUTHENTICATION
# names = ["Avyattana", "Stefano Guanziroli"]
# usernames = ["avy27", "stef_g"]
#
# #-- Load the passwords
# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)
#
# authenticator = stauth.Authenticate(names, usernames, hashed_passwords)
# name, authentication_status, username = authenticator.login("Login", 'main')
#
# if authentication_status == False:
#     st.error("Username/password is incorrect")
# if authentication_status == None:
#     st.warning("Please enter your username and password")
# if authentication_status:
