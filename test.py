import pandas as pd
import pickle
import tkinter as tk
import csv
import tksheet

# Load the saved Logistic Regression model
filename = 'lr_model.pkl'
with open(filename, 'rb') as file:
    lr = pickle.load(file)

# Load the test data
test_data = pd.read_csv('instagram_test.csv')

# Preprocess the test data to exclude the 'username' column
X_test = test_data.iloc[:, 1:].values

# Save the usernames for output
usernames = test_data.iloc[:, 0]
fields = ['Username', 'Sample No', 'Fake?'] 
f = "data.csv"

# Use the loaded model to make predictions on the test data
y_pred = lr.predict(X_test)
data = [[]]
# Display the predictions
with open(f, 'w',newline='') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    pred = "Yes"
    print("Predictions:")
    for i in range(len(y_pred)):
        print("Username: {}, Sample {}: {}".format(usernames[i], i+1, y_pred[i]))
        if y_pred[i] == 1:
            pred = "Yes"
        else:
            pred = "No"
        data.append([usernames[i],i+1,pred])
    csvwriter.writerows(data)


top = tk.Tk()
top.geometry("600x600")
sheet = tksheet.Sheet(top,width = 600,height= 600)

sheet.grid()

sheet.set_sheet_data(data,reset_col_positions = True,
               reset_row_positions = True,
               redraw = True,
               verify = False,
               reset_highlights = False)

# table enable choices listed below:

sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))

top.mainloop()
 