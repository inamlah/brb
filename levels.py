
import numpy as np

def experiment_levels(rotor,odd):
    E_odd=[0]
    if rotor==r'$^{168}$Er':
        # please write the energies scales
        E_rot=79.804
        E_vib=821.1685
        # the low lying levels of the rotor
        E_r=np.array(       [ 0       , 79.804  ,264.0888,548.7470,928.3029,1396.826 ,1947.3   ,2571.9   , 3259.5])
        error_r_ex=np.array([0.0000001, 0.001   ,0.0014  ,0.002   ,0.0025  ,0.005    ,0.5      ,0.5      ,1      ])

    if rotor==r'$^{238}$Pu':
        # please write the energies scales
        E_rot=44.065
        E_vib=605.18
        # the low lying levels of the rotor
        E_r=np.array(       [ 0       ,44.065   ,145.936,303.36 ,512.55 ,771.9  ,1077.7 ,1426.4 ,1815.5 ,2241.7 ,2702.3,3195.4,3717.1,4263.7,4833.3,5426.5])
        error_r_ex=np.array([0.015, 0.015   ,0.021  ,0.06   ,0.15   ,0.5    ,0.5    ,0.6    ,0.5    ,0.6    ,0.8   ,0.8   ,  1   ,1.1   ,1.3   , 0.9])

    if rotor==r'$^{234}$U':
        # please write the energies scales
        E_rot=43.4981
        E_vib=926.720
        E_r=np.array(       [ 0       ,43.4981  ,143.352,296.072,497.04 ,741.2  ,1023.8 ,1340.5,1687.8,2062.8 ,2464.0,2889.5,3338.5,3807.5,4296.5,4807])
        error_r_ex=np.array([0.001, 0.001   ,0.004  ,0.004  ,0.03   ,0.5    ,0.7    ,1.2   ,1.6   ,1.7    ,1.8   ,1.8   ,2.1   ,2.3   ,2.5   , 1])

    if rotor==r'$^{182}$W':
        # please write the energies scales
        E_rot=100.10598
        E_vib=1221.4001
        # the low lying levels of the rotor
        E_r=np.array( [            0,100.10598,329.4268,680.42,1144.32,1711.99,2372.59,3112.89,3910.09,4690.89,5428.6])
        error_r_ex=np.array([7.0E-5, 7.0E-5,6.0E-4  ,0.05  ,0.12   ,0.14   ,0.17   ,0.2    ,0.22   ,0.25   ,0.4])

    if rotor==r'$^{100}$Ru':
         # please write the energies scales
        E_rot=539.510
        E_vib=1362.166 
        # the low lying levels of the rotor
        E_r=np.array(       [ 0     , 539.510,1226.465,2075.674,3060.068,4235.854])
        error_r_ex=np.array([0.01, 0.01   ,0.01    ,0.012   ,0.015   ,0.024   ])

    if rotor ==r'$^{166}$Er':
        # please write the energies scales
        E_rot=80
        E_vib=785
        # the low lying levels of the rotor
        E_r=np.array([ 0       , 80.5776,264.990,545.454,911.208,1349.53,1846.53,2389.33, 2967.3])
        error_r_ex=np.array([0.002, 0.002  ,0.003  ,0.004  ,0.006  ,0.07   ,0.12   ,0.16   , 0.6])
        
    if odd==r'$^{167}$Tm':
        E_sp=470
        # the low lying levels of the odd nucleus 
        E_odd= np.array(      [0.     ,10.4   ,116.575  ,142.424 ,326.464 ,370.996,622.044 ,689.131 ,993.553,1086.511,1429.49,1549.97,1915.33,2065.53,2440.40,2620.20])
        error_odd_ex=np.array([0.019, 0.019  ,0.018   ,0.02    ,0.023   ,0.022  ,0.023   ,0.024   , 0.025 ,0.025   ,0.04   ,0.04   ,0.05   ,0.15   ,0.07   ,0.13])
        #error on the first level is not avialable
        
    if odd==r'$^{167}$Er':
        E_sp=545
        # the low lying levels of the odd nucleus
        E_odd= np.array(      [207.801,264.874,281.574,413.272,441.979 ,645.21  ,683.31  ,954.53  ,998.73 ,1336.9 ,1379.5 ,1782.2 ,1816.5 ,2285.2,2305.5 ,2833.3, 2842.5 ,3426.5 ])
        error_odd_ex=np.array([0.005  , 0.006 ,0.006  ,0.007  ,0.012   ,0.14    ,0.15    ,0.25    , 0.21  ,0.4    ,0.9    ,0.9    ,1.3    ,1.4   ,1.7    ,2.4   ,   2    ,2.2])# one level missing in the signiture term 35/2-
        error_odd_ex=error_odd_ex[:-2]
        E_odd=E_odd[:-2]
               
    if odd==r'$^{99}$Tc':
        E_sp=529
        # the low lying levels of the odd nucleus 
        E_odd= np.array(      [142.6836  ,509.096,612.37 ,986.19,1176.47,1604.43,1747.46 ,2222.95,2330.05,2646.85,2785.16,3129.71,3376.75,3883.83,4203.6 ,4785.6,5341.1 ])
        error_odd_ex=np.array([0.0011    ,0.01   ,0.03   ,0.04  ,0.04   ,0.1    ,0.08    ,0.09   , 0.08  ,0.09   ,0.11   ,0.13   ,0.13   ,0.21   ,0.3    ,0.3   ,   0.3 ])
        error_odd_ex=error_odd_ex[:-1]
        E_odd=E_odd[:-1]
        
    if odd==r'$^{183}$W':
        E_sp=209
        # the low lying levels of the odd nucleus 
        E_odd= np.array(      [0.     ,46.4838,99.0791 ,207.0114,308.9466,475.05  ,631.11  ,849.94  ,1061.99,1327.67,1595.29,1900.87,2221.79,2559.83,2929.89 ,3290.34,3706.39,4042.1])
        error_odd_ex=np.array([5.0E-4 ,5.0E-4 ,9.0E-4  ,0.0014  ,0.002   ,0.06    ,0.08    ,0.09    , 0.11  ,0.11   ,0.15   ,0.15   ,0.18   ,0.14   ,0.21    ,0.17   ,   0.23,0.3 ])
        #error on the first level is not avialable
        
    if odd==r'$^{235}$U':
        E_sp=393
        # the low lying levels of the odd nucleus
        E_odd= np.array(      [0.0760 ,13.0339,51.6968 ,81.724  ,150.356 ,197.087 ,294.557 ,357.22  ,482.00 ,559.34 ,710.02 ,800.58 ,975.94 ,1078.03,1276.84,1389.22,1610.04,1731.65,1973.09,2103.36,2363.80,2502.5,2780.2 ,2927.9 ,3220.6 ,3683.5])
        error_odd_ex=np.array([4.0E-4 ,0.0021 ,0.0011  ,0.004   ,0.016   ,0.015   ,0.016   ,0.04    , 0.04  ,0.05   ,0.05   ,0.06   ,0.07   ,0.07   ,0.08   ,0.09   ,   0.1 ,0.1    ,0.12   ,0.13   ,0.18   ,0.9   ,0.3    ,0.9    ,0.3    ,0.3 ])
        error_odd_ex=error_odd_ex[:-2]
        E_odd=E_odd[:-2]
    
    if odd==r'$^{239}$Pu':
        E_sp=752
        # the low lying levels of the odd nucleus
        E_odd= np.array(      [0.0    ,7.861  ,57.275  ,75.705  ,163.76  ,192.8   ,318.5   ,358.1   ,519.3  ,570.6  ,764.6  ,828.0  ,1052.9 ,1127.6 ,1381.1 ,1467.3 ,1748.2 ,1846.3 ,2151.8 ,2262.0 ,2589.4 ,2712.8 ,3059.7 ,3196.1 ,3558.2 ,3713.0 ,4087.1,4256])
        error_odd_ex=np.array([0.002  ,0.002  ,0.002   ,0.003   ,0.03    ,1.      ,0.7     ,0.1     , 0.6   ,0.7    ,0.6    ,0.7    ,0.3    ,0.7    ,0.7    ,0.8    ,  0.7  ,0.8    ,0.7    ,0.8    ,0.8    ,0.8    ,0.8    ,0.9    ,0.9    ,2.4    , 2.4  ,3 ])
        #error on the first level is not avialable
        
    if odd==r'$^{169}$Tm':
        E_sp=570
        # the low lying levels of the odd nucleus
        E_odd= np.array(      [0      ,8.41017,118.18945,138.93315,332.116,367.67  , 637.08  ,691.24  ,1027.85,1104.18,1497.8 ])
        error_odd_ex=np.array([1.1E-4 ,1.1E-4 ,1.1E-4   ,1.2E-4   ,0.011  ,0.05    ,0.13     ,0.16    , 0.16  ,0.25   ,0.4    ])
        error_odd_ex=error_odd_ex[:-1]
        E_odd=E_odd[:-1]
        #error on the first level is not avialable
        
    if odd==r'$^{169}$Er':
        E_sp=562
        # the low lying levels of the odd nucleusE_1= np.array([['1/2-' , '5/2-' , '9/2-' , '13/2-','17/2-','21/2-','25/2-','29/2-','33/2-','37/2-','41/2-']\
        E_odd=np.array(       [0      ,64.550, 74.59  , 224.13 ,242.00  ,475.1   ,501.0   ,813.1   ,848.0  ,1237.1 ,1280.0 ,1741.1 ,  1793.0,2324.1,2383.0 ,2979.1 ,3045.0 ,3701,3773   ,4549])
        error_odd_ex=np.array([0.02 ,0.02  ,0.06    ,0.08    ,0.12    ,  1.     ,1.     ,1.5     , 1.5   ,1.8    ,1.8    ,2      ,  2     ,2.3   ,2.3    ,2.5    ,   2.5 ,3   ,3.     ,3   ])
        error_odd_ex=error_odd_ex[:-2]
        E_odd=E_odd[:-2]
        #error on the first level is not avialable
        
    
    if rotor==r'$^{152}$Gd' and odd==r'$^{153}$Gd':
        # energies scales
        E_rot = 344.3
        E_vib = 615.4
        E_sp = 109.8
        
        # low lying levels of the rotor
        E_r = np.array([0, 344.3, 755.4, 1227.4, 1746.8, 2299.5, 2883.5, 3498.8, 4141.9])
        error_r_ex = 0.005 * E_r
        # low lying levels of the odd nucleus
        data = np.array([[3/2, 0, 0],
                         [5/2, 41.6, 0.0004],
                         [7/2, 93.3, 0.0006],
                         [9/2, 168.4, 0.6],
                         [13/2, 363.4, 0.011]])
        
    if rotor==r'$^{154}$Gd' and odd==r'$^{155}$Gd':
        # energies scales
        E_rot = 123.1
        E_vib = 680.7
        E_sp = 287.0041
        
        # low lying levels of the rotor
        E_r = np.array([0, 123.1, 371, 717.7, 1144.4, 1637.1, 2184.7, 2777.3, 3404.5])  
        error_r_ex = 0.005 * E_r
        # low lying levels of the odd nucleus
        data = np.array([[3/2, 0, 0],
                         [5/2, 60, 0.0006],
                         [7/2, 146.1, 0.0007],
                         [9/2, 251.7, 0.001],
                         [11/2, 392.3, 0.004],
                         [13/2, 534.3, 0.1],
                         [15/2, 729.6, 0.5],
                         [17/2, 896.9, 0.6],
                         [19/2, 1142.3, 0.8],
                         [21/2, 1326.5, 0.7],
                         [23/2, 1615.3, 1.3],
                         [25/2, 1809.4, 1.3],
                         [27/2, 2136.0, 1.6],
                         [29/2, 2331.9, 1.6],
                         [31/2, 2702.2, 1.9],
                         [33/2, 2883.7, 1.9],])
            
    if rotor==r'$^{156}$Gd' and odd==r'$^{157}$Gd':
        # energies scales
        E_rot = 89
        E_vib = 1049.5
        E_sp = 426.5
        
        # low lying levels of the rotor
        E_r = np.array([0, 89, 288.2, 584.7, 965.1, 1416.1, 1924.5, 2475.8, 3059.5])
        error_r_ex = 0.005 * E_r
        # low lying levels of the odd nucleus
        data = np.array([[3/2, 0, 0],
                         [5/2, 54.5, 0.006],
                         [7/2, 131.5, 0.009],
                         [9/2, 227, 0.019],
                         [11/2, 347.1, 0.06],
                         [13/2, 478.6, 0.04],
                         [15/2, 640.3, 0.08],
                         [17/2, 801.3, 0.09],
                         [19/2, 1002.5, 0.12],
                         [21/2, 1185.6, 0.13],
                         [23/2, 1423.9, 0.8],
                         [25/2, 1623.1, 0.9]])
        
    if rotor==r'$^{158}$Gd' and odd==r'$^{159}$Gd':
        # energies scales
        E_rot = 79.5
        E_vib = 1187.1
        E_sp = 146.3
        
        # low lying levels of the rotor
        E_r = np.array([0, 79.5, 261.5, 539, 904.1, 1349.5, 1865])
        error_r_ex = 0.005 * E_r
        # low lying levels of the odd nucleus
        data = np.array([[3/2, 0, 0],
                         [5/2, 50.6, 0.009],
                         [7/2, 121.9, 0.024],
                         [9/2, 212.6, 0.6],
                         [11/2, 324.9, 0.5]])
        
    if rotor==r'$^{158}$Dy' and odd==r'$^{159}$Dy':
        # energies scales
        E_rot = 98.8
        E_vib = 946.3
        E_sp = 309.6
        
        # low lying levels of the rotor
        E_r = np.array([0, 98.9, 317.1, 637.7, 1043.9, 1520, 2048.8, 2612.2, 3190.3])
        error_r_ex = 0.005 * E_r
        # low lying levels of the odd nucleus
        data = np.array([[3/2, 0, 0],
                         [5/2, 56.6, 0.006],
                         [7/2, 136.4, 0.006],
                         [9/2, 235.9, 0.01],
                         [11/2, 361.1, 0.14],
                         [13/2, 497.6, 0.14],
                         [15/2, 666.9, 0.3],
                         [17/2, 832, 0.15],
                         [19/2, 1041.6, 0.17],
                         [21/2, 1227.9, 0.18],
                         [23/2, 1470.9, 0.21],
                         [25/2, 1673, 0.23],
                         [27/2, 1941, 0.3],
                         [29/2, 2158.4, 0.3],
                         [31/2, 2445.9, 0.4],
                         [33/2, 2682.6, 0.5],
                         [35/2, 2986.1, 0.4],
                         [37/2, 3251.2, 0.7],
                         [39/2, 3568.4, 0.5],
                         [41/2, 3869.7, 0.9],
                         [43/2, 4201.7, 0.6],
                         [45/2, 4540.7, 1.0],
                         [47/2, 4889.7, 0.7],
                         [49/2, 5264.1, 1.1],
                         [51/2, 5632.5, 0.6],
                         [53/2, 6038.7, 1.2],
                         [55/2, 6427.0, 0.6],
                         [57/2, 6861.8, 1.2]])
        
    if odd == r'$^{153}$Gd' or odd == r'$^{155}$Gd' or odd == r'$^{157}$Gd' or odd == r'$^{159}$Gd' or odd == r'$^{159}$Dy':
        E_odd = data[:,1]
        error_odd_ex = data[:,2]    
        
    I_r=np.arange(0,2*len(E_r),2)
    I_odd=np.arange(1/2,len(E_odd),1)
    
    if odd == r'$^{153}$Gd' or odd == r'$^{155}$Gd' or odd == r'$^{157}$Gd' or odd == r'$^{159}$Gd' or odd == r'$^{159}$Dy':
        I_odd = data[:,0]
        
    if odd==r'$^{167}$Er_7/2':
        E_sp=810.5
        E_odd=np.array([0, 79.3221, 177.970, 294.953, 434.447, 587.375, 772.687, 954.99, 1194.20, 1393.9, 1698.6, 1901.9, 2283.3, 2476.9, 2946.3, 3118.9])
        error_odd_ex=np.array([0.0013, 0.0013, 0.007, 0.008, 0.01, 0.011, 0.014, 0.25, 0.1, 0.6, 0.8, 0.9, 1, 1.4, 1.5, 1.7])
        I_odd=np.array([ 7/2, 9/2, 11/2, 13/2, 15/2, 17/2, 19/2, 21/2, 23/2, 25/2, 27/2, 29/2, 31/2, 33/2, 35/2, 37/2])
        #error on the first level is not avialable
        
    if odd==r'$^{167}$Er_3/2':
        E_sp=531.1-810.5
        E_odd=np.array(       [531.54, 573.76, 640.25, 711.11, 790.97, 878.4])
        error_odd_ex=np.array([0.04,   0.05,   0.1,    0.12,   0.2,    0.3])
        I_odd=np.array([3/2, 5/2, 7/2, 9/2,11/2,13/2])

        
    if odd==r'$^{167}$Er_5/2':
        E_sp=667.9-346.6
        E_odd=np.array(       [346.554, 430.028, 535.80, 662.48, 812.0, 979.8, 1165.9, 1368.8])
        error_odd_ex=np.array([0.015,   0.015,   0.09,    0.24,  0.7,   0.8,      0.9,   1.1 ])
        I_odd=np.array([5/2, 7/2, 9/2, 11/2,13/2, 15/2, 17/2, 19/2])
        
    if odd==r'$^{235}$U_7/2':
        E_sp=633.092
        E_odd=np.array([0, 46.103, 103.903, 171.464 , 250.014, 339.976, 439.39, 551.17, 671.94, 805.65, 945.58, 1100.98, 1258.08, 1434.30, 1606.32, 1802.23, 1986.91, 2201.00, 2395.90, 2626.81, 2829.97, 3075.98, 3286.77, 3547.6, 3764.3, 4040.7])
        error_odd_ex=np.array([0.008, 0.008, 0.008, 0.013, 0.021, 0.024, 0.03,   0.04,   0.04,     0.06, 0.05,   0.06,     0.06,   0.06,     0.06,    0.06,   0.06,  0.07,   0.08,    0.09,    0.12,     0.17,   0.17,    0.8,   0.6,  1.3])
        I_odd=np.array([ 7/2, 9/2, 11/2, 13/2, 15/2, 17/2, 19/2,21/2, 23/2, 25/2, 27/2, 29/2, 31/2, 33/2,35/2, 37/2, 39/2, 41/2,43/2, 45/2, 47/2, 49/2,51/2, 53/2, 55/2, 57/2])
        #error on the first level is not avialable

        
    if odd==r'$^{235}$U_5/2':
        E_sp=332.845-129.2995
        E_odd=np.array([129.2995, 171.358, 225.382, 291.135, 368.9, 456.84, 557.2, 666.69, 787.8, 916.87, 1057.4, 1204.16, 1362.5, 1525.15, 1700.1, 1877.55, 2067.4, 2258.69, 2462.7, 2666.2, 2883.7, 3098.3])
        error_odd_ex=np.array([0.001, 0.005, 0.007, 0.019,   0.3,   0.07,   0.3,      0.1,   0.3,   0.13,   0.3 ,   0.15,    0.3,    0.17,    0.3,    0.2,      0.3,     0.24,    0.3,    0.7,    0.4,     0.7])
        I_odd=np.array([ 5/2, 7/2, 9/2, 11/2, 13/2, 15/2, 17/2, 19/2, 21/2, 23/2, 25/2, 27/2, 29/2, 31/2, 33/2, 35/2, 37/2, 39/2, 41/2, 43/2, 45/2, 47/2])
        
    return E_rot,E_vib,E_sp,E_r,error_r_ex,I_r,E_odd,error_odd_ex,I_odd


def Slope(E_odd,I_odd,E,A,skip,skipa):
    # Calculate the average of the absolute value of the defference between theory and experiment
    r=np.sqrt((E_odd-E)**2)

    Ia=(I_odd[0::2]+I_odd[1::2])/2
    ra=(r[0::2]+r[1::2])/2

    # find the slope
    slope, intercept = np.polyfit(np.log(I_odd[skip:]), np.log(r[skip:]), 1)
    slopea, intercept = np.polyfit(np.log(Ia[skipa:]), np.log(ra[skipa:]), 1)
    
    return slope,slopea,r,Ia,ra

def E_r_LO_(E_r,I_r):
    # First 2+ rotational energy level for the rotor
    E_2=E_r[1]

    # First 4+ rotational energy level for the rotor
    E_4= E_r[2]

    # The LEC for the rotor at LO Fitting according to E(I)=A I(I+1)
    A_r_LO=E_2/6

    # The LEC's for the rotor at NLO Fitting according to E(I)=A I(I+1) + B I^2(I+1)^2
    A_r_NLO=(400/36*E_2-E_4)/(400/6-20)
    B_r_NLO=(E_2-6*A_r_NLO)/36
    
    # We calculte the Energy levels for the rotor
    E_r_LO=A_r_LO*I_r*(I_r+1)

    return A_r_LO,A_r_NLO,B_r_NLO,E_r_LO

