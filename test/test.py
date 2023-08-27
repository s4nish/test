import random

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

# Function to display and grade a question.
def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")
    
    user_answer = input("Enter the number of your answer: ")
    
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if 1 <= user_answer <= len(question_data["options"]):
            selected_option = question_data["options"][user_answer - 1]
            if selected_option == question_data["correct_answer"]:
                print("Correct!\n")
                return 1
            else:
                print(f"Sorry, the correct answer is {question_data['correct_answer']}.\n")
                return 0
        else:
            print("Invalid input. Please enter a number between 1 and 4.\n")
            return 0
    else:
        print("Invalid input. Please enter a number.\n")
        return 0

# Quiz loop
for question_data in questions:
    score += ask_question(question_data)

# Display the final score.
print(f"Quiz completed! Your score is {score}/{len(questions)}")
