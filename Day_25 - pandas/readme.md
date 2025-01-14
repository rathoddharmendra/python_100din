#  if __next__ is overwritten in a class, I can run loop as it converts object into iterable

# working with csv
- using default file object readlines() method
- using csv module -- faff 🫤
- using pandas module

# pandas work well with tabular data

# using square functions with pandas dataframe

`
if [column_name], returns entire column as Series object
if [condition for data column == some_value], returns only the row with the condition
`


# passing true / false series to dataframe to map out another dataframe
print(~self.states_data.state.isin(self.guessed_states))
print(type(~self.states_data.state.isin(self.guessed_states)))
unguessed_states = self.states_data[~self.states_data.state.isin(self.guessed_states)]
