import math

k = input('')
n = int(input(''))
a = input('').split()

if len(a) == n:
    pass
else:
    print("error in a input")

count = 0    
lst = []   
count += len(a)


if int(a[0]) <= int(k):
        count += 1
    
else:
    count += math.ceil(int(a[0]) / int(k))


if int(a[-1]) <= int(k):
    count += 1
else:
    count += math.ceil(int(a[-1]) / int(k))

for i in range(0, len(a) - 1):
    lst.append(abs(int(a[i + 1]) - int(a[i])))

new = []
for num in lst:
    new.append(num)
for i in new:
    count += math.ceil(int(i) / int(k))
    



print(count)

