#Selection sort
def selectSort(arr):
    n=len(arr)
    for i in range(n-1):
        current=i
        for j in range(i+1, n):
            if arr[j]<arr[current]:
                current=j
            
        if current!=i:
            arr[i], arr[current] =arr[current], arr[i]
           
    return arr

#Two pointers
def twoSum(arr,target):
    selectSort(arr)
    n=len(arr)
    left=0
    right = n-1
    output=[]
    while left<=right:
        sum= arr[left]+arr[right]
        if sum==target:
            output.append(arr[left])
            output.append(arr[right])
            return output
        elif sum<target:
            left+=1
        else:
            right-=1

print(twoSum([7,1,8,3,0,9], 11))


#merge alternately