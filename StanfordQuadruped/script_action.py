from src.MovementGroup import MovementGroups

Move = MovementGroups()

# Define the movement library
MovementLib = {
    0: Move.move_forward,
    1: Move.move_backward,
    2: lambda: Move.rotate(10)(),   # turn left 10 degrees
    3: lambda: Move.rotate(-10)(),  # turn right 10 degrees
    4: Move.look_up,
    5: Move.look_down,
    6: Move.look_right,
    7: Move.look_left,
}

def get_user_action():
    """Get user input for the next action"""
    action = input("Next move (type 'exit' to quit): ")
    if action == "exit":
        print("Pupper stopped.")
        return "exit"
    if action not in MovementLib.values():
        Move.body_row(30)
        print("Invalid action, pupper is confused")
        return None
    return action
