import streamlit as st
from main import get_qa_chain

st.title("Chatbot")

# Check if 'chat_history' is already in the session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Create placeholders for the user input and 'Ask' button
user_input_placeholder = st.empty()
button_placeholder = st.empty()

# Display the chat history at the top
for message in st.session_state['chat_history']:
    if "You: " in message:
        st.markdown(f'<p style="color:green;">{message}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p style="color:blue;">{message}</p>', unsafe_allow_html=True)

# Input for user query
user_input = user_input_placeholder.text_input("You: ")

# 'Ask' button for user to submit query
if button_placeholder.button("Ask"):

    chain = get_qa_chain()
    answer = chain(user_input)
    bot_response = answer["result"]

    # Append the user input and bot response to the chat history
    st.session_state['chat_history'].append("You: " + user_input)
    st.session_state['chat_history'].append("Bot: " + bot_response)

    # Rerun the script to update the chat history
    st.experimental_rerun()