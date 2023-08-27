import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Define colors
title_color = "#000000"
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
    {
        "question": "What is the capital of Japan?",
        "correct_answer": "Tokyo",
    },
    {
        "question": "How many days are there in a leap year?",
        "correct_answer": "366",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "correct_answer": "Carbon dioxide",
    },
    {
        "question": "What is the largest mammal in the world?",
        "correct_answer": "Blue whale",
    },
    {
        "question": "What is the closest planet to the Sun?",
        "correct_answer": "Mercury",
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "correct_answer": "William Shakespeare",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "correct_answer": "Au",
    },
    {
        "question": "Which gas makes up the majority of Earth's atmosphere?",
        "correct_answer": "Nitrogen",
    },
    {
        "question": "What is the largest organ in the human body?",
        "correct_answer": "Skin",
    },
]

# Shuffle the questions to make the quiz more interesting.
random.shuffle(questions)

# Initialize variables to keep track of user information and the user's score.
user_name = ""
score = 0
current_question = 0

# Default text size
text_size = 20

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
    question_number_label.config(text=f"Question {current_question + 1} of 12")

# Function to end the quiz and display the final score.
def end_quiz():
    if score == len(questions):
        messagebox.showinfo("Quiz Completed", f"Congratulations, {user_name}! Your score is {score}/{len(questions)}. 🐵")
    else:
        messagebox.showinfo("Quiz Completed", f"🐵 You should go back to school, {user_name}! Your score is {score}/{len(questions)}.")
    root.quit()

# Function to change text size
def change_text_size():
    global text_size
    new_text_size = simpledialog.askinteger("Text Size", "Enter the new text size:")
    if new_text_size:
        text_size = new_text_size
        set_text_sizes()

# Function to set text sizes
def set_text_sizes():
    title_label.config(font=("Cambria", text_size, "underline"))
    name_label.config(font=("Arial", text_size - 6, "underline"))
    name_entry.config(font=("Arial", text_size, "underline"))
    start_game_button.config(font=("Arial", text_size, "underline"))
    settings_button.config(font=("Arial", text_size, "underline"))
    additional_text_label.config(font=("Cambria", text_size - 6), fg=text_color)
    question_number_label.config(font=("Cambria", text_size - 6), fg=text_color)
    question_label.config(font=("Arial", text_size, "underline"))
    answer_entry.config(font=("Arial", text_size, "underline"))
    submit_button.config(font=("Arial", text_size, "underline"))

# Create the main application window.
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg=bg_color)

# Create and configure widgets for the name input interface.
name_frame = tk.Frame(root, bg=bg_color)
name_frame.pack(pady=200)  # Lowered the interface towards the center.

title_label = tk.Label(name_frame, text="Welcome to Are You Smarter Than a 5th Grader!", font=("Cambria", 24, "underline"), fg=title_color, bg=bg_color)
title_label.pack(pady=20)

name_label = tk.Label(name_frame, text="Enter your government name:", font=("Arial", text_size - 6, "underline"), fg=text_color, bg=bg_color)
name_label.pack(pady=10)

name_entry = tk.Entry(name_frame, font=("Arial", text_size, "underline"), fg=text_color, bg=bg_color)
name_entry.pack(pady=20)

start_game_button = tk.Button(name_frame, text="Start Game", command=start_quiz, font=("Arial", text_size, "underline"), fg=text_color, bg=bg_color)
start_game_button.pack(side="left")

# Button to access text size settings
settings_button = tk.Button(name_frame, text="Settings", command=change_text_size, font=("Arial", text_size, "underline"), fg=text_color, bg=bg_color)
settings_button.pack(side="left")

# Additional text below the title in the menu interface.
additional_text_label = tk.Label(name_frame, text="Can you recall what you learned in your school days?\nMany think they can, so let’s put it to the test!",
                                 font=("Cambria", text_size - 6), fg=text_color, bg=bg_color)
additional_text_label.pack()

# Create and configure widgets for the quiz.
question_frame = tk.Frame(root, bg=bg_color)  # Create a frame for the question interface.
question_frame.pack(pady=100, anchor="center")  # Centered the question interface within the window.

question_number_label = tk.Label(root, text="Question 1 of 12", font=("Cambria", text_size - 6), fg=text_color, bg=bg_color, anchor="e")
question_number_label.pack(fill="x", side="top", padx=20, pady=20)

question_label = tk.Label(question_frame, text="", font=("Arial", text_size, "underline"), fg=text_color, bg=bg_color)
question_label.pack()

answer_entry = tk.Entry(question_frame, font=("Arial", text_size, "underline"), fg=text_color, bg=bg_color)
answer_entry.pack(pady=20)

submit_button = tk.Button(question_frame, text="Submit", command=check_answer, font=("Arial", text_size, "underline"), fg=text_color, bg=bg_color)
submit_button.pack()

# Set initial text sizes
set_text_sizes()

# Run the main event loop.
root.mainloop()
