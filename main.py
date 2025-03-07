import streamlit as st #importing streamlit library
import random #importing random library
import string #importing string library


# Function to generate password
def generate_password(Length, use_digits, use_special):
    characters = string.ascii_letters #includes all letters (a-z)(A-Z)

    if use_digits:
        characters += string.digits #adds numbers (0-9) to the password if selected

    if use_special:
        characters += string.punctuation #adds special characters (!,@,#,$,%,^,&,*)

    # Generates a random password of the specified length using the characters defined above
    return ''.join(random.choice(characters)for _ in range(Length))

# Title of the app
st.title("SecurePassGen")

# Input for the length of the password
length = st.slider("Select the length of the password", min_value=8, max_value=32, value=12)

#Chexkbox for digits
use_digits = st.checkbox("Include Digits")

#Checkbox for special characters
use_special = st.checkbox("Include Special Characters")

#Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password:`{password}`")


#Footer
st.write("--------------------------------")
st.write("🔒 Securely generated by PassGenie | Made by [Laiba Ashfaq](https://github.com/laibaashfaq1)")