import numpy as np
import time
import threading
from src.IMU import IMU
from src.Controller import Controller
from src.State import State
from MangDang.mini_pupper.HardwareInterface import HardwareInterface
from MangDang.mini_pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
from MangDang.mini_pupper.display import Display
from src.MovementScheme import MovementScheme
from src.Command import Command
from src.MovementGroup import MovementGroups

def get_user_input():
    while True:
        command = input("Enter command: ")
        if command in command_mapping:
            command_queue.append(command)

def main(use_imu=False):
    """Main program"""

    # Create config
    config = Configuration()
    hardware_interface = HardwareInterface()
    disp = Display()
    disp.show_ip()

    # Create imu handle
    if use_imu:
        imu = IMU(port="/dev/ttyACM0")
        imu.flush_buffer()

    # Create controller and user input handles
    controller = Controller(
        config,
        four_legs_inverse_kinematics,
    )
    state = State()

    last_loop = time.time()

    command = Command()

    # Create an instance of MovementGroups
    movement_groups = MovementGroups()

    # Start a separate thread to get user input
    input_thread = threading.Thread(target=get_user_input)
    input_thread.daemon = True
    input_thread.start()

    while True:
        now = time.time()
        if now - last_loop < config.dt:
            continue
        last_loop = time.time()

        # Read imu data. Orientation will be None if no data was available
        quat_orientation = (
            imu.read_orientation() if use_imu else np.array([1, 0, 0, 0])
        )
        state.quat_orientation = quat_orientation

        # Check if there is a command in the queue
        if command_queue:
            user_command = command_queue.pop(0)
            command_mapping[user_command]()
            print("Exectuing action: {command_queue}")

        elif command_queue == "exit":
            print("Pupper stopped")
            return False

        else:
            print("Pupper is confused...")
            movement_groups.body_row(30)
        # Step the controller forward by dt
        controller.run(state, command, disp)

        # Update the pwm widths going to the servos
        hardware_interface.set_actuator_postions(state.joint_angles)

# Command queue and mapping
command_queue = []

movement_groups = MovementGroups()

command_mapping = {
    "w": lambda: movement_groups.move_forward(),
    "s": lambda: movement_groups.move_backward(),
    "a": lambda: movement_groups.rotate(10),
    "d": lambda: movement_groups.rotate(-10),
    "look up": lambda: movement_groups.look_up(),
    "look down": lambda: movement_groups.look_down(),
    "look right": lambda: movement_groups.look_right(),
    "look left": lambda: movement_groups.look_left(),

    "exit": lambda: movement_groups.stop()
}

main()
