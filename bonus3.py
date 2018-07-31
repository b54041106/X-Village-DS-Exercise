
#insert sort
def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

insertlist=[ 9, 64, 51, 76, 76, 96, 5, 18]
print('insert_sort:',insert_sort(insertlist))

#bubble sort
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
bubblelist = [20, 9, 100, 0, 55, 3 ,11]
print('bubble_sort:',bubble_sort(bubblelist))

#merge sort
def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    for x in left:
        print("左=", x, end=" ")
    right = merge_sort(lists[num:])
    for y in right:
        print("右=", y, end=" ")
    print(" ")
    return merge(left, right)

list1=[20, 9, 0, 55, 3,1,13,14,18,16]
mergelist=(merge_sort(list1))
print('merge_sort:',mergelist)


#quick sort
def quick_sort(list): #extra-place
    smaller = []
    bigger = []
    keylist = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                smaller.append(i)
            elif i > key: #比key值大的數
                bigger.append(i)
            else:
                keylist.append(i)

    smaller = quick_sort(smaller)
    bigger = quick_sort(bigger)
    return smaller + keylist + bigger
listquick=[20, 9, 0, 55, 3 ,1,13,14,18,16,17]
print('quick_sort:',quick_sort(listquick))

#heap sort
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)
 
def build_heap(lists, size):
    for i in range(0, (size//2))[::-1]:
        adjust_heap(lists, i, size)
 
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
a = [12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 5, 6]
heap_sort(a)
print('heap_sort:', a) 