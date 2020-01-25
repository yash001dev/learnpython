#Emoji Converter Using Dictonary
message=input(">")
words=message.split(' ')
emojis={
    ":)":"Happy",
    ":(":"Sad"
}
output=""
for word in words:
    output+=emojis.get(word,word)+" "
print(output)

