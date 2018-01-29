
while True:

    text = input("What is your question?")


    if text.endswith("?"):
	    print("Yes, this is a question.")

    elif text == "quit":
	    break

    else:
	    print("I’m sorry, I can only answer questions.")


