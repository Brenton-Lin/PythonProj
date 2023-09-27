import random
import pandas as pd
# General List comprension format:

# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

print(new_list)

# Python sequences have an order:
# tuples, strings, lists, ranges


doubled_list = [num * 2 for num in range(1, 5)]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
# print(short_names)

big_names = [name.upper() for name in names if len(name) > 4]
# print(big_names)

# Dictionary Comprenhension

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {name: random.randint(50, 100) for (name) in names}

print(student_scores)
# Example
passed_student = {name: "passed" for (name,score) in student_scores.items() if score > 80}

print(passed_student)

student_dict = {
    "student" : ["Yob", "Blob", "Job"],
    "score" : [56, 76, 98]
}
# Iterating through a pandas Dataframe:

# Create dataframe from dict
passed_data_frame = pd.DataFrame(student_dict)

for (index,row) in passed_data_frame.iterrows():
    if row.student == "Yob":
        print(row.score)
