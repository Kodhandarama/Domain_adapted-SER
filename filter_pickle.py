import pickle

def filter_and_save_pickle(input_pickle_file, output_pickle_file,emotion):
    # Load the dictionary from the input pickle file
    with open(input_pickle_file, 'rb') as f:
        original_dict = pickle.load(f)

    # Filter out key-value pairs where the key contains the word "Happy"
    filtered_dict = {key: value for key, value in original_dict.items() if emotion in key}

    # Save the filtered dictionary to a new pickle file
    with open(output_pickle_file, 'wb') as f:
        pickle.dump(filtered_dict, f)

# Example usage
input_file_path = 'data/unlabeled/Train/feats.pk'
output_file_path = 'data/unlabeled/Train/Calm.pk'
emotion = "Calm"
filter_and_save_pickle(input_file_path, output_file_path,emotion)
