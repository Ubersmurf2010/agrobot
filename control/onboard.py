from handler import ClientThread
import library
import sys
from time import sleep



if __name__ == "__main__":	
	
	rover = ClientThread(library.HOST, library.PORT)
	rover.setupConnection()
	rover.run()

	while True:     # бесконечный цикл
		try:
			sleep(10)
		except KeyboardInterrupt:
			rover.closeConnection()
			break
