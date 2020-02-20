import random

# So here is example how you can have a palindrome sekvence in your list.

def appendList(arr):
    for i in range(10):
        arr.append(i)

    palindrome = False

    for i in range(0,len(arr)-1):
        if arr[i]-1 < arr[i]:
            palindrome = True

    print(arr)
    return palindrome


print(appendList(list()))

# In this case we know its always going to be true.

# But what if we have an unsorted list ?
# For example , let say :

array = [2,7,4,8,9,3,1,6]

# We know this is never going to be true . Lets use sort method.

array.sort()

# We could use variables to sort our list manually , you can try it for practice.

print(array)

