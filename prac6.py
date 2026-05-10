# Simple Customer Support Chatbot

print("===== Welcome to Customer Support Chatbot =====")

print("Type 'bye' to exit\n")

while True:

    # Take user input
    user = input("You: ").lower()

    # Greeting
    if user in ["hello", "hi", "hey"]:

        print("Bot: Hello! How can I help you?")

    # Product inquiry
    elif "product" in user:

        print("Bot: We provide laptops, mobiles, and accessories.")

    # Price inquiry
    elif "price" in user:

        print("Bot: Prices depend on the product model.")

    # Working hours
    elif "hours" in user or "time" in user:

        print("Bot: Our shop is open from 9 AM to 9 PM.")

    # Contact information
    elif "contact" in user:

        print("Bot: You can contact us at support@gmail.com")

    # Thank you message
    elif "thank" in user:

        print("Bot: You're welcome!")

    # Exit condition
    elif user == "bye":

        print("Bot: Thank you for visiting!")
        break

    # Unknown query
    else:

        print("Bot: Sorry, I didn't understand that.")