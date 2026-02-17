from math import sqrt
from sys import stdin

def dist(pair1,pair2):
    return sqrt((pair2[0]-pair1[0])**2 + (pair2[1]-pair1[1])**2)

def main():
    t = int(stdin.readline().strip())
    while t != 0:
        points = []
        for i in range(t):
            x, y = list(map(float,stdin.readline().split()))
            points.append((x,y))
        
        Px = sorted(points, key= lambda p: p[0]) # ordenamos por componenete x asc
        Py = sorted(points,key = lambda p: p[1] ) # ordenamos por componenete y asc
        ans = closest_pair(Px, Py)

        if ans >= 10000.0:
            print("INFINITY")
        else:
            print(f"{ans:.4f}")

        t = int(stdin.readline().strip())

def base_case_determination(points):
    min = float('inf')
    for i in range(len(points)):
        for j in range (i + 1, len(points)):
            d = dist(points[i], points[j])
            if d < min:
                min = d

    return min

def min_val_candidates(d, candidates):
    min_val = d
    n = len(candidates)
    for i in range(n):
        j = i + 1
        # El while se rompe solo cuando j se sale del rango O cuando la distancia vertical es muy grande.
        while j < n and (candidates[j][1] - candidates[i][1]) < min_val:
            d_new = dist(candidates[i], candidates[j])
            if d_new < min_val:
                min_val = d_new
            j += 1
            
    return min_val
    
def closest_pair(Px, Py):
    n = len(Px)
    dist_min_ans = 0
    # caso base
    if n <= 3 and n >= 1:
        dist_min_ans = base_case_determination(Px)
    # caso inductivo
    else: 
        mid = n//2
        mid_point = Px[mid]

        Px_l = Px[:mid]
        Px_r = Px[mid:]

        Py_l = []
        Py_r = []

        for i in range (len(Py)):
            if Py[i][0] < mid_point[0]: # Si está a la izquierda
                Py_l.append(Py[i])
            else:
                Py_r.append(Py[i])

        d_l = closest_pair(Px_l, Py_l)
        d_r = closest_pair(Px_r, Py_r)
        dist_min = min(d_l, d_r)
    
        candidates = []
        for i in range(len(Py)):
            if abs(Py[i][0] - mid_point[0]) < dist_min:
                candidates.append(Py[i])
        dist_min_ans = min_val_candidates(dist_min, candidates)
    
    return dist_min_ans

main()