import threading
import time

# Threads cannot return values directly — you need a shared mutable object like a dict or list.
# Pass that object to the thread, and let the thread write results into it.
# time.sleep(1) simulates a long-running task.
# Threads run in parallel, so both squares are computed at roughly the same time.

def longSquare(n, result):
    """Function to compute the square of a number after a delay."""
    time.sleep(1)
    result[n] = n * n



def main():
    #print([longSquare(n) for n in range(0, 3)])  # Warm-up to avoid initial delay in timing  

    result = {}
    t1 = threading.Thread(target=longSquare, args=(3, result))
    t2 = threading.Thread(target=longSquare, args=(4, result)) 

    t1.start()
    t2.start()  

    t1.join()
    t2.join()   

    print(result)

    threads = [threading.Thread(target=longSquare, args=(n, result)) for n in range(0, 10)]
    
    for thread in threads:
        thread.start()
        thread.join()

    print(result)
    



if __name__ == "__main__":
    main()

