import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import os

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Game variables
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.choices = ['rock', 'paper', 'scissors']
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create all GUI widgets"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="🪨 Rock Paper Scissors ✂️", 
            font=('Arial', 24, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Choose your weapon by clicking one of the buttons below:",
            font=('Arial', 12),
            bg='#f0f0f0',
            fg='#34495e'
        )
        instructions.pack(pady=10)
        
        # Game buttons frame
        buttons_frame = tk.Frame(self.root, bg='#f0f0f0')
        buttons_frame.pack(pady=20)
        
        # Rock button
        self.rock_btn = tk.Button(
            buttons_frame,
            text="🪨 ROCK",
            font=('Arial', 14, 'bold'),
            bg='#e74c3c',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.play_game('rock')
        )
        self.rock_btn.pack(side=tk.LEFT, padx=10)
        
        # Paper button
        self.paper_btn = tk.Button(
            buttons_frame,
            text="📄 PAPER",
            font=('Arial', 14, 'bold'),
            bg='#3498db',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.play_game('paper')
        )
        self.paper_btn.pack(side=tk.LEFT, padx=10)
        
        # Scissors button
        self.scissors_btn = tk.Button(
            buttons_frame,
            text="✂️ SCISSORS",
            font=('Arial', 14, 'bold'),
            bg='#2ecc71',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.play_game('scissors')
        )
        self.scissors_btn.pack(side=tk.LEFT, padx=10)
        
        # Game result frame
        self.result_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.result_frame.pack(pady=20)
        
        # User choice label
        self.user_choice_label = tk.Label(
            self.result_frame,
            text="Your choice: ",
            font=('Arial', 14),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        self.user_choice_label.pack()
        
        # Computer choice label
        self.computer_choice_label = tk.Label(
            self.result_frame,
            text="Computer choice: ",
            font=('Arial', 14),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        self.computer_choice_label.pack()
        
        # Result label
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#e74c3c'
        )
        self.result_label.pack(pady=10)
        
        # Score frame
        score_frame = tk.Frame(self.root, bg='#f0f0f0')
        score_frame.pack(pady=20)
        
        # Score labels
        self.score_label = tk.Label(
            score_frame,
            text="Score: You 0 - Computer 0",
            font=('Arial', 14, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        self.score_label.pack()
        
        self.rounds_label = tk.Label(
            score_frame,
            text="Rounds played: 0",
            font=('Arial', 12),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.rounds_label.pack()
        
        # Control buttons frame
        control_frame = tk.Frame(self.root, bg='#f0f0f0')
        control_frame.pack(pady=20)
        
        # Reset button
        reset_btn = tk.Button(
            control_frame,
            text="🔄 Reset Game",
            font=('Arial', 12, 'bold'),
            bg='#f39c12',
            fg='white',
            width=15,
            height=2,
            command=self.reset_game
        )
        reset_btn.pack(side=tk.LEFT, padx=10)
        
        # Exit button
        exit_btn = tk.Button(
            control_frame,
            text="❌ Exit Game",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            width=15,
            height=2,
            command=self.root.quit
        )
        exit_btn.pack(side=tk.LEFT, padx=10)
        
    def get_computer_choice(self):
        """Generate random choice for computer"""
        return random.choice(self.choices)
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner based on game rules"""
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"
    
    def play_game(self, user_choice):
        """Play a round of the game"""
        computer_choice = self.get_computer_choice()
        
        # Update choice labels
        self.user_choice_label.config(text=f"Your choice: {user_choice.upper()}")
        self.computer_choice_label.config(text=f"Computer choice: {computer_choice.upper()}")
        
        # Determine winner
        result = self.determine_winner(user_choice, computer_choice)
        
        # Update scores and display result
        if result == "tie":
            self.result_label.config(text="🤝 It's a TIE!", fg='#f39c12')
        elif result == "user":
            self.user_score += 1
            self.result_label.config(text="🎉 You WIN!", fg='#27ae60')
        else:
            self.computer_score += 1
            self.result_label.config(text="💻 Computer WINS!", fg='#e74c3c')
        
        self.rounds_played += 1
        
        # Update score display
        self.update_score_display()
        
        # Check for game end (optional - play to 5 wins)
        if self.user_score >= 5 or self.computer_score >= 5:
            self.end_game()
    
    def update_score_display(self):
        """Update the score and rounds display"""
        self.score_label.config(text=f"Score: You {self.user_score} - Computer {self.computer_score}")
        self.rounds_label.config(text=f"Rounds played: {self.rounds_played}")
    
    def end_game(self):
        """End the game and show final results"""
        if self.user_score > self.computer_score:
            winner = "You"
            message = f"🎊 CONGRATULATIONS!\nYou won the game {self.user_score}-{self.computer_score}!"
        else:
            winner = "Computer"
            message = f"🤖 Game Over!\nComputer won {self.computer_score}-{self.user_score}!"
        
        messagebox.showinfo("Game Over", message)
        
        # Ask if user wants to play again
        play_again = messagebox.askyesno("Play Again?", "Would you like to play another game?")
        if play_again:
            self.reset_game()
        else:
            self.root.quit()
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        
        # Reset labels
        self.user_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer choice: ")
        self.result_label.config(text="")
        self.update_score_display()

def main():
    """Main function to run the game"""
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
