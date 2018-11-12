#!/usr/bin/env python
import matplotlib.pyplot as plt
import pdb
import sys

def filter_t_plus_1(dt2, dx2, dz2):
    return ((dt2 + dx2) * dz2)/(dt2 + dx2 + dz2)

def main(dx2, dz2, dt2_init):
    ts  = [1.0]
    dt2 = [dt2_init]
    for t in range(1,1000):
        dt2.append(filter_t_plus_1(dt2[-1], dx2, dz2))
        ts.append(t)

    plt.plot(ts, dt2)
    plt.title("dx2={0}, dz2={1}, starting value of dt2={2}".format(dx2, dz2, dt2_init))
    plt.savefig('q3_dx2_{0}_dz2_{1}_dt2_init{2}.pdf'.format(dx2, dz2, dt2_init), dpi=600)

if __name__=='__main__':
    main(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    
