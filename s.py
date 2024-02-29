# s = 'BBWWB'
# print(s.find("B"))
# print(s.rfind("B"))
# print(s.index("B"))

def distance_squared(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def area_of_square(x1, y1, x2, y2, x3, y3, x4, y4):
    side_length_squared = min(distance_squared(x1, y1, x2, y2),
                              distance_squared(x1, y1, x3, y3),
                              distance_squared(x1, y1, x4, y4),
                              distance_squared(x2, y2, x3, y3),
                              distance_squared(x2, y2, x4, y4),
                              distance_squared(x3, y3, x4, y4))
    return side_length_squared

t = int(input())
for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    
    area = area_of_square(x1, y1, x2, y2, x3, y3, x4, y4)
    print(area)
