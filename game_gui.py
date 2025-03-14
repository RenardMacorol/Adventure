import tkinter as tk
from tkinter import messagebox
from mage import Mage
from archer import Archer
from swordsman import SwordsMan
from overlord import OverLord
from enemy import Enemy
from damageCounter import DamageCounter

root = tk.Tk()
root.title("Adventure Battle")
root.geometry("600x500")
root.configure(bg="#1e1e2e")  # Dark background

player = None
enemy = Enemy()

def select_character(choice):
    """Handles character selection and initializes the player."""
    global player
    classes = {"Mage": Mage, "Archer": Archer, "Swordsman": SwordsMan, "Overlord": OverLord}
    player = classes[choice]()
    char_label.config(text=f"{player.name} ({player.classType}) Selected", fg="white", bg="#1e1e2e")
    update_ui()

    # Enable ability buttons
    for btn in ability_buttons:
        btn["state"] = "normal"

def attack(ability):
    """Executes player's attack and triggers enemy counterattack."""
    global player, enemy
    if player and enemy.health > 0:
        cooldown = player.cooldownCheck()
        
        # Check if ability is on cooldown
        if isinstance(cooldown, int) and cooldown > 0:
            messagebox.showwarning("Cooldown", f"Ability on cooldown! Wait {cooldown} turns.")
            return
        
        print(f"Before attack: Enemy health = {enemy.health}, Player health = {player.health}")
        getattr(player, ability)(enemy)  # Player attacks enemy
        
        if enemy.health > 0:
            enemy_attack()  # Enemy counterattacks
            
        update_ui()
        check_game_status()
        print(f"After attack: Enemy health = {enemy.health}, Player health = {player.health}")

def enemy_attack():
    """Handles the enemy's counterattack."""
    global player, enemy
    if enemy.health > 0 and player.health > 0:
        DamageCounter.dmg(player, enemy, enemy.strength, enemy.name)  # Enemy attacks player

def check_game_status():
    """Checks if the game has ended based on health values."""
    if enemy.health <= 0:
        messagebox.showinfo("Victory", "You defeated the enemy!")
    elif player.health <= 0:
        messagebox.showinfo("Defeat", "You have been defeated!")

def update_ui():
    """Updates the UI with the latest health values."""
    enemy_health_label.config(text=f"Enemy Health: {max(0, enemy.health)}/300", fg="red", bg="#1e1e2e")
    if player:
        player_health_label.config(text=f"{player.name} Health: {max(0, player.health)}/300", fg="lightgreen", bg="#1e1e2e")
    root.update_idletasks()  # Force UI refresh

# Character Selection
char_frame = tk.Frame(root, bg="#1e1e2e")
char_frame.pack(pady=10)
char_label = tk.Label(char_frame, text="Choose Your Character", fg="white", bg="#1e1e2e", font=("Arial", 14, "bold"))
char_label.pack()

char_buttons = ["Mage", "Archer", "Swordsman", "Overlord"]
for char in char_buttons:
    btn = tk.Button(char_frame, text=char, command=lambda c=char: select_character(c), fg="white", bg="#3a3a5a", padx=10, pady=5, font=("Arial", 10, "bold"))
    btn.pack(side="left", padx=5)

# Health Display
player_health_label = tk.Label(root, text="Your Health: 300/300", fg="lightgreen", bg="#1e1e2e")
player_health_label.pack()

enemy_health_label = tk.Label(root, text="Enemy Health: 300/300", fg="red", bg="#1e1e2e")
enemy_health_label.pack()

# Attack Buttons
attack_frame = tk.Frame(root, bg="#1e1e2e")
attack_frame.pack(pady=10)

ability_buttons = []
attack_buttons = ["ability1", "ability2", "ability3"]
for atk in attack_buttons:
    btn = tk.Button(
        attack_frame,
        text=atk.replace("ability", "Ability "),
        command=lambda a=atk: attack(a),
        fg="white",
        bg="#ff6b6b",
        padx=10,
        pady=5,
        font=("Arial", 10, "bold"),
    )
    btn.pack(side="left", padx=5)
    btn["state"] = "disabled"  # Initially disabled
    ability_buttons.append(btn)

root.mainloop()
