light_matrix_string = "00000:00000:00000:00000:00000"

# Convert light matrix to a multidimensional array
def convert_light_string_to_array(array_str):
    outer_demension = array_str.split(':')
    multi_dimension_array = []
    
    for inner in outer_demension:
        inner_list = [int(char) for char in inner]
        multi_dimension_array.append(inner_list)
        
    return multi_dimension_array


# Convert Light Array to a string to pass to lego hub
def convert_matrix_to_string(matrix):
    return ':'.join([''.join(map(str, row)) for row in matrix])
 
 
# Manipulate the string directly
def toggle_light_by_index(matrix_str, row, col, brightness):
    index = row * 6 + col # 5 characters per row plus a colon
    matrix_str = matrix_str[:index] + brightness + matrix_str[index + 1:]
    return matrix_str

# for loop example

# range(start at, end before, increment)
for i in range(0,8,1):  # will count from 1-7
    print('the current index (i) is:', i)

print('\n')    
print('light matrix as a string:')
print(light_matrix_string)
print('\n')  
print('light matrix as a matrix:')
print (convert_light_string_to_array(light_matrix_string))

