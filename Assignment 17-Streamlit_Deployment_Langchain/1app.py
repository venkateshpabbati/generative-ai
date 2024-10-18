# Import the required libraries
import openai
import streamlit as st

# Function to generate a response from OpenAI's GPT model (new API structure)
def generate_response(prompt):
    # Initialize the OpenAI client and pass the API key directly
    client = openai.OpenAI(api_key="OPEN_API_KEY")  # Replace with your actual API key
    completion = client.chat.completions.create(
        model="gpt-4",  # Use the model you want (e.g., 'gpt-4' or 'gpt-4o')
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # Properly access the message content without subscripting
    return completion.choices[0].message.content

# Streamlit UI
st.title("OpenAI LLM Chatbot")

# Input text box
user_input = st.text_input("You:", "")

# Button to submit query
if st.button("Send"):
    if user_input:
        # Generate response using OpenAI API
        response = generate_response(user_input)
        # Display the response
        st.text_area("Assistant:", value=response, height=300)
    else:
        st.warning("Please enter a message.")