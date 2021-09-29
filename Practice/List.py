#!/usr/bin/python3

list1 = ['physics', 'chemistry', '1997', '2000'];
list2 = ['1', '2', '3', '4', '5'];
list3 = ["a", "b", "c", "d"]

print('list1[0]: ' + list1[0])
print('list2[1:5]: ' + repr(list2[1:5]))

print('Value available at index 2 : ')
print(list1[2])

list1[2] = 2001;
print('New value available at index 2 : ')
print(list1[2])

print(list1)
del list1[2];
print('After deleting value at index 2 : ')
print(list1)