Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
num = random.random()
if num>1:
    for i in range(2, num):
        if (num%i) == 0:
            print(num, "is a Composite number")
            break
    else:
        print(num, "is a PRIME number")
elif num== 0 or 1:
    print(num,"is a neither prime nor composite number")
else:
    print(num,"it is a Composite number")
if num> 0:print(num,"is a Positive number")
elif num==0:
    print("zero")
else:
    print(num,"is a Negative number")



if (num%2)==0:
    print(num," is Even number")
else:
    print(num, "is Odd number")