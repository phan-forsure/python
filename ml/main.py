from transformers import pipeline, set_seed

# Load GPT-2 text-generation pipeline
chatbot = pipeline("text-generation", model="gpt2")
set_seed(42)

# Conversation history to provide context
conversation = ""

print("Smarter GPT-2 Chatbot (type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    # Add the new user message to the conversation
    conversation += f"User: {user_input}\nBot:"

    # Generate a reply using GPT-2
    response = chatbot(conversation, max_length=len(conversation.split()) + 50, num_return_sequences=1, pad_token_id=50256)
    
    # Extract the bot's reply
    full_reply = response[0]['generated_text']
    bot_reply = full_reply[len(conversation):].split("\n")[0].strip()

    # Show the reply
    print("Bot:", bot_reply)

    # Append bot's reply to the conversation
    conversation += f" {bot_reply}\n"
