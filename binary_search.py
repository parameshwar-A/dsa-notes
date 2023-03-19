

def binary_search(element, data, start, end, mid):
    if element>data[mid]:
        start=mid+1
        mid=(start+end)//2
        binary_search(element, data, start, end, mid)

    elif element<data[mid]:
        print("less")
        end=mid-1
        mid=(start+end)//2
        binary_search(element, data, start, end, mid)

    elif data[mid]==element:
        print(data.index(element))


test_data=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Remember the input needs to be sorted before processed
binary_search(5, test_data, 0, 8, 4)
