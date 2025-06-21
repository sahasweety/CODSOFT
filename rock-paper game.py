import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Main window setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("460x500")
root.config(bg="#f2f2f2")

# Game state variables
user_score = 0
computer_score = 0
current_round = 0
total_rounds = 0

# Ask number of rounds from user at the start
def ask_rounds():
    global total_rounds, current_round, user_score, computer_score
    user_score = 0
    computer_score = 0
    current_round = 0
    total_rounds = simpledialog.askinteger("Rounds", "How many rounds do you want to play?", minvalue=1)
    if total_rounds:
        rounds_label.config(text=f"🎯 Rounds: 0 / {total_rounds}")
        greeting.config(text="👋 Welcome to Rock-Paper-Scissors!")
        winner_label.config(text="")
        score_label.config(text="Your Score: 0 | Computer Score: 0")

# UI Labels
greeting = tk.Label(root, text="👋 Welcome to Rock-Paper-Scissors!", font=("Arial", 14, "bold"), bg="#f2f2f2")
greeting.pack(pady=5)

instructions = tk.Label(root, text="Choose your move below ⬇️", font=("Arial", 11), bg="#f2f2f2")
instructions.pack()

rounds_label = tk.Label(root, text="", font=("Arial", 11), bg="#f2f2f2")
rounds_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f2f2f2")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12), bg="#f2f2f2")
score_label.pack(pady=5)

choice_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
choice_label.pack(pady=5)

winner_label = tk.Label(root, text="", font=("Arial", 13, "bold"), fg="purple", bg="#f2f2f2")
winner_label.pack(pady=10)

# Game Logic
def play(user_choice):
    global user_score, computer_score, current_round, total_rounds

    if total_rounds == 0:
        messagebox.showinfo("Start Game", "Please choose number of rounds first.")
        return

    if current_round >= total_rounds:
        messagebox.showinfo("Game Over", "All rounds completed. Please reset to play again.")
        return

    computer_choice = random.choice(["rock", "paper", "scissors"])
    choice_label.config(text=f"You chose {user_choice.capitalize()} | Computer chose {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie! 🤝", fg="blue")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1
        result_label.config(text="🎉 You Win this Round!", fg="green")
    else:
        computer_score += 1
        result_label.config(text="💻 Computer Wins this Round!", fg="red")

    current_round += 1
    rounds_label.config(text=f"🎯 Rounds: {current_round} / {total_rounds}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

    # Auto declare winner after last round
    if current_round == total_rounds:
        declare_winner()

# Winner Logic
def declare_winner():
    if user_score > computer_score:
        winner = f"🎉 Congratulations! You Won the Game!\nFinal Score: You {user_score} - {computer_score} Computer"
    elif computer_score > user_score:
        winner = f"💻 Computer Won the Game!\nFinal Score: Computer {computer_score} - {user_score} You"
    else:
        winner = f"🤝 It's a Tie!\nFinal Score: You {user_score} - {computer_score} Computer"
    winner_label.config(text=winner)

# Reset Game
def reset_game():
    global user_score, computer_score, current_round, total_rounds
    user_score = 0
    computer_score = 0
    current_round = 0
    total_rounds = 0
    result_label.config(text="")
    choice_label.config(text="")
    score_label.config(text="Your Score: 0 | Computer Score: 0")
    winner_label.config(text="")
    rounds_label.config(text="")
    ask_rounds()

# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=15)

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=12, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=12, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=12, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

bottom_frame = tk.Frame(root, bg="#f2f2f2")
bottom_frame.pack(pady=15)

reset_btn = tk.Button(bottom_frame, text="🔁 Reset Game", width=15, bg="#ffcccb", command=reset_game)
reset_btn.grid(row=0, column=0, padx=10)

start_btn = tk.Button(bottom_frame, text="🎯 Set Rounds", width=15, bg="#ccffcc", command=ask_rounds)
start_btn.grid(row=0, column=1, padx=10)

# Run the app
ask_rounds()
root.mainloop()

