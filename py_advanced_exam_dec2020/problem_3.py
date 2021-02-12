def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    def calc(r):
        l = []
        # for i in range(r):

        priv_row = r - 1
        for col in range(-1, r):
            if col == r - 1:
                a = triangle[priv_row][col]

            elif col < 0:
                a = triangle[priv_row][col + 1]
            else:
                a = triangle[priv_row][col] + triangle[priv_row][col + 1]
            l.append(a)

        return l


    for row in range(2, n):
        new_row = calc(row)
        triangle.append(new_row)
    return triangle
    pass
print(get_magic_triangle(5))
