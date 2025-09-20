from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score_label = Label(text=f"score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(row=1, column=0, pady=25, columnspan=2)

        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"))

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.user_answer_false)
        self.false_button.grid(row=2, column=1 , padx=20, pady=25,)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.user_answer_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=25,)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():   
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text) 
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        self.canvas.config(highlightthickness=0, bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
    

    def user_answer_true(self):
        self.is_right = self.quiz.check_answer(True)
        self.score_label.config(text=f"score: {self.quiz.score}")
        self.give_feedback()

    def user_answer_false(self):
        self.is_right = self.quiz.check_answer(False)
        self.score_label.config(text=f"score: {self.quiz.score}")
        self.give_feedback()

    def give_feedback(self):
        if self.is_right:      
            self.canvas.config(highlightthickness=0, bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(highlightthickness=0, bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, func=self.get_next_question)
