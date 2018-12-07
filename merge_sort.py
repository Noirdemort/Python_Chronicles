# programs for merge sort
def mergeme(a):

    if len(a)>1:
        x = len(a)//2

        lh = a[:x]
        rh = a[x:]

        mergeme(lh)
        mergeme(rh)

        i=0;j=0;k=0

        while i<len(lh) and j< len(rh):
               if lh[i]<rh[j]:
                   a[k]=lh[i]
                   i+=1
               else:
                   a[k]=rh[j]
                   j+=1
               k+=1

        while i<len(lh):
                a[k]=lh[i]
                i+=1
                k+=1

        while j < len(rh):
                a[k]=rh[j]
                j+=1
                k+=1

    return a
