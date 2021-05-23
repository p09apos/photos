import sys

def read_ints(n):
    int_list=[]
    with open(n+".txt") as f:
        for line in f:
            ints =  line.split()
            for i in ints:
                int_list.append(int(i))
    return int_list

n = sys.argv[1]

int_list = read_ints(n)

#print (int_list)
#bubble_sort(int_list)
#print( insertion_sort(int_list) )


#a = [16, 19, 11, 15, 10, 12, 14]

#repeating loop len(a)(number of elements) number of times
for j in range(len(int_list)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(int_list)-1:
        #comparing the adjacent elements
        if int_list[i]>int_list[i+1]:
            #swapping
            int_list[i],int_list[i+1] = int_list[i+1],int_list[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
#print (int_list)
