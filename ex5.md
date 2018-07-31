sort 是應用在 list 上的方法，sort是在原位重新排列列表。

sorted 可以對所有可迭代的对象進行排序操作，返回的是一個新的 list。
sorted(iterable[, cmp[, key[, reverse]]])

list.sort 方法只可以供列表使用，而 sorted 函數可以接受任意可疊代對象(iterable)


python中的sorted算法，通过阅读官方文档，发现python中的sorted排序，真的是高大上，用的Timsort算法。
https://blog.csdn.net/kobe2016/article/details/79144534
Timsort是结合了合并排序（merge sort）和插入排序（insertion sort）
https://blog.csdn.net/yangzhongblog/article/details/8184707