import os

def parent_child():
    n = os.fork()
    # os.fork()
    # os.fork()
    # print("Parent process and id is :", os.getpid())
    # if n > 0:
    #     print("Parent process and id is :", os.getpid())
    # else:
    #     print("child process and id is : ", os.getpid())
    if (n and n):
        n
    print("Hello")

parent_child()