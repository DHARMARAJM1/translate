# time = float(input("Enter time in Minutes and seconds"))
# time = time % (24 *3600)
# time %= 3600

# min = time // 60
# time %= 60
# seconds = time
# print("m:s-> %d%d" %(min,seconds))


from _typeshed import NoneType
import time
def myFunc ():
    start_time = time.time()
    s = 0
    for i in range (1, n+1):
        s= s+i
    end_time = time.time()
    return s, end_time-start_time

n = 5
print(myFunc())