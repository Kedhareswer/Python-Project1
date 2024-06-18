import requests  # library for making HTTP requests
import json  # library for working with JSON data
from tkinter import *  # GUI toolkit
from tkinter import messagebox as mb  # module for displaying message boxes

# Create the root window for the GUI
root = Tk()
root.geometry("800x500")  # Set the size of the window
root.title("Quiz")  # Set the title of the window

# URL of the JSON data for the quiz
url = 'https://drive.google.com/uc?id=1HJoH7ZgxbbbTWHJLWJHcjxPICXHocVM4&export=download'

# Fetch the JSON data using requests library
response = requests.get(url)
data = response.content

# Parse the JSON data
obj = json.loads(data.decode('utf-8'))  # decode the JSON data into a Python object
q = obj['ques'] 
options = obj['options']
a = obj['ans']


class Quiz:
    def __init__(self):
        # Initialize the quiz with the first question
        self.qn = 0  
        self.ques = self.question(self.qn)  
        self.opt_selected = IntVar()  
        self.opts = self.radiobtns()  
        self.display_options(self.qn)  
        self.buttons()  
        self.correct = 0  

    def question(self, qn):
        # Create a label widget to display the current question
        t = Label(root, text="Kedhareswer's Quiz in Python Programming", width=50, bg="blue", fg="white",
                  font=("times", 20, "bold"))  # title label
        t.place(x=0, y=2)  
        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")  # label for the current question
        qn.place(x=70, y=100)  
        return qn

    def radiobtns(self):
        # Create a list of Radiobutton widgets for displaying the answer options
        val = 0  
        b = []  
        yp = 150  
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))  # create a Radiobutton widget
            b.append(btn)  
            btn.place(x=100, y=yp)  
            val += 1  
            yp += 40  
        return b  

    def display_options(self, qn):
        # Display the answer options for the current question
        val = 0  
        self.opt_selected.set(0)  
        for option in options[qn]:
            self.opts[val]['text'] = option  
            val += 1  

    def check_ans(self, qn):
        # Check if the selected answer option is correct
        if self.opt_selected.get() == a[qn]:
            return True

    def buttons(self):
        # Create the "Next" and "Quit" buttons
        n = Button(root, text="Next", command=self.next_btn, width=10, bg="green", fg="white",
                   font=("times", 16, "bold"))  # create the "Next" button
        n.place(x=200, y=380)  # set the position of the "Next" button
        q = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                   font=("times", 16, "bold"))  # create the "Quit" button
        q.place(x=380, y=380)  # set the position of the "Quit" button

    def next_btn(self):
        # Handle the "Next" button click event
        if self.check_ans(self.qn):
            self.correct += 1  
        self.qn += 1  
        if self.qn == len(q):
            self.display_result() 
        else:
            self.ques['text'] = q[self.qn]  
            self.display_options(self.qn)  

    def display_result(self):
        # Display the quiz result
        score = int(self.correct / len(q) * 100)  
        result = f"You scored {score}% in the quiz"  
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))  # display the result message in a message box
        root.destroy()  # destroy the window
        
# Create an instance of the Quiz class
quiz=Quiz()

# Start the GUI event loop
root.mainloop()
