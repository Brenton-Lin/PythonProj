import pandas as pd

data = pd.read_csv("50_states.csv")

all_states = data.state.to_list()


guessed_states = ["Florida", "Kansas", "Maine", "Georgia"]

missed_states = [state for state in all_states if state not in guessed_states]

print(missed_states)