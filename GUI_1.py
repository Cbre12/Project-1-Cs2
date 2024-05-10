from tkinter import *
from tkinter import messagebox
import csv

class Gui:
    def __init__(self, window):
        """Initialize the GUI.
        :param window: The Tkinter window.
        :type window: object
        :rtype: None
        :return: None
        """
        
        # this code initializes the window. 
        self.window = window

        # This will build the frame for entering the number of students.
        self.frame_one = Frame(self.window)
        self.frame_one.pack(anchor=W)
        self.label_number = Label(self.frame_one, text='Enter the number of Students :')
        self.label_number.pack(side='left', padx=10)
        self.input_number = Entry(self.frame_one, width=10)
        self.input_number.pack(padx=0, pady=10)

        # this will create the frame for the first submit button.
        self.frame_two = Frame(self.window)
        self.frame_two.pack()
        self.button_save = Button(self.frame_two, text='Submit', command=self.submit)
        self.button_save.pack(pady=10)

        # This frame for entering scores.
        self.frame_three = Frame(self.window)
        self.output_label = Label(self.frame_three, text='Enter the students score(s) :')
        self.output_label.pack(pady=10)
        self.frame_three.pack()

        # This will initialize objects for use in the submission function.
        self.input_frame = None
        self.output_text = StringVar()

    def submit(self):
        """Action when the first submit button is pressed.
        :param self: the submit button function.
        :type self: object
        :rtype: none
        :return: none
        """
        number = self.input_number.get()
        if number.isdigit() and int(number) >= 1:
            number = int(number)
            self.create_input_frame(number)
        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    def create_input_frame(self, number):
        """Create input fields based on the number of students.
        :param number: This creates the input frame.
        :type number: object
        :rtype: none
        :return: none
        """
        # This will destroy existing input frame if there are any.
        if self.input_frame:
            self.input_frame.destroy()

        # This code creates a new input frame.
        self.input_frame = Frame(self.window)
        self.input_frame.pack(anchor=W)

        # This is the label for entering in the scores.
        self.label_Score = Label(self.input_frame, text=f'Enter The {number} Score(s) :')
        self.label_Score.grid(row=0, column=0, padx=10, sticky=W)

        # this is the input fields for scores.
        self.input_Scores = []
        for i in range(1, number + 1):
            entry = Entry(self.input_frame, width=10)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=W)
            self.input_Scores.append(entry)

        # this is the submit button for scores.
        self.button_save_two = Button(self.input_frame, text='Submit', command=self.grade_submit)
        self.button_save_two.grid(row=number + 1, column=1, columnspan=2, pady=10)

        # The output frame for showing the results of the scores. 
        self.output_frame = self.input_frame

    def grade_submit(self):
        """Process submitted scores and calculate grades.
        :param self: the grade submit button function.
        :type self: object
        :rtype: Error window object.
        :return: Error messages.  
        """
        # This will add the scores into a list to get them ready to be calculated into a letter grade. 
        scores = []
        for entry in self.input_Scores:
            try:
                score = int(entry.get())
                scores.append(score)
            except ValueError:
                messagebox.showerror("Error", "Please enter numeric values for all scores.")
                return

        # This will calculate grades for each student based on the scores that were entered above.
        result = ""
        for i, score in enumerate(scores, 1):
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'F'
            result += f"\nStudent {i} score is {score} and grade is {grade}"

        # This displays scores after the calculations have been completed for a letter grade. 
        self.output_text.set(result)
        output_label = Label(self.output_frame, textvariable=self.output_text, justify=LEFT)
        output_label.grid(row=len(scores) + 2, columnspan=2, padx=10)

        # This will send the results to the Grades CSV. 
        with open('Grades.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([result])

