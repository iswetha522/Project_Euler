# write a python program to add two matrices
# m1 = [ [1,2,3],
#        [2,3,4],
#        [3,4,5]]

# m2 = [ [1,1,1],
#        [1,1,1],
#        [1,1,1]]

# add m1 + m2

# sum = [ [2,3,4],
#        [3,4,5],
#        [4,5,6]]

# for first_matrix_row_index in range(0, 3):
#     for first_matrix_column_index in range(0, 3):
#         for second_matrix_row_index in range(0, 3):
#             for second_matrix_column_index in range(0, 3):
#                 newly_created_list = [(m1[first_matrix_row_index][first_matrix_column_index]) +
#                 (m2[second_matrix_row_index][second_matrix_column_index])]
#                 m3.append(newly_created_list)
# print(m1[0][0])

# Matrix 1
m1 = [[1, 2, 3],[2, 3, 4],[3, 4, 5]]
print(f"First Matrix: {m1}")
# Matrix 2
m2 = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
print(f"Second Matrix: {m2}")
m3 = [[0,0,0],[0,0,0],[0,0,0]]
for row_index in range(0,3):
    for column_index in range(0,3):
        m3[row_index][column_index] = ((m1[row_index][column_index]) + 
        (m2[row_index][column_index]))

print(f"Sum of first and second matrix: {m3}")    