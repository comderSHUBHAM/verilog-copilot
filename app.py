import streamlit as st
import openai

# --- OpenAI API key input (always at the top) ---
api_key = st.text_input("Enter your OpenAI API key", type="password")
if not api_key:
    st.warning("Enter your OpenAI API key to use this app.")
    st.stop()

client = openai.OpenAI(api_key=api_key)

st.title("💬 ChatGPT for Verilog Code")
st.write("Paste Verilog code or ask a question (explain code, find errors, predict next lines).")

# Maintain conversation history for the session
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are an expert in Verilog. Answer questions, explain code, suggest corrections and predict next lines when asked."}
    ]

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# Chat input at the bottom
prompt = st.chat_input("Type your question or paste Verilog code here...")

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # OpenAI chat completion (latest API call format)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4o" if you have access
            messages=st.session_state["messages"],
            temperature=0.3,
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"Error from OpenAI API: {e}"

    st.session_state["messages"].append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
