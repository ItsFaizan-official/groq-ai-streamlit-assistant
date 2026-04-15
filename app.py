import os
import streamlit as st
from langchain_groq import ChatGroq

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Groq AI Assistant", page_icon="🤖")

# ---- SESSION STATE ----
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================================
# 🔐 LOGIN SCREEN (FIRST LANDING PAGE)
# =========================================================
if not st.session_state.logged_in:

    st.title("🔐 Login")
    st.write("Please login to continue")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submit = st.form_submit_button("Login")

        if submit:
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

    st.stop()

# =========================================================
# 🤖 MAIN APP (AFTER LOGIN)
# =========================================================

st.title("🤖 Groq AI Assistant")
st.write("Ask anything about Python, Data Science, or AI")

# ---- SIDEBAR (ONLY AFTER LOGIN) ----
st.sidebar.header("⚙️ Settings")

# Logout
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

api_key = st.sidebar.text_input("Enter GROQ API Key", type="password")

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.0)

model = st.sidebar.selectbox(
    "Select Model",
    ["llama-3.3-70b-versatile"]
)

# ---- USER INPUT ----
user_input = st.text_area("💬 Your Question:")

# ---- GENERATE RESPONSE ----
if st.button("Generate Response"):

    if not api_key:
        st.warning("⚠️ Please enter your GROQ API key")
    elif not user_input:
        st.warning("⚠️ Please enter a question")
    else:
        try:
            os.environ["GROQ_API_KEY"] = api_key

            groq_chat = ChatGroq(
                model=model,
                temperature=temperature
            )

            with st.spinner("Generating response..."):
                response = groq_chat.invoke(user_input)

            st.success("✅ Response:")
            st.write(response.content)

        except Exception as e:
            st.error(f"Error: {str(e)}")