import numpy as np
a= [1, 2]
b = [3, 4]
def dist(p1, p2):
    a = np.array(p1)
    b = np.array(p2)
    return np.linalg.norm(a-b)


def mid_point(p1, p2):
    mp = (int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))
    return mp

c = mid_point(a, b)
print(c)