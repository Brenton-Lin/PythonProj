




# python open

with open("Save.txt") as file:
    contents = file.read()
    print(contents)


# Manually closing files opens your program up to human management errors

with open("Save.txt", mode="a+") as file:

    file.write("Testudo")
    contents = file.read()
    print(contents)

#With keyword instead