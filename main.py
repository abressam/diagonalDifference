matriz = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

"""
matriz[0][0] = 11
matriz[1][1] = 5
matriz[2][2] = -12

matriz[0][2] = 11
matriz[1][1] = 5
matriz[2][0] = -12

"""

diagonal_1 = 0
diagonal_2 = 0

for row in range(3):
    diagonal_1 += matriz[row][column + row]
    diagonal_2 += matriz[row][3 - row - 1]

difference = diagonal_1 - diagonal_2

if difference > 0:
    print(f"Difference between {diagonal_1} and {diagonal_2} is {difference}")
else:
    difference *= -1
    print(f"Difference between {diagonal_1} and {diagonal_2} is {difference}")
