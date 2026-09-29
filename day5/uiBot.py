import ollama
import streamlit as st
st.title(":violet[ 🔍My ChatBot!!!]")
with st.sidebar:
    personalities ={
        "🧒Kid": "Give the answers like you are explaining to a 5-year old kid. Give the answer in 2 lines only.",
        "🧑‍🏫Professor": "You are an IIT professor .Explain the topics using terminology.Give the answer in 2-3 lines only. ",
        "🧑‍🏫Student":"think you are an average student.explain the topics in detail .give the answer in 3-4 lines only."
    }
    personality=st.selectbox("select a personality", personalities.keys())
    if st.button("Clear Chat 🚮  "):
        st.session_state.messages=[]
        st.success("Chat cleared successfully")

    st.header("Chat Settings ⚙️")
    uploaded_file=st.file_uploader("upload the file...")
    try:
        if uploaded_file is not None:
            st.write("file name:",uploaded_file.name)
            st.write("file is uploaded successfully")
            if st.button("display"):
                with st.expander("preview"):
                    context=uploaded_file.read().decode("utf-8")
                    st.text(context)
    except:
        st.error("file type not supported")



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
            messages=[{
                "role": "system","content":personalities[personality]

            }]+st.session_state.messages
            
            )
    st.session_state.messages.append(
        {    "role":"assistant",
            "content":response["message"]["content"]}
        )
    with st.chat_message("Assistant"):

        st.write("AI:",response["message"]["content"])

