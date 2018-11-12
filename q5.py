#!/usr/bin/env python
import math
import pdb
import scipy.stats as stats

def dist(p1,p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def main():
    x0 = (12, 4)
    x1 = (5, 7)
    p0 = (10, 8)
    p1 = (6, 3)
    d0 = 3.9
    d1 = 4.5
    
    # Compute intersection points analagously to p 34 of
    # cs685-sensor-models.ppt. But have to account for rotation.
    
    # distance between cell towers
    a = dist(x1, x0)
    
    x = (a**2 + d0**2 - d1**2)/(2*a)

    # Use similar triangles to get p2
    p2 = (x1[0] + (x0[0] - x1[0]) * x/a,
          x0[1] + (x1[1] - x0[1]) * x/a)

    # angle between cell towers
    theta = math.atan2(x1[1] - x0[1], x0[0] - x1[0])

    # calculate y value from ppt
    y = math.sqrt(d0**2 - x**2)

    x_delta = y * math.sin(theta)
    y_delta = y * math.cos(theta)

    # Find intersection points
    int0 = (p2[0] - x_delta, p2[1] - y_delta)
    int1 = (p2[0] + x_delta, p2[1] + y_delta)

    # Find closest home distance
    home_dist = min(dist(p1,int0), dist(p1, int1))

    # Find closest Johnson distance
    jc_dist   = min(dist(p0,int0), dist(p0, int1))

    print("Home is {} distance from intersection of cell signals".format(home_dist))
    print("Johnson Center is {} distance from intersection of cell signals".format(jc_dist))
    if jc_dist < home_dist:
        print("Johnson Center is most likely before prior knowledge.")
    else:
        print("Home is most likely before prior knowledge")

    # Combine variances using formula 5.73 on p 330 of Siegwart
    var0 = 1.0
    var1 = 1.5
    var2 = var0 - var0**2/(var0 + var1)
    print("combined variance is {}".format(var2))

    norm = stats.norm(0, var2)
    p_jc   = norm.pdf(jc_dist) * 0.3
    p_home = norm.pdf(home_dist) * 0.7

    p_total = p_jc + p_home
    p_jc = p_jc/p_total
    p_home = p_home/p_total

    print("With prior knowledge, probability of being at Johnson Center is {}".format(p_jc))
    print("With prior knowledge, probability of being at Home is {}".format(p_home))

    return

if __name__=='__main__':
    main()
