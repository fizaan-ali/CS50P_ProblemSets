import emoji

line = input("Input: ")

emoji_line = emoji.emojize(line, language='alias')

print("Output:", emoji_line)
