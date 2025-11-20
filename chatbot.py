import gradio
from groq import Groq

# Initialize Groq client
client = Groq(
    api_key="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",
)

# Initialize system message list
def initialize_messages():
    return [
        {
            "role": "system",
            "content": """You are a cricket information assistant with strong
            knowledge about cricket rules, players, teams, formats, records,
            match updates, and history. Answer everything in simple and clear English."""
        }
    ]

# Global message list
messages_prmt = initialize_messages()

# Chatbot function
def customLLMBot(user_input, history):
    global messages_prmt

    # Add user message
    messages_prmt.append({"role": "user", "content": user_input})

    # Get response from model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages_prmt
    )

    # Extract assistant response
    LLM_reply = response.choices[0].message.content

    # Add reply to message history
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply


# ----------- GRADIO INTERFACE -----------
iface = gradio.ChatInterface(
    customLLMBot,
    chatbot=gradio.Chatbot(height=300),
    textbox=gradio.Textbox(placeholder="Ask me anything about cricket"),
    title="Cricket Info ChatBot",
    description="Your cricket assistant for rules, players, records, matches & more.",
    theme="soft",
    examples=[
        "Who is the God of cricket?",
        "Explain LBW rule",
        "What is powerplay?",
        "Who won the 2011 World Cup?",
        "What is the difference between ODI and Test cricket?"
    ]
)

iface.launch(share=True)
