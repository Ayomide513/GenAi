import streamlit as st
from utils import response_generator, make_prompt,support_function





st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        model_response = make_prompt(user_prompt=prompt)
        model_response = support_function(user_prompt=model_response)
        response = st.write_stream(response_generator(response=model_response))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})