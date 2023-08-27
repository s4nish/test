import random
import tkinter as tk
from tkinter import messagebox

# Define colors
text_color = "#D12727"
underline_color = "black"
bg_color = "#A8A7A6"

# Define a list of questions and their corresponding answers.
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Madrid", "Paris", "Berlin"],
        "correct_answer": "Paris",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Jupiter",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["3", "5", "7", "9"],
        "correct_answer": "7",
    },
]

# Shuffle the questions to make the quiz more interesting.
random.shuffle(questions)

# Initialize a variable to keep track of the user's score.
score = 0
current_question = 0

# Function to start the quiz.
def start_quiz():
    menu_frame.pack_forget()  # Hide the menu interface.
    display_question()  # Start displaying questions.

# Function to handle the submission of an answer.
def check_answer():
    global score, current_question

    user_answer = option_var.get()
    if user_answer == questions[current_question]["correct_answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        end_quiz()

# Function to display the current question.
def display_question():
    question_label.config(text=questions[current_question]["question"])
    for i in range(4):
        option_labels[i].config(text=questions[current_question]["options"][i])
    option_var.set(None)

# Function to end the quiz and display the final score.
def end_quiz():
    messagebox.showinfo("Quiz Completed", f"Quiz completed! Your score is {score}/{len(questions)}")
    root.quit()

# Create the main application window.
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg=bg_color)

# Create and configure widgets for the menu interface.
menu_frame = tk.Frame(root, bg=bg_color)
menu_frame.pack(pady=100)

quiz_name_label = tk.Label(menu_frame, text="Quiz Name", font=("Cambria", 36, "underline"), fg=text_color, bg=bg_color)
quiz_name_label.pack(pady=20)

created_by_label = tk.Label(menu_frame, text="Created by $anish", font=("Cambria", 16, "underline"), fg=text_color, bg=bg_color)
created_by_label.pack()

start_button = tk.Button(menu_frame, text="Start Quiz", command=start_quiz, font=("Arial", 24, "underline"), fg=text_color, bg=bg_color)
start_button.pack()

# Create and configure widgets for the quiz.
question_label = tk.Label(root, text="", font=("Arial", 24, "underline"), fg=text_color, bg=bg_color)
question_label.pack(pady=20)

option_var = tk.StringVar()
option_labels = []
for i in range(4):
    option_label = tk.Label(root, text="", font=("Arial", 20, "underline"), fg=text_color, bg=bg_color)
    option_label.pack()
    option_labels.append(option_label)
    option_radio = tk.Radiobutton(root, variable=option_var, value=questions[0]["options"][i])
    option_radio.pack()

submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 20, "underline"), fg=text_color, bg=bg_color)
submit_button.pack(pady=20)

# Run the main event loop.
root.mainloop()
