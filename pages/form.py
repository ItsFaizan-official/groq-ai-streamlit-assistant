import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Login", page_icon="🔐")

# ---- SESSION STATE INIT ----
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# ---- UI ----
st.title("🔐 Login Page")
st.write("Enter your credentials to access the app")

# ---- LOGIN FORM ----
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    submit = st.form_submit_button("Login")

    if submit:
        # Dummy credentials
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("✅ Login successful!")

            # 🚀 Auto redirect to main app
            st.switch_page("app.py")
        else:
            st.error("❌ Invalid username or password")

# ---- OPTIONAL: Already logged in ----
if st.session_state["logged_in"]:
    st.info("✅ You are already logged in")

    if st.button("➡️ Go to Main App"):
        st.switch_page("app.py")