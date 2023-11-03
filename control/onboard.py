from handler import ClientThread

import library
import sys
from time import sleep


if __name__ == "__main__":
    agrobot = ClientThread(library.HOST, library.PORT)
    agrobot.setupConnection()
    agrobot.run()

    while True:
        try:
            sleep(10)
        except KeyboardInterrupt:
            agrobot.clientsocket()
            break