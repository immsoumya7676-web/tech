import streamlit as st
from openai import OpenAI

# Set up the title of your web app
st.title("🤖 My First AI Prototype")

# Get your OpenAI API key from the user securely
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# Input field for the user's prompt
user_prompt = st.text_input("Ask the AI something:")

# When the button is clicked, send the request to OpenAI
if st.button("Generate Response"):
    if not api_key:
        st.warning("Please enter your OpenAI API key first.")
    elif not user_prompt:
        st.warning("Please type a prompt.")
    else:
        try:
            # Initialize the OpenAI client
            client = OpenAI(api_key=api_key)
            
            # Call the OpenAI API
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini", # Standard fast model
                    messages=[{"role": "user", "content": user_prompt}]
                )
            
            # Display the result
            st.success("Response:")
            st.write(response.choices[0].message.content)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
