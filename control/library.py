'''Configuration'''

'''TIMINGS '''
pulsebeat = 0.04
time_delay_seconds = 0.05
time_calibrate = 0.1

HOST="192.168.0.110"
PORT=65432

index = 1

keyboard = {
    "w": index,   #move_forward
    "s": index + 1,   #move_backward
    "a": index + 2,   #tank_turn_left
    "d": index + 3,   #tanl_turn_right
    "": index + 4,
    "": index + 5,
    "": index + 6,
    "": index + 7,
    "": index + 8,
    "": index + 9,
    "": index + 10,
    "": index + 11,
    "": index + 12,
    "": index + 13,
    "": index + 14,
    "": index + 15,
    "": index + 16,
    "": index + 17,
    "x": index + 18,  #speed_increase
    "z": index + 19,  #speed decrease
    "": index + 20,
    "": index + 21,
    "": index + 22,
    "": index + 23,
}
