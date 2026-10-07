import streamlit as st
from ai_bot import ask_ai

st.set_page_config(
    page_title="XXX Solar Assistant",
    page_icon="☀️"
)

st.title("☀️ XXX Solar Company Assistant")

customer_id = st.text_input("Customer WhatsApp Number")

# Reset chat when customer changes
if "last_customer" not in st.session_state:
    st.session_state.last_customer = customer_id

if customer_id != st.session_state.last_customer:
    st.session_state.messages = []
    st.session_state.last_customer = customer_id

if customer_id:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show chat history
    for chat in st.session_state.messages:
        with st.chat_message(chat["role"]):
            st.write(chat["text"])

    user_message = st.chat_input("Type your message...")

    if user_message:

        # Store user message
        st.session_state.messages.append({
            "role": "user",
            "text": user_message
        })

        with st.chat_message("user"):
            st.write(user_message)

        # Get AI reply
        reply = ask_ai(customer_id, user_message)

        # Store assistant reply
        st.session_state.messages.append({
            "role": "assistant",
            "text": reply
        })

        with st.chat_message("assistant"):
            st.write(reply)