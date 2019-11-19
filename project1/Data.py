import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import os.path

def in_hull(p, hull):
    return hull.find_simplex(p)>=0

def Data(k,dim,n):
    if os.path.exists("data" + str(k)+"_"+str(dim)+"_"+str(n)+ ".npy"):
        data = np.load("data" + str(k)+"_"+str(dim)+"_"+str(n) + ".npy")
        ground_truth = data[0:k]
        shuffled_data = np.random.permutation(data)
        return ground_truth,shuffled_data
    data = []
    data_write = np.zeros((n,dim))
    radius = np.random.randint(0,10)
    rad = np.full(k,radius)
    rad = np.square(rad)
    sum = np.zeros(k)
    count= k
    for i in range(dim-1):
        data.append(np.random.uniform(-10,10,(k)))
        sum+=np.square(data[i])
    last_col = rad-sum
    last_col = np.sqrt(np.abs(last_col))
    data.append(last_col)
    data = np.array(data).T
    hull = Delaunay(data)
    for i in range(k):
        data_write[i] = data[i]
    while(count!=n):
        point = np.random.uniform(-5,5,(dim))
        val = in_hull(point,hull)
        if(val):
            data_write[count] = point
            count+=1
    np.save("data" + str(k)+"_"+str(dim)+"_"+str(n), data_write)
    ground_truth = data
    shuffled_data = np.random.permutation(data_write)
    return ground_truth,shuffled_data
