
import streamlit as st
from agent import get_ai_response
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Page configuration
st.set_page_config(
    page_title="AI Agent Web Interface",
    page_icon="🤖",
    layout="centered"
)

# App title
st.title("🤖 My Custom AI Agent")
st.write("Ask your AI agent anything below!")

# Initialize chat historypython 
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your message here..."):

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare chat history
    chat_history = [
        SystemMessage(
            content="You are a helpful, smart, and concise AI assistant."
        )
    ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_history.append(
                HumanMessage(content=msg["content"])
            )
        else:
            chat_history.append(
                AIMessage(content=msg["content"])
            )

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(chat_history)

        st.markdown(ai_response)

    # Save AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )
