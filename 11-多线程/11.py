import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1

def myJian():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1

if __name__ == '__main__':
    print("开始  {0}".format(sum))

    #开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myJian, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("采用多线程后  {0}".format(sum))