import random

while True:
    text = input("What is your question? ")
    if text.endswith("?"):
        ans = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
        "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
        "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
        "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
        "Don't count on it", "My reply is no", "My sources say no",
        "Outlook not so good", "Very doubtful"]
        print(ans[random.randrange(20)])

    elif text == "quit":
        break

    else:
        print("I’m sorry, I can only answer questions.")
