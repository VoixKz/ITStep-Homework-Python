def access_to_outOfBounds_element(array, index):
    try:
        return array[index]
    except IndexError:
        while index > len(array):
            index -= len(array)
        return array[index]
    
result = access_to_outOfBounds_element(list(map(str, input("Enter the list (separate by space): ").split())), int(input("Enter the index: ")))
print(result)