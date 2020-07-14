
def emoji_conv(messages):
    words = messages.split(" ")
    emojis = {
        ":(":"☹",
        ":)":"😁"

    }
    output = ''
    for word in words:
        output += emojis.get(word, word)
    return output


messages = input("> ")

print(emoji_conv(messages))