arr2=[1,2,3,4,5,6,7,8] 
arr1=[1,3,5,7,9,8]
print("Duplicate elements in given array: ");    
for i in range(0, len(arr1)):    
    for j in range(0,len(arr2)):    
        if(arr1[i] == arr2[j]):    
            print(arr2[j])


