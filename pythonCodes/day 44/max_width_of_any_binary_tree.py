# the code below uses a static array where none value denotes that node has not child(left/right)
'''
  the binary tree for the array below will be
              1
            /   \
           2     3
         /   \  /  \
        4    5  6   7
            / \
           8   9
'''



arr = [1,2,3,4,5,6,7,None,None,8,9,None,None,None,None]
l = 0
index = 0
maxArray = [1]
maxArrayValue = 0
while(index < len(arr)):
    for i in range(0,pow(2,l)):      
        if (2*index + 2) < len(arr) and arr[index] != None:
            if arr[2*index + 1] != None:
                maxArrayValue = maxArrayValue + 1
            if arr[2*index + 2] != None:
                maxArrayValue = maxArrayValue + 1
        index = index + 1
    maxArray.append(maxArrayValue)
    maxArrayValue = 0
    l = l + 1
print("The maximumwidth is :",max(maxArray))

