sum = 0
l = 1
num = int(input("Enter a number "))

if num > l:
    for item in range(num):
        sum += item
    print(sum)
else:
    l+=1
