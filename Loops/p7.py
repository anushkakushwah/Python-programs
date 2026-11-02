#for i in range(3,10):
# print(i)
#for j in reversed(range(1,11,1)):
#print(j)
n = int(input("Enter the n:"))
first_num = 0
sec_num= 1
print (first_num, sec_num, end=" ")
for i in range(3, n+1):
    next = first_num + sec_num
    print(next, end = " ")
    first_num = sec_num
    sec_num = next
