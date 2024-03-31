def ray_casting(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n+1):
        p2x, p2y = polygon[i % n]
        if (p1y > y) != (p2y > y):
            if x < (p2x - p1x) * (y - p1y) / (p2y - p1y) + p1x:
                inside = not inside
        p1x, p1y = p2x, p2y
    return inside