import numpy as np

marks = np.array(
    [72, 85, 49, 90, 67, 55, 38, 76, 81, 60, 45, 88]
)

print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Data type:", marks.dtype)

print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard deviation:", np.std(marks))

high_marks = marks[marks >= 60]
print("Marks >= 60:", high_marks)

below_50 = np.sum(marks < 50)
print("Number of marks below 50:", below_50)

matrix = marks.reshape(3, 4)
print("3 x 4 matrix:")
print(matrix)

row_sums = matrix.sum(axis=1)
print("Sum of each row:", row_sums)