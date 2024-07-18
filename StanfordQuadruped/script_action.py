from src.MovementGroup import MovementGroups

Move = MovementGroups()

#start, introducing pupper
#pupper says hello, dance, etc.
Move.head_ellipse()
Move.body_row(45, 0.2, 0)
Move.body_row(-45, 0.2, 0)
Move.look_down()
Move.stop()





MovementLib = Move.MovementLib