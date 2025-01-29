
userInput = input(">")

def emoji_converter(message):
    message = message.split(" ")

    emojis = {
        ":)": "😁",
        ":(": "☹️",
        "T_T": "😭"
    }

    output = ''

    for word in message:
        output += emojis.get(word, word) + " "

    print(output)


emoji_converter(userInput)