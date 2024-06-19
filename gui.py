import tkinter as tk
import csv
import pandas as pd
import pickle
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Entry Form")
        
        tk.Label.config(self.master,bg= "white")
        # create label for each field
        tk.Label(self.master, text="Username : ").grid(row=0)
        tk.Label(self.master, text="Does user have profile pic? :").grid(row=1)
        tk.Label(self.master, text="Name of account :").grid(row=2)
        tk.Label(self.master, text="Bio Lenght : ").grid(row=3)
        tk.Label(self.master, text="External URL?: ").grid(row=4)
        tk.Label(self.master, text="Is the account private? :").grid(row=5)
        tk.Label(self.master, text="Number of posts : ").grid(row=6)
        tk.Label(self.master, text="Number of followers :").grid(row=7)
        tk.Label(self.master, text="Number of following :").grid(row=8)


        # create entry widget for each field
        self.e1 = tk.Entry(self.master)
        self.e2 = tk.Entry(self.master)
        self.e3 = tk.Entry(self.master)
        self.e4 = tk.Entry(self.master)
        self.e5 = tk.Entry(self.master)
        self.e6 = tk.Entry(self.master)
        self.e7 = tk.Entry(self.master)
        self.e8 = tk.Entry(self.master)
        self.e9 = tk.Entry(self.master)

        # arrange entry widgets
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.e8.grid(row=7, column=1)
        self.e9.grid(row=8, column=1)

        # create button to save data
        self.submit_button = tk.Button(self.master, text="Save", command=self.save_data)
        self.submit_button.grid(row=9, column=0, columnspan=2)


    def save_data(self):
        if (self.e2.get() == 'Y' or self.e2.get() == 'y'):
            profile = 1
        else:
            profile = 0
        
        username = self.e1.get()

        num_count = sum(c.isdigit() for c in username)
        length = len(username)

        ratio = num_count / length
        fullname = self.e3.get()
        words = fullname.split()
        word_count = len(words)
        f_num_count = sum(c.isdigit() for c in fullname)
        f_length = len(fullname)
        f_ratio = f_num_count / f_length


        if(self.e6.get() == "Y"):
            priv = 1
        else:
            priv = 0


        if(self.e5.get() == "Y"):
            ext = 1
        else:
            ext = 0
        if (username == fullname):
            unf = 1
        else:
            unf = 0
        # get data from entry widgets
        data = [self.e1.get(), profile, ratio, word_count, f_ratio, unf, self.e4.get(),ext, priv, self.e7.get(), self.e8.get(), self.e9.get()]

        # write data to CSV file
        with open('instagram_test.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)

        # clear entry widgets
        self.e1.delete(0, tk.END)
        self.e2.delete(0, tk.END)
        self.e3.delete(0, tk.END)
        self.e4.delete(0, tk.END)
        self.e5.delete(0, tk.END)
        self.e6.delete(0, tk.END)
        self.e7.delete(0, tk.END)
        self.e8.delete(0, tk.END)
        self.e9.delete(0, tk.END)
    
    
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.geometry("800x800")
    root.configure(bg='white')
    root.mainloop()
