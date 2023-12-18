import numpy as np
import math

ABD = 0
FLX = 0
MEDROT = 0
EFLX = 0
WFLX = 0
WDEV = 0
WSUP = 0


L1 = 500
L2 = 400

T = [0,-ABD,90-FLX, MEDROT,-90-EFLX,WFLX,90-WDEV,-WSUP]
A = [-90,90,90, -90 , -90,90, 90, 0]
R = [0,0, 0, 0, -L2, 0, 0, 0]
D = [0, 0, 0, -L1, 0, 0, 0, 0]

T = [x*math.pi/180 for x in T]
A = [x*math.pi/180 for x in A]
#Do frame zero to 1, then move forwards!!


for i in range(len(T)-1):
#for i in range(1):
    DH_matrix = np.zeros((4, 4))
    t1 = T[i]
    t2 = T[i+1]
    a1 = A[i]
    a2 = A[i+1]
    d2 = D[i+1]

    DH_matrix[0, :] = [np.cos(t2), -np.sin(t2), 0, R[i]]
    DH_matrix[1, :] = [np.sin(t2) * np.cos(a1), np.cos(t2) * np.cos(a1), -np.sin(a1), -np.sin(a1) * d2]
    DH_matrix[2, :] = [np.sin(t2) * np.sin(a1), np.cos(t2) * np.sin(a1), np.cos(a1), np.cos(a1) * d2]
    DH_matrix[3, :] = [0, 0, 0, 1]

    DH_matrix.round(3,DH_matrix)
    if i != 0:
        #print("DH matrix no %d" % i)
        #print(DH_matrix)
        DH_matrix = np.dot(DH_prev,DH_matrix)
    if i == 3:
        Elbow_position = DH_matrix
    if i ==6:
        Hand_position = DH_matrix
    print("DH matrix origin to matrix no %d" % i)
    print(DH_matrix)
    DH_prev = DH_matrix
print("\n Elbow position matrix:")
print(Elbow_position)
print("\n Hand position matrix:")
print(Hand_position)
