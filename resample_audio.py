import os
import librosa
import soundfile as sf

# Define the input and output directories
input_dir = '/home/eng/s/sxc220013/Documents/TTS/Datasets/emotions/wavs'
output_dir = '/home/eng/s/sxc220013/Documents/journal1/domain_adaptation_ser/unlabeled_dataset'

# Ensure the output directory exists, create it if not
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set the target sample rate (16 kHz)
target_sample_rate = 16000

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.wav'):  # You can modify the file extension as needed
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)
        
        # Load the audio file
        audio_data, sample_rate = librosa.load(input_file_path, sr=None)  # sr=None to keep original sample rate

        # Resample the audio to 16 kHz
        resampled_audio = librosa.resample(audio_data, orig_sr = sample_rate, target_sr= target_sample_rate)

        # Save the resampled audio to the output directory
        sf.write(output_file_path, resampled_audio, target_sample_rate)

        print(f'Resampled and saved: {filename}')

print('All audio files resampled and saved.')
