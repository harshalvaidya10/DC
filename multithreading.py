import threading 


def fibonacci(num):

    a = 0 
    b = 1

    if num >= 1:
        print(f"Fib 1: {a}\n")
    
    if num >= 2:
        print(f"Fib 2: {b}\n")

    if num >= 3 :
        for i in range(2, num):
            c = a + b
            print(f"Fib {i + 1}: {c}\n")
            a = b
            b = c

fib_thread = threading.Thread(target = fibonacci, args = (10,))
fib_thread.start()
fib_thread.join()