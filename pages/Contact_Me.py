import streamlit as st
from send_email import send_email, valid_email

st.header("Contact Me")

with st.form(key="contact_me"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Submit")

    if submit:
        if name and email and message:
            if valid_email(email):
                try:
                    send_email(name, email, message)
                    st.write("Thank you for contacting me! I will get back to you as soon as possible.")
                except:
                    st.write("An error occurred while sending your message. Please try again later.")
            else:
                st.write("Please enter a valid email address.")
        else:
            st.write("Please fill out all fields.")
