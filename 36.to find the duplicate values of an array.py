arr=[1,1,2,4,3,4,5,3,6,7,8]     
print("Duplicate elements in given array: ");    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j])