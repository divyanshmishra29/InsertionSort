def selection(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min=j
        a[i],a[min]=a[min],a[i]
    return a
print(selection([2,4,3,1,6]))
