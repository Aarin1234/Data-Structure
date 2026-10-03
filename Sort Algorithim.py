mylist = [4,21,45,42,36,87,1230,10,231,103,]
print(f"\n Original mylist = {mylist}")

mylist.sort(reverse= True)
print(f'Sorted mylist in descending order = {mylist}')


print(f'Sorted mylist in ascending order = {sorted(mylist, reverse = False)}\n\n')
#--------------------------------------------------
#Bubble Sort
mylist1 = [12,43,123,453,55,66765,234,987,67,87,8765432,21344,123334,11,1]
print(f'Original mylist = {mylist1}')
for i in range(len(mylist1)):
    for j in range(i, len(mylist1)):
        if mylist1[i] < mylist1[j]:
            mylist1[i], mylist1[j] = mylist1[j], mylist1[i]

print(f'Sorted mylist (in descending order = {mylist1})\n\n')
#--------------------------------------------------

print(f'{"-"*30}\nBubble Sort(Ascending order)')
mylist2 = [12,21,345,78,97,6,4,9,435,]
print(f'Original mylist = {mylist2}')
for i in range(len(mylist2)):
    for j in range(0, len(mylist2)-i-1):
        if mylist2[j] > mylist2[j+1]:
            mylist2[j], mylist2[j+1] = mylist2[j+1], mylist2[j]
print(f'Sorted list in (Ascending order = {mylist2})')
