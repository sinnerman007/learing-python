input_ = input("> ")
words = input_.split(" ")
emojis = {
    ":(" :"☹",
    ":)":"😁"

}
output = ''
for word in words:
    output += emojis.get(word, word)

print(output)