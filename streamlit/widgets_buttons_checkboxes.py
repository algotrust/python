import streamlit as st

# buttons
name = 'Billy'
counter = 0
if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = 1 #st.number_input('Enter a value', value=0, step=1)

def increment_counter(increment_value):
    st.session_state.count += increment_value

if st.button("Submit"):
    st.write(f"My name is : {name.upper()}")

if st.button("Submit", key='new02'):
    st.write(f"My name is : {name.lower()}")

increment = st.button('Increment', on_click=increment_counter,
    args=(increment_value, ))
st.write('Count = ', st.session_state.count)

# radio buttons
status = st.radio("What is your status?", ("Active", "Inactive"))

if status == "Active":
    st.success("Good! You are active!")
else:
    st.warning("Go out and move!!")

# checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing something")

# beta expander
if st.expander("Python"):
    st.success("Hello Python")