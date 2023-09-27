import pandas as pd



# Use pandas to convert CSV to df

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
print(nato_df.to_dict())
# Use comprehension to create dict from df
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)
# Create input to generate list of NATO alphabet from input word
word = input("Enter your word for conversion: ")

nato_list = [nato_dict[char.upper()] for char in word]
print(nato_list)
