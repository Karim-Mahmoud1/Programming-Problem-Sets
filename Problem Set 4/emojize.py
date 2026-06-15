import emoji

user_input = input("Input: ")

emojized_text = emoji.emojize(user_input, language='alias')

print(f"Output: {emojized_text}")