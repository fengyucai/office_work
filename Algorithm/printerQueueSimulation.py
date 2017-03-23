from pythonds.basic import Queue
import random

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []   # waiting times in the queue

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()
        
    averageWaitTime = sum(waitingtimes) / len(waitingtimes)
    print('Average Wait %6.2f secs. %3d tasks remaining.' %\
        (averageWaitTime, printQueue.size()))


class Printer:
    def __init__(self, pagesPerMin):
        self.ppm = pagesPerMin
        self.currentTask = None
        self.remainingTime = 0
    
    def busy(self):
        return self.currentTask != None
    
    def tick(self):
        if self.currentTask != None:
            self.remainingTime -= 1
            if self.remainingTime <= 0:
                self.currentTask = None

    def startNext(self, nextTask):
        self.currentTask = nextTask
        self.remainingTime = nextTask.getPages() * 60 / self.ppm 

class Task:
    def __init__(self, currentSecond):
        self.timestamp = currentSecond
        self.pages = random.randrange(1, 21)

    def getPages(self):
        return self.pages
    
    def waitTime(self, currentSecond):
        return currentSecond - self.timestamp 


def newPrintTask():
    return random.randrange(1, 181) == 180


for i in range(10):
    simulation(3600, 5)
