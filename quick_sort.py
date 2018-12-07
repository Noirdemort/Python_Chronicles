# quick sort algorithm
def quick_sort(a):
    def partition(a,f,u):
        pv = a[f]

        lm = f+1
        rm = u

        done = False

        while not done:
            while lm <= rm and a[lm]<=pv:
                lm+=1

            while lm <= rm and a[rm]>= pv:
                rm-=1

            if rm<lm:
                done = True
            else:
                a[lm],a[rm]=a[rm],a[lm]


        a[f], a[rm] = a[rm], a[f]
        return rm




    def qsh(a,f,u):
        if f<u:
            sp = partition(a,f,u)

            qsh(a,f,sp-1)
            qsh(a,sp+1,u)


    qsh(a,0,len(a)-1)
    return a

