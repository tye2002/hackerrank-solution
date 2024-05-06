def performOperations (arr, operations):
    for operation in operations:
        start, end = operation
        arr[start:end+1]= arr[start:end+1][::-1]
    return arr

# Example usage:
arr = [1,2,3]
operations=[[0,2],[1,2],[0,2]]
print(performOperations(arr, operations))

arr = [9,8,7,6,5,4,3,2,1,0]
operations = [[0,9],[4,5],[3,6],[2,7],[1,8],[0,9]]
print(performOperations(arr, operations))