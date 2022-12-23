from threading import Thread
import queue
from gui import openGui, changingGui
from connections import gettingStarted



if __name__ == "__main__":
    sq = queue.Queue()
    tkq = queue.Queue()
    t1 = Thread(target = openGui, args=(tkq, ))
    t2 = Thread(target = gettingStarted, args=(sq, tkq, ))
    t3 = Thread(target = changingGui, args=(sq, tkq, ))

    t1.start()
    t2.start()
    t3.start()