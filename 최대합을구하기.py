def solution(triangle):
     answer = [[0 for x in range(0, len(triangle[y]))] for y in range(0, len(triangle))]
     answer[0][0] = triangle[0][0]
     for y in range(1, len(triangle)):
         for x in range(0, len(triangle[y])):
             if x == 0:
                 answer[y][x] = answer[y-1][x] + triangle[y][x]
             elif x == (len(triangle[y]) - 1):
                 answer[y][x] = answer[y-1][x-1] + triangle[y][x]
             else:
                 left = answer[y-1][x-1]
                 right = answer[y-1][x]
                 answer[y][x] = triangle[y][x] + (left if left > right else right)
     return max(answer[len(triangle)-1])

 def get_max(triangle, depth, pos):
     if len(triangle) == depth:
         return triangle[depth - 1][pos - 1]
     left = get_max(triangle, depth + 1, pos)
     right = get_max(triangle, depth + 1, pos + 1)
     return triangle[depth - 1][pos - 1] + (right if right > left else left)


 if __name__=="__main__":
     data = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
     print(solution(data))
     print(get_max(data, 1, 1))
