from src.MovementGroup import MovementGroups

Move = MovementGroups()

# Define the movement library
MovementLib = {
    "w": Move.move_forward,
    "s": Move.move_backward,
    "a": Move.rotate(10),   # turn left 10 degrees
    "d": Move.rotate(-10),  # turn right 10 degrees
    "look up": Move.look_up,
    "look down": Move.look_down,
    "look right": Move.look_right,
    "look left": Move.look_left,
}

def get_user_action():
    """Get user input for the next action"""
    action = input("Next move (type 'exit' to quit): ")
    if action == "exit":
        print("Pupper stopped.")
        return "exit"
    if action not in MovementLib:
        Move.body_row(30)
        print("Invalid action, pupper is confused")
        return None
    return action
