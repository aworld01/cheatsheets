"""multithreading using threadingModule"""
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import time

"""Indicates some task being done"""
# def sleep(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)

"""Normal Code"""
# time1 = time.perf_counter() #to calculate the time
# sleep(4)
# sleep(2)
# sleep(5)
# time2 = time.perf_counter()
# print(time2 - time1)

"""Same code using Threads"""
# time1 = time.perf_counter() #to calculate the time
# t1 = Thread(target=sleep, args=[4])
# t2 = Thread(target=sleep, args=[2])
# t3 = Thread(target=sleep, args=[5])
# t1.start()
# t2.start()
# t3.start()
# time2 = time.perf_counter()
# print(time2 - time1)

"""Same code using .join() method"""
# time1 = time.perf_counter() #to calculate the time
# t1 = Thread(target=sleep, args=[4])
# t2 = Thread(target=sleep, args=[2])
# t3 = Thread(target=sleep, args=[5])
# t1.start()
# t2.start()
# t3.start()
""".join() method"""
# t1.join()
# t2.join()
# t3.join()
# time2 = time.perf_counter()
# print(time2 - time1)








"""multithreading using threadingModule"""
def sleep(seconds):
    time.sleep(seconds)
    print(f"Sleeping for {seconds} seconds")
    return "Return sleeping", {seconds}



"""example1"""
# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         executor.submit(sleep, 4)
#         executor.submit(sleep, 2)
#         executor.submit(sleep, 5)

# poolingDemo()


"""example2"""
# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         future1 = executor.submit(sleep, 4)
#         future2 = executor.submit(sleep, 2)
#         future3 = executor.submit(sleep, 5)
#         print(future1.result())
#         print(future2.result())
#         print(future3.result())

# poolingDemo()


"""example2"""
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l = [3,4,2,6]
        results = executor.map(sleep, l)
        for result in results:
            print(result)

poolingDemo()