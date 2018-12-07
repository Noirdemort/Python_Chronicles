def bucket_sort(arr):
    bucket = [ [] for _ in range(10)]
    n=10
    for i in arr:
        bi = (i)/n
        bucket[int(bi)].append(i)
    for i in bucket:
        i.sort()
    arr=[]
    for i in bucket:
        for j in i:
            arr.append(j)
    return arr
    