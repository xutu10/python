family = ['aa','bb','cc',12]
print(family[2])
print(family[-1])

print('abcd'[2])
print("abcd"[3])
print("----------------")
number = [1,2,3,4,5,6]
print(number[0:4])
print(number[-3:-1])
print(number[-3:])
print(number[:3])
print(number[:])
print(number[0:6:2]) # how much increment
print(number[6:0:-2]) #backwards
print(number[::-2])
print("---------------")
x = [9,8,7] + [1,2,3]
print(x)
print("---------------")
# array functions
numbers = [2,45,66,88,26,8,98]
print(len(numbers))
print(max(numbers),min(numbers))
print(list("haha xutu"))
numbers[1] = 68
print(numbers)
del numbers[5]
print(numbers)
del numbers[:3]
print(numbers)

#slicing list
example = list('hello world')
print(example)
example[6:] = list('baby')
print(example)

#add elements
example = [6,7,8]
example[1:1] = [2,3,4]
print(example)
example1 = [6,7,8]
example1[1:2] = [2,3,4]
print(example1)
example[1:5] = []  #delete
print(example)




