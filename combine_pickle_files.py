import pickle

# List of filenames for the 5 pickle files
pickle_files = ['data/unlabeled/Train/Anger.pk', 'data/unlabeled/Train/Base.pk' ,'data/unlabeled/Train/Happy.pk', 'data/unlabeled/Train/Sad.pk']

# Function to read a pickle file and return the dictionary
def load_pickle(file_name):
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
    return data

# Initialize an empty dictionary to store the combined data
combined_data = {}

# Iterate over each pickle file and concatenate the dictionaries
for file_name in pickle_files:
    data = load_pickle(file_name)
    combined_data.update(data)

# Save the combined dictionary into a new pickle file
output_file = 'all_emotions.pkl'
with open(output_file, 'wb') as file:
    pickle.dump(combined_data, file)

print(f"Combined dictionary saved to {output_file}")
