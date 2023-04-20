#import sys
import multiprocessing

def child_process1():
    for i in range(10):
        print(i)

def child_process2():
    for i in range(100,110):
        print(i)

if __name__ == '__main__':
    print("main process")
    childProcess1 = multiprocessing.Process(target=child_process1)
    childProcess1.start()
    childProcess2 = multiprocessing.Process(target=child_process2)
    childProcess2.start()