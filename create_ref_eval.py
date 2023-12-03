# Open a file in write mode ('w' flag)
file_path = '/home/eng/s/sxc220013/Documents/journal1/domain_adaptation_ser/speech-emotion-recognition-with-ladder-network/log/ref_eval_log.txt'

# Open the file for writing
with open(file_path, 'w') as file:
    # Write data line by line
    for i in range(370):
        file.write("0\n")
    for i in range(410):
        file.write("7\n")
    for i in range(360):
        file.write("2\n")
    for i in range(335):
        file.write("1\n")
    

print(f"Data has been written to {file_path}")
