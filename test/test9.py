import random
import tkinter as tk
from tkinter import messagebox

# Define colors
title_color = "#D12727"
text_color = "#D12727"
underline_color = "black"
bg_color = "#A8A7A6"

# Define a list of questions and their corresponding answers.
questions = [
    {
        "question": "What is the capital of France?",
        "correct_answer": "Paris",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "correct_answer": "Jupiter",
    },
    {
        "question": "How many continents are there on Earth?",
        "correct_answer": "7",
    },
]

# Shuffle the questions to make the quiz more interesting.
random.shuffle(questions)

# Initialize variables to keep track of user information and the user's score.
user_name = ""
score = 0
current_question = 0

# Function to start the quiz and get the user's name.
def start_quiz():
    global user_name
    user_name = name_entry.get().strip()
    name_frame.pack_forget()  # Hide the name input interface.
    display_question()  # Start displaying questions.

# Function to handle the submission of an answer.
def check_answer():
    global score, current_question

    user_answer = answer_entry.get().strip()  # Get the user's answer from the text input.
    correct_answer = questions[current_question]["correct_answer"]
    
    if user_answer.lower() == correct_answer.lower():
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        end_quiz()

# Function to display the current question.
def display_question():
    question_label.config(text=questions[current_question]["question"])
    answer_entry.delete(0, tk.END)  # Clear the previous answer.
    answer_entry.focus()  # Set focus to the answer entry.

# Function to end the quiz and display the final score.
def end_quiz():
    score_message = f"Congratulations, {user_name}! Your score is {score}/{len(questions)}."
    messagebox.showinfo("Quiz Completed", score_message)
    root.quit()

# Create the main application window.
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg=bg_color)

# Create and configure widgets for the name input interface.
name_frame = tk.Frame(root, bg=bg_color)
name_frame.pack(pady=100)

title_label = tk.Label(name_frame, text="Welcome to Are You Smarter Than a 5th Grader!", font=("Cambria", 20), fg=title_color, bg=bg_color)
title_label.pack(pady=20)

name_label = tk.Label(name_frame, text="Enter your government name:", font=("Arial", 20, "underline"), fg=text_color, bg=bg_color)
name_label.pack(pady=10)

name_entry = tk.Entry(name_frame, font=("Arial", 20, "underline"), fg=text_color, bg=bg_color)
name_entry.pack(pady=20)

start_game_button = tk.Button(name_frame, text="Start Game", command=start_quiz, font=("Arial", 24, "underline"), fg=text_color, bg=bg_color)
start_game_button.pack()

# Create and configure widgets for the quiz.
question_label = tk.Label(root, text="", font=("Arial", 24, "underline"), fg=text_color, bg=bg_color)
question_label.pack(pady=20)

answer_entry = tk.Entry(root, font=("Arial", 20, "underline"), fg=text_color, bg=bg_color)
answer_entry.pack(pady=20)

submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 20, "underline"), fg=text_color, bg=bg_color)
submit_button.pack(pady=20)

# Run the main event loop.
root.mainloop()

