class Polygon:

    def __init__(self, points):
        self.points = points

    def show(self):
        print(self.points)

    def is_convex(self):
        n = len(self.points)
        for i in range(n):

            x1, y1 = self.points[i]
            x2, y2 = self.points[(i+1) % n]
            x3, y3 = self.points[(i+2) % n]

            cross = (x2-x1)*(y3-y2) - (y2-y1)*(x3-x2)
            if cross < 0:
                return False
        return True

class Pentagon(Polygon):
    pass

class Hexagon(Polygon):
    pass

def read_polygons(file):
    polygons = []
    with open(file) as f:
        for line in f:
            nums = list(map(int, line.split()))
            n = nums[0]
            coords = nums[1:]

            points = []
            for i in range(0, len(coords), 2):
                points.append((coords[i], coords[i+1]))
            if n == 5:
                polygons.append(Pentagon(points))
            elif n == 6:
                polygons.append(Hexagon(points))
            else:
                polygons.append(Polygon(points))
    return polygons


polygons = read_polygons("polygons.txt")

print("convex polygons:")

for p in polygons:
    if p.is_convex():
        p.show()