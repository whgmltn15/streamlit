import streamlit as st

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.write("write")

if st.button("Click Button"):
    st.write("Hello")

# check box
checkbox_btn = st.checkbox("Checkbox button")
if checkbox_btn:
    st.write("Good")

# if you want to difault value = True
checkbox_btn2 = st.checkbox("Checkbox button2", value=True)
if checkbox_btn2:
    st.write("hello")

# Radio Buttton
selected_item = st.radio("Radio Button", ("hi", "hello", "bye"))
if selected_item == "hi":
    st.write("HI")
elif selected_item == "hello":
    st.write("HELLO")
elif selected_item == "bye":
    st.write("BYE")

