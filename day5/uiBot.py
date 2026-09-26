import ollama
import streamlit as st
if "messages" not in st.session_state:
    st.session_state.messages= []
for msg in st.session_state.messages:
    if msg["role"]=="user":
        with st.chat_message("user"):
            st.write("user:",msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write("AI:",msg["content"])

    
question=st.chat_input("you:")
if question:
    with st.chat_message("user"):
        st.write("user:",question)
    st.session_state.messages.append(
    
        {
            "role":"user",
            "content": question
        }
    )
with st.spinner("Thinking...."):
    response = ollama.chat(
        model="llama3.2:3b",
        messages=st.session_state.messages
        
        )
st.session_state.messages.append(
    {    "role":"assistant",
        "content":response["message"]["content"]}
    )
with st.chat_message("Assistant"):

    st.write("AI:",response["message"]["content"])

with st.sidebar:
    uploaded_file=st.file_uploader("upload the file...")
    if uploaded_file is not None:
        st.write("file name:",uploaded_file.name)
        st.write("file is uploaded successfully")
        context=uploaded_file.read().decode("utf-8")
        st.text(context)
    else:
        st.write("please upload the file")


