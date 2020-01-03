def minTimeToVisitAllPoints(points) -> int:
    ma, a = [], 0
    for i in range(1 , len(points)):
        x = abs(points[i][0] - points[i - 1][0])
        y = abs(points[i][1] - points[i - 1][1])
        a += max(x, y)
    return a

    return sum([max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])) for i in
                range(1, len(points))])

points = [[1, 1], [3, 4], [-1, 0]]
print(minTimeToVisitAllPoints(points))

