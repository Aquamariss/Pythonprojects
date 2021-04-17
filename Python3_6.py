print ("k - max number of steak on the one pan is: ")
k = int(input())

print ("m - time of fry 1 steak on the one side is: ")
m = int(input())

print ("n - number of steak to roast is: ")
n = int(input())

x = 0
if (n//k!=0): x=1
R_time = (n//k+x)*2*m

print("You need ",R_time," minutes")



