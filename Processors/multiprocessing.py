from multiprocessing import Process
import time

def checkParity(x):
    time.sleep(1)
    if x == 0:
        return "zero"
    elif x%2 == 0:
        return "even"
    else:
        return "odd"

def multiProcess(num):
    exp = num*num
    print(f"{num}^{num} is {checkParity(exp)}")

before = time.time()
for num in range(0,10):
    exp = num*num
    print(f"{num}^{num} is {checkParity(exp)}")
lDelta = round(time.time()-before,2)
print(f"Done. Loop took {lDelta} seconds")

before = time.time()
processes = []
for num in range(0,10):
    p = Process(target=multiProcess,args=(num,))
    processes.append(p)
    p.start()
for process in processes:
    process.join()
pDelta = round(time.time()-before,2)
print(f"Done. Process took {pDelta} seconds")
difference = round(lDelta-pDelta)
quotient = round(lDelta/pDelta,1)
print(f"Loop was {quotient}x slower than processing ({difference} secs difference)")