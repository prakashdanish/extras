#http://practice.geeksforgeeks.org/problems/check-if-a-number-can-be-expressed-as-xy/0
import math
t = int(input())

for i in range(t):
    n = int(input())
    fact = 2
    flag = 0
    while fact <= int(math.sqrt(n)):
        temp = n
        while temp > 1:
            if temp%fact == 0:
                temp = int(temp/fact)
            else:
                fact += 1
                break
        if temp == 1:
            flag = 1
            break
    if (flag == 1 and fact <= math.sqrt(n)) or n==1:
        print(1)
    else:
        print(0)
