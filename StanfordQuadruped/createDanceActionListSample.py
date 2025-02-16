#
# Copyright 2024 MangDang (www.mangdang.net) 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Description: You can use the following FPC(Flexible Programmable Choreography) APIs to define your Mini Pupper to dance.
#              There are 3 levels of APIs
#                 Level 1(for beginners): Simple APIs without input parameters
#                 Level 2(for makers): APIs with input parameters
#                 Level 3(for beyond): Samples delicately control the foot locations, move speed, and attitudes at each execution time.
#
# Test method 1 by the controller:
#   step1: Pair the controller to your Mini Pupper after power on
#   step2: Click controller "L1" button
#   step3: Click controller "Circle" button 
#   the mini pupper will dance based on your following script.
#
#
#Test method 2 by command line:
#   After editing this file, run run_danceActionList.py to do your designed movements
#   $python /home/ubuntu/StanfordQuadruped/run_danceActionList.py
#
#
# Level 1(for beginners): Movement Action API List without input parameters
# stop()
# look_up()
# look_down()
# look_right()
# look_left()
# look_upperright()
# look_upperleft()
# look_rightlower()
# look_leftlower()
# move_forward()
# move_backward()
# move_right()
# move_left()
# move_rightfront()
# move_leftfront()
# move_rightback()
# move_leftback()

# stop()
# Level 2(for makers): Movement Action API List with input parameters
# body_row(row_deg,  time_uni, time_acc)
# gait_uni(v_x, v_y, time_uni, time_acc)
# height_move(ht,    time_uni, time_acc)
# head_move(pitch_deg, yaw_deg, time_uni, time_acc)
# foreleg_lift(leg_index, ht,   time_uni, time_acc)
# backleg_lift(leg_index, ht,   time_uni, time_acc)
#
# Level 3(for beyond) samples
#  body_cycle()
#  head_ellipse()
#
#

from src.MovementGroup import MovementGroups

Move = MovementGroups()

# Level 1: movements without input parameters
Move.stop()
Move.look_up()
Move.look_down()
Move.look_right()
Move.look_left()
Move.look_upperright()
Move.look_upperleft()
Move.look_rightlower()
Move.look_leftlower()
Move.move_forward()
Move.move_backward()
Move.move_right()
Move.move_left()
Move.move_rightfront()
Move.move_leftfront()
Move.move_rightback()
Move.move_leftback()


# Level 2: movements with input parameters
Move.head_move(20, 10)
Move.stop()
Move.body_row(30)
Move.stop()
Move.gait_uni(0.1,0)
Move.gait_uni(-0.1, -0.1)
Move.stop()
Move.height_move(0.03)
Move.height_move(-0.02)
Move.foreleg_lift("left", 0.03)
Move.stop()
Move.stop()
Move.rotate(45)
Move.rotate(-45)
Move.bowback(30)


# Level 3 samples
Move.body_cycle()
Move.head_ellipse()

MovementLib = Move.MovementLib
