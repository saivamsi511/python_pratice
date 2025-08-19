import tkinter as tk 

class QuizApp:
    def __init__(self):
        self.quiz_data = [
            {
            "question":"what is my name?",
            "options":["vamsi","sai","mithun"],
            "correct_answer":0
            },
            {
            "question":"what is my aim?",
            "options":["machine learning analyst","data science","python developer"],
            "correct_answer":2
            },
            {
            "question":"what is my language?",
            "options":["java","python","c++"],
            "correct_answer":1
            }
        ]
        self.current_question_index = 0
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Quiz App")

def start_Quiz(self):
    #self.load_question
    self.window.mainloop()
quiz_app=QuizApp()
quiz_app.start_Quiz()