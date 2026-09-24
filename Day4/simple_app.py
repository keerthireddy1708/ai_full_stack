import streamlit as st
st.title("welcome to my first app")
st.write("Hello")
st.header("home page....")
st.subheader("about ....")
st.markdown("Hello **keerthi**")
name=st.text_input("Enter your name....")
if st.button("submit"):
    st.write("hello",name)
