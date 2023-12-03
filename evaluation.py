from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file and convert each line to a float
            numbers = [float(line.strip()) for line in file.readlines()]
        return numbers
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    

ref_file_path = 'log/ref_eval_log.txt'
prediction_file_path = 'log/eval_log_3_recon_5_SER.txt' 
# Initialize an empty array to store the numbers
true_label =  read_numbers_from_file(ref_file_path)
predictions = read_numbers_from_file(prediction_file_path)

report = classification_report(true_label, predictions)
print(report)
# df = pd.DataFrame(report).transpose()
# print(df)
# confusion_matrix = metrics.confusion_matrix(true_label, predictions)

# cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix,display_labels = ["Angry", "Sad" ,"Happy","Neutral"])

# cm_display.plot()
# plt.show()
conf_matrix = confusion_matrix(true_label, predictions)
cm_normalized = conf_matrix.astype('float') / conf_matrix.sum(axis=1)[:, np.newaxis]
# Create a heatmap using Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(cm_normalized, annot=True, cmap='Blues', cbar=False,
            xticklabels=["Angry", "Sad" ,"Happy","Neutral"],
            yticklabels=["Angry", "Sad" ,"Happy","Neutral"], vmin=0, vmax=0.6)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()