import pandas as pd
import openpyxl
from fuzzywuzzy import fuzz

list = []
df = pd.read_csv("DSA Bootcamp Feedback Form.csv") 

print(df.columns)

name_column = df['Name '].to_list() 

print(name_column)

df = pd.read_excel('meetingAttendanceList (1).xlsx')
unique_values = set(df['The data could be incomplete due to the large number of meeting participants.'])
print(unique_values)

result_list = []

for value in unique_values:
   
    if not isinstance(value, float) and "mri" not in value:
        result_list.append(value)

print(result_list)



similar_pairs = []
for name1 in unique_values:
    for name2 in result_list:
        similarity = fuzz.token_sort_ratio(name1, name2)
        if similarity >= threshold:
            similar_pairs.append((name1, name2, similarity))

# Print the similar pairs
for pair in similar_pairs:
    print(f"Similar Pair: {pair[0]} and {pair[1]} with similarity {pair[2]}%")
