import pandas as pd

# Input first file
contact_df = pd.read_csv('respondent_contact.csv')
# Input second file
other_df = pd.read_csv('respondent_other.csv')

# Merge the two dataframes based on the ID column
merged_df = pd.merge(contact_df, other_df, left_on = 'respondent_id', right_on = 'id')
# Delete id column to avoid redundancy
merged_df = merged_df.drop('id', axis = 1)

# Drop any rows with missing values
merged_df = merged_df.dropna()

# Drop rows with 'job' value containing 'insurance' or 'Insurance'
merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

# Print the shape of the output file
print("Output file shape:", merged_df.shape)

# Save the modified data to a new CSV file
merged_df.to_csv('clean_data.csv', index=False)