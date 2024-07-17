import numpy as np
import time
from IMU import IMU
from State import State
from MangDang.mini_pupper.HardwareInterface import HardwareInterface
from MangDang.mini_pupper.Config import Configuration
from Kinematics import four_legs_inverse_kinematics
from MangDang.mini_pupper.display import Display
from MovementScheme import MovementScheme
from play import MovementLib
from command import Command

def main(use_imu=False):
    """Main program without using Controller class
    """

    # Create config
    config = Configuration()
    hardware_interface = HardwareInterface()
    disp = Display()
    disp.show_ip()

    # Create imu handle
    if use_imu:
        imu = IMU(port="/dev/ttyACM0")
        imu.flush_buffer()

    # Initialize state
    state = State()

    # Create movement group scheme instance and set a default True state
    movementCtl = MovementScheme(MovementLib)
    dance_active_state = True
    lib_length = len(MovementLib)

    last_loop = time.time()

    command = Command()
    command.pseudo_dance_event = True

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

        # Step the movement scheme forward by dt
        if dance_active_state:
            # Calculate legsLocation, attitudes and speed using custom movement script
            movementCtl.runMovementScheme()
            command.legslocation = movementCtl.getMovemenLegsLocation()
            command.horizontal_velocity = movementCtl.getMovemenSpeed()
            command.roll = movementCtl.attitude_now[0]
            command.pitch = movementCtl.attitude_now[1]
            command.yaw = movementCtl.attitude_now[2]
            command.yaw_rate = movementCtl.getMovemenTurn()

            # Directly calculate joint angles using inverse kinematics
            joint_angles = four_legs_inverse_kinematics(
                command.legslocation,
                command.horizontal_velocity,
                command.roll,
                command.pitch,
                command.yaw
            )
            state.joint_angles = joint_angles
        else:
            # Handle non-dance state if necessary
            pass

        if movementCtl.movement_now_number >= lib_length - 1 and movementCtl.tick >= movementCtl.now_ticks:
            print("exit the process")
            break

        # Update the pwm widths going to the servos
        hardware_interface.set_actuator_postions(state.joint_angles)

main()
