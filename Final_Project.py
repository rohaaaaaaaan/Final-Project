# rohaan mirza
# 17/1/25
# pd 1-2
# in this game you must collect all the pieces of trash to keep yourscore up and win the game while you evade monsters that will attack you and take away your health points which causes you to lose the game 

import simplegui
import random

# Global variables
room_description = "You are in a park. There is trash scattered around."
inventory = []
health = 100
score = 0
trash_to_collect = 5  # Number of trash to collect to win
game_over = False

# Define shapes for animation (like the player or trash)
player_position = [200, 200]
trash_positions = [[100, 100], [300, 100], [150, 300], [400, 400], [50, 400]]

# Game logic functions

def update_display():
    """Update all the displayed information in the GUI."""
    label_description.set_text(room_description)
    label_inventory.set_text("Inventory: " + ", ".join(inventory))
    label_health.set_text("Health: " + str(health))
    label_score.set_text("Score: " + str(score))
    label_trash.set_text(f"Trash Collected: {len(inventory)} / {trash_to_collect}")
    if game_over:
        label_description.set_text("Game Over! Press Restart to play again.")

def move_player():
    """Simple animation of player moving."""
    global player_position
    player_position[0] += random.choice([-20, 20])
    player_position[1] += random.choice([-20, 20])

def go_north():
    """Handle the 'Go North' action."""
    global room_description
    room_description = "You are in a forest. You can see more trash scattered around."
    random_event()
    update_display()

def go_south():
    """Handle the 'Go South' action."""
    global room_description
    room_description = "You are at a beach. The tide is coming in, and there's trash everywhere."
    random_event()
    update_display()

def examine_room():
    """Handle the 'Examine Room' action."""
    global room_description
    room_description += " You find some trash that you can pick up."
    update_display()

def pick_up_trash():
    """Handle picking up trash and adding it to the inventory."""
    global score, trash_positions
    if trash_positions:
        trash_positions.pop()
        inventory.append("Trash")
        score += 10
        if len(inventory) >= trash_to_collect:
            win_game()
    update_display()

def random_event():
    """Trigger a random event based on player actions."""
    event = random.choice(["find treasure", "lose health", "nothing happens"])
    if event == "find treasure":
        found_treasure()
    elif event == "lose health":
        lose_health()
    update_display()

def found_treasure():
    """Handle finding treasure."""
    global score
    score += 20
    update_display()

def lose_health():
    """Handle the player losing health."""
    global health
    health -= 10
    if health <= 0:
        game_over_screen()
    update_display()

def game_over_screen():
    """End the game when health reaches 0."""
    global game_over
    game_over = True
    update_display()

def win_game():
    """End the game with a win condition when trash is collected."""
    global room_description, game_over
    room_description = "Congratulations! You've collected all the trash."
    game_over = True
    update_display()

def restart_game():
    """Restart the game."""
    global room_description, inventory, health, score, trash_positions, game_over
    room_description = "You are in a park. There is trash scattered around."
    inventory = []
    health = 100
    score = 0
    trash_positions = [[100, 100], [300, 100], [150, 300], [400, 400], [50, 400]]
    game_over = False
    update_display()

# SimpleGUI elements
frame = simplegui.create_frame("Trash Collector Game", 500, 500)

# Create labels to display game information
label_description = frame.add_label(room_description)
label_inventory = frame.add_label("Inventory: ")
label_health = frame.add_label("Health: " + str(health))
label_score = frame.add_label("Score: " + str(score))
label_trash = frame.add_label(f"Trash Collected: {len(inventory)} / {trash_to_collect}")

# Add buttons for player actions
frame.add_button("Go North", go_north, 100)
frame.add_button("Go South", go_south, 100)
frame.add_button("Examine Room", examine_room, 100)
frame.add_button("Pick Up Trash", pick_up_trash, 100)
frame.add_button("Restart", restart_game, 100)

# Draw function for simple animations
def draw(canvas):
    # Draw player (represented by a simple circle)
    canvas.draw_circle(player_position, 20, 1, "Red", "Red")
    
    # Draw trash (represented by small circles)
    for pos in trash_positions:
        canvas.draw_circle(pos, 10, 1, "Green", "Green")
    
    # Update the player's position and animate movement
    move_player()

# Start the game loop
frame.set_draw_handler(draw)
update_display()
frame.start()
