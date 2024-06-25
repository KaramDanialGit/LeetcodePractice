"""
Given a height N, print the corresponding pascal triangle in the form:
   A
  B C
 D E F
"""


def pascal_triangle(height):
    triangle = [[1]]
    string_tri = [""] * height
    for i in range(1, height):
        temporary = [0] * (i + 1)
        for j in range(0, len(temporary)):
            if j - 1 >= 0:
                temporary[j] += triangle[i - 1][j - 1]
            if j < len(triangle[i - 1]):
                temporary[j] += triangle[i - 1][j]
        triangle.append(temporary)

    for i in range(height):
        string_tri[i] += " " * (height - i - 1)
        for x in triangle[i]:
            string_tri[i] += str(x) + " "

    return string_tri


for x in pascal_triangle(4):
    print(x)
