from src.MovementGroup import MovementGroups

Move = MovementGroups()

#start, introducing pupper
#pupper says hello, dance, etc.
Move.head_ellipse()
#Move.look_up()
#Move.look_down()
#Move.stop()

# start_pupper = True


# list_of_commands = {
#     #basic movement: wasd keys
#     "w": Move.move_forward,
#     "s": Move.move_backward,
#     "a": Move.rotate(10),   #turn left 10 degree
#     "d": Move.rotate(-10),  #turn right 10 degree

#     #look movements: string input
#     "look up": Move.look_up(),
#     "look down": Move.look_down(),
#     "look right": Move.look_right(),
#     "look left": Move.look_left()
# }

# while start_pupper:
#     action = input("Next move (type 'exit' to quit): ")

#     if action == "exit":
#         start_pupper = False
#         print("Pupper stopped.")
    
#     elif action in list_of_commands:
#         print(f"Executing action: {action}")
#         calling_action = list_of_commands[action]
#         calling_action() #calls the corr action

#     else:
#         Move.body_row(30)
#         print("Invalid action, pupper is confused")


# MovementLib = Move.MovementLib