from time import sleep
from servo import ServoController

time_delay_seconds = 0.1

''''Motor's pwm from servoHat'''

IN1 = 0
IN2 = 1
IN3 = 2
IN4 = 3


class motorEvent():
	def __init__(self, debug=False):
		self.controller = ServoController(0x40, debug=False)
		self.controller.setPWMFreq(7)
		self.debug = debug
		self.currentDutyCycle = 50


	def rotate_forward(self):
		self.controller.Set_DutyCycle(IN1, self.currentDutyCycle)
		self.controller.Set_DutyCycle(IN2, 0)

		self.controller.Set_DutyCycle(IN3, self.currentDutyCycle)
		self.controller.Set_DutyCycle(IN4, 0)
		print("clockwiae")

	def rotate_backward(self):
		self.controller.Set_DutyCycle(IN1, 0)
		self.controller.Set_DutyCycle(IN2, self.currentDutyCycle)

		self.controller.Set_DutyCycle(IN3, 0)
		self.controller.Set_DutyCycle(IN4, self.currentDutyCycle)
		print("counter clockwize")


	def turn_left(self):
		self.controller.Set_DutyCycle(IN1, 0)
		self.controller.Set_DutyCycle(IN2, self.currentDutyCycle)

		self.controller.Set_DutyCycle(IN3, self.currentDutyCycle)
		self.controller.Set_DutyCycle(IN4, 0)

		print("left")

	def turn_right(self):
		self.controller.Set_DutyCycle(IN1, self.currentDutyCycle)
		self.controller.Set_DutyCycle(IN2, 0)

		self.controller.Set_DutyCycle(IN3, 0)
		self.controller.Set_DutyCycle(IN4, self.currentDutyCycle)
		print("right")

	def stop(self):
		self.controller.Set_DutyCycle(IN1, 0)
		self.controller.Set_DutyCycle(IN2, 0)

		self.controller.Set_DutyCycle(IN3, 0)
		self.controller.Set_DutyCycle(IN4, 0)


	def break_motors(self):
		self.controller.Set_DutyCycle(IN1, 1)
		self.controller.Set_DutyCycle(IN2, 1)

		self.controller.Set_DutyCycle(IN3, 1)
		self.controller.Set_DutyCycle(IN4, 1)

	def increase_speed(self):
		if (self.currentDutyCycle < 94):
			self.currentDutyCycle = self.currentDutyCycle + 5
			print("duty cycle: ", self.currentDutyCycle)

	def decrease_speed(self):
		if (self.currentDutyCycle > 5):
			self.currentDutyCycle = self.currentDutyCycle - 5
			print("duty cycle: ", self.currentDutyCycle)



if __name__ == "__main__":
	motor = motorEvent()
	motor.rotate_forward()
	sleep(1)
	motor.rotate_backward()
	sleep(1)
	motor.turn_left()
	sleep(1)
	motor.turn_right()
	sleep(1)
	motor.stop()







