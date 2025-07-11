# 2D dimensional keypad
# cannot use set datatype as it is unordered.whereas, list is ordered but changeable and duplicates can be used

num_pad  = ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()