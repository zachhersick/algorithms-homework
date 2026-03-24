#by Zach Hersick (Programmer) and Christian Vaikona (Navigator)

def search_2d_matrix(target, matrix):
    if not matrix or not matrix[0]:
        return None
    
    current = (0, len(matrix[0])-1)
    
    while (current[0] < len(matrix) and current[1] >= 0):
        if matrix[current[0]][current[1]] > target:
            current = (current[0], current[1]-1)
            
        elif matrix[current[0]][current[1]] < target:
            current = (current[0]+1, current[1])
        
        else:
            return current
    
    return None

print(search_2d_matrix(5, [[1, 4, 7],[2, 5, 8],[3, 6, 9]]))
print('expected = (1, 1)')
print('---------------------')
print(search_2d_matrix(10, [[1, 4, 7],[2, 5, 8],[3, 6, 9]]))
print('expected = None')
print('---------------------')
print(search_2d_matrix(3, [[1, 3, 5, 7, 9]]))
print('expected = (0, 1)')
print('---------------------')
print(search_2d_matrix(6, [[1],[3],[5],[7]]))
print('expected = None')
print('---------------------')
print(search_2d_matrix(42, [[42]]))
print('expected = (0, 0)')
print('---------------------')
print(search_2d_matrix(42, [[]]))
print('expected = None')
print('---------------------')
print(search_2d_matrix(42, []))
print('expected = None')
    
        