lists=[12,1,2,3,45]
def recursiveList(lists,index=0):
    if index == len(lists):
        return 0
    print(lists[index],end=" ")
    recursiveList(lists,index+1)
recursiveList(lists)