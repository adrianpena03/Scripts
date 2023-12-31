# Cyphers / encryption algorithms

# Implement a cypher which converts text to something.
# Be able to implement basic cyphers.


# dict = {
#     ":)": "Happy",
#     ":(": "Sad",
#     ":O": "Surprised"
# }

# user_input = input("Look at dictionary, input what you want to receive as output based on input. ")
# sep = user_input.split(' ')

# for word in sep:
#     for key, value in dict.items():
#         if word == key:
#             print(value, end=' ')


# ----------
# Below is more efficient code

dict = {
    ":)": "Happy",
    ":(": "Sad",
    ":O": "Surprised"
}

user_input = input("Look at dictionary, input what you want to receive as output based on input. ")
sep = user_input.split(' ')

output = ''
for word in sep:
    output += dict.get(word, word) + ' '
print(output)
