from lib.queue import Queue

q = Queue()
def hot_potato(name_list, num):

    for i in name_list:
        q.enqueue(i)

    while q.size()!=1:
        for j in range(num):
            person=q.dequeue()
            q.enqueue(person)
        q.dequeue()
     
    if q.size()==1:
        remaining_person=q.dequeue()
        return remaining_person

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7)) # 回傳 "Susan"
print(hot_potato(["Susan","Brad","Kent","David"], 6))# 回傳 "Brad"