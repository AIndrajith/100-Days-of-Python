# Basic Math Quiz Game

import random

# Step 1: Define the math question fumction
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+','-','*'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else: 
        answer = num1 * num2

    return f"{num1} {operator} {num2}",answer

# Step 2: Main Quiz Game function
def math_quiz():
    score = 0

    print("\n---Welcome to the Math Quiz Game! ---")
    print("You will be presented with math problems, and you need to provid the correct answer.")
    print("\n----------------------------------------")
    rounds = int(input("How much rounds do you want to play: "))
    
    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        user_answer = int(input("Your answer: "))
            

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is : {correct_answer}")             

    print("\n---Game Over!---") 
    print(f"Your final score is : {score}/{rounds}")
    if score == rounds:
        print("Congratulations! You got al the questions correct.") 
    elif score >= rounds // 2:
        print("Good job! you did well.") 
    else:
        print("keep Practicing! You can do better next time.") 

# Step 3: Run the game
math_quiz()                      
            