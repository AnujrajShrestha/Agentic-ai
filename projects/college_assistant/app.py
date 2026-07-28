import streamlit as st
from agentic import app

st.set_page_config(
    page_title="College Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------
# Session State
# ---------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "programme" not in st.session_state:
    st.session_state.programme = "BCA"

# ---------------------------
# Sidebar
# ---------------------------

with st.sidebar:

    st.title("🎓 College Assistant")

    st.markdown("---")

    programme = st.selectbox(
        "Select Your Programme",
        ["BCA", "BBA", "B.Com (H)"],
        index=["BCA", "BBA", "B.Com (H)"].index(
            st.session_state.programme
        )
    )

    st.session_state.programme = programme

    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.info(
        """
This assistant can answer questions about:

- 📘 Academic Rules
- 💰 Fee Structure
- 🎓 College Policies
- 🤖 General Queries
"""
    )

# ---------------------------
# Header
# ---------------------------

st.title("🎓 AI College Assistant")

st.caption(
    f"Currently assisting **{st.session_state.programme}** students."
)

# ---------------------------
# Display Chat
# ---------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# User Input
# ---------------------------

prompt = st.chat_input("Ask anything about your college...")

if prompt:

    # Show User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = app.invoke(
                {
                    "programme": st.session_state.programme,
                    "messages": [("user", prompt)]
                }
            )

            response = result["messages"][-1].content

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )