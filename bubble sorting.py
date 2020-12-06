a = [1, 3, 6, 2, 9] #it can be your array

for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)