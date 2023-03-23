def merge_sort(data):
    if len(data)>1:
        mid=len(data)//2
        left=data[:mid]
        right=data[mid:]
        merge_sort(left)

        merge_sort(right)

        i=j=0
        for k in range(len(data)):
            if i<len(left) and j<len(right):
                if left[i]<right[j]:
                    data[k]=left[i]
                    i+=1
                else:
                    data[k]=right[j]
                    j+=1
            elif i<len(left):
                data[k]=left[i]
                i+=1
            elif j<len(right):
                data[k]=right[j]
                j+=1
            else:
                break
    else:
        return None


array=[6,1,5,9,10, 2, 30, 7]
#array=[10,2]
#array=[1,2,3,4,5,6,7]
merge_sort(array)
print(array)
