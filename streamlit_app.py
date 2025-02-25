import os
os.environ["MISTRAL_API_KEY"] = "LoXIODO6VkldB64uwva76l1zDpIz6cfu"
print(f"MISTRAL_API_KEY: {os.environ.get('MISTRAL_API_KEY')}")
import streamlit as st
from mistralai import Mistral, UserMessage

# Set page configuration
st.set_page_config(
    page_title="Mistral AI Chat",
    page_icon="🤖",
    layout="wide"
)

# Get API key from environment or Streamlit secrets
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def mistral_query(user_message, model="mistral-large-latest", is_json=False):
    """Function to query the Mistral AI API"""
    client = Mistral(api_key=api_key)
    messages = [
        UserMessage(content=user_message),
    ]
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
    )
    return chat_response.choices[0].message.content

# App title
st.title("Mistral AI Chat")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    
    # Model selection
    model = st.selectbox(
        "Select Model",
        ["mistral-large-latest", "mistral-medium-latest", "mistral-small-latest"]
    )
    
    # API key input (if not set as environment variable)
    if not api_key:
        api_key = st.text_input("Enter your Mistral API Key", type="password")
        if not api_key:
            st.warning("Please enter your Mistral API key to continue")
    
    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("### Examples")
    
    example_prompts = [
        "Explain quantum computing in simple terms",
        "Write a short poem about artificial intelligence",
        "What are the main features of Mistral AI models?",
        "Classify this text: I need to change my PIN for my banking card"
    ]
    
    for prompt in example_prompts:
        if st.button(prompt):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if api_key:
    prompt = st.chat_input("What would you like to ask?")
    
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get response from Mistral
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = mistral_query(prompt, model)
                    st.markdown(response)
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error: {str(e)}")
else:
    st.info("Please enter your Mistral API key in the sidebar to start chatting")

# Add a footer
st.markdown("---")
st.markdown("Built with Streamlit and Mistral AI")