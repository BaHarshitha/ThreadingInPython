import threading
import os


def print_square(num1, num2):
    print("print_square assigned to thread:{}".format(threading.current_thread().name))

    print("Square: {}".format(num1 * num1))
    print("Square: {}".format(num2 * num2))


def print_cube(num):
    print("print_square assigned to thread:{}".format(threading.current_thread().name))

    print("Cube: {}".format(num * num * num))


if __name__ == "__main__":
    print("Id of process running main program:{}".format(os.getpid()))

    print("main thread name:{}".format(threading.current_thread().name))
    t1 = threading.Thread(target=print_square, args=(3332, 1))
    t2 = threading.Thread(target=print_cube, args=(3352,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
