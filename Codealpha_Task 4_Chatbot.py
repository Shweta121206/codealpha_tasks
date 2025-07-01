def chatbot():
    flag = 0
    print("\n~~~WELCOME TO THE CHATBOT~~~\n")
    responses = {"hi":"Hello!", "how are you":"Thank you. I am fine.", "hello":"Hi!",
                 "what is python":"Python is a high-level programming language",
                 "write a comment in python":"Use the # symbol before your comment. "
                                             "\n\t\tExample: # This is a comment.",
                 "function to print something in python": "Use the print() function. "
                                                          "\n\t\tExample: print(\"Hello, world!\")"}

    while flag != 1:
        user = input("You: ")
        if user.lower() in responses:
            print("Chatbot:", responses[user.lower()])
        else:
            if user.lower() == "bye":
                print("Chatbot: Goodbye.")
                flag = 1
            else:
                print("Chatbot: Sorry, I did not understand the question. ")

chatbot()