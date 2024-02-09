import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.score = 0
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text=f"Score: {self.score}", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg="white", borderwidth=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280 ,text="none", fill=THEME_COLOR, font=QUESTION_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)
        right_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=right_image, bd=0,
                                     highlightthickness=0, activebackground=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, bd=0,
                                      highlightthickness=0, activebackground=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the test")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(ms=1000, func=self.get_next_question)