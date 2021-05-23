import sys

def mergeSort(nlist):
    #print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",nlist)

#nlist = [14,46,43,27,57,41,45,21,70]
def read_ints(n):
    nlist=[]
    with open(n+".txt") as f:
        for line in f:
            ints =  line.split()
            for i in ints:
                nlist.append(int(i))
    return nlist

n = sys.argv[1]

nlist = read_ints(n)

n = len(nlist) 

mergeSort(nlist)
#print(nlist)
