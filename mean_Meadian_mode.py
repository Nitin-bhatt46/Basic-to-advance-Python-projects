
#mean
l1 =[12,3,4,56,89,33]
mean = sum(l1)/len(l1)
print(mean)




# median


l1.sort()

if len(l1) % 2 ==0:
    m1 = l1[len(l1)//2]
    m2 = l1[len(l1)//2-1]
    median = (m1+m2)/2
else:
    median = l1[len(l1)//2]
print(median)




# mode
frequency = {}
for i in l1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)






