class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5


def bruteForce(points):
    ''' the brute solution to find the smallest distance which takes O(n^2) time'''
    minDistance = float("inf")
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if distance(points[i], points[j]) < minDistance:
                minDistance = distance(points[i], points[j])
    return minDistance

def closestPairOfPoints(points):

    if len(points) <= 3:
        return bruteForce(points)

    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]

    leftMin = closestPairOfPoints(left)
    rightMin = closestPairOfPoints(right)
    minDistance = min(leftMin, rightMin)

    strip = []
    for point in points:
        if abs(point.x - points[mid].x) < minDistance:
            strip.append(point)

    strip.sort(key=lambda point: point.y)
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j].y - strip[i].y < minDistance:
                minDistance = distance(strip[i], strip[j])
            else:
                break

    return minDistance

def main():
    points = [Point(2, 3), Point(12, 30),
     Point(40, 50), Point(5, 1), 
     Point(12, 10), Point(3, 4)]
    points.sort(key=lambda point: point.x)
    print(closestPairOfPoints(points))
main()