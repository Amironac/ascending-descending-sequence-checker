import random

# So here is example how you can have a ascending or descending sekvence in your list.

def appendList(arr):
    for i in range(10):
        arr.append(i)

    sequence = False

    for i in range(0,len(arr)-1):
        if arr[i]-1 < arr[i]:
            sequence = True

    print(arr)
    return sequence


print(appendList(list()))

# In this case we know its always going to be true.

# But what if we have an unsorted list ?
# For example , let say :

array = []

for i in range(10):
    integer = random.randint(0,10);
    array.append(integer)

    
# We know this is never going to be true . Lets use sort method.

array.sort()

#Basicly what we did in previous function is checked if function is sorted. 


# We could use variables to sort our list manually , you can try it for practice.

print(array)

