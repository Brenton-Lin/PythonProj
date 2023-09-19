# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt") as default_body:
    message_body = default_body.read()

print(message_body)

with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        stripped = name.strip()
        new_letter_body = message_body.replace("[name]", stripped)
        # we needed the stripped version, the names have a new line char in them to start
        # the newline char causes invalid input errors in the open method.
        with open(f"./Output/ReadyToSend/{stripped}.txt", "w") as new:
            new.write(new_letter_body)
