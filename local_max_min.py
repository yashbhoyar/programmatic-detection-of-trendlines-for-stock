from matplotlib import pyplot as plt
import pandas as pd
import numpy as np 
from findiff import FinDiff 


# Extracting Data for plotting
x=input("Enter  file name :")
x=x+".csv"
data = pd.read_csv(x)
rows,columns  =data.shape



h=np.array(data["Close"])   # h as a one dimensional function ie.f(h)

dx=1 #interval always fixed

d_dx=FinDiff(0,dx,1) #first differntial
d1=d_dx(h)

d2_dx=FinDiff(0,dx,2) #second differntial
d2=d2_dx(h)

def get_extrema_x(isMin):
  return [x for x in range(len(d1))
    if (d2[x] > 0 if isMin else d2[x] < 0) and
      (d1[x] == 0 or #slope is 0
        (x != len(d1) - 1 and #check next day
          (d1[x] > 0 and d1[x+1] < 0 and
           h[x] >= h[x+1] or
           d1[x] < 0 and d1[x+1] > 0 and
           h[x] <= h[x+1]) or
         x != 0 and #check prior day
          (d1[x-1] > 0 and d1[x] < 0 and
           h[x-1] < h[x] or
           d1[x-1] < 0 and d1[x] > 0 and
           h[x-1] > h[x])))]

minimaIdxs= get_extrema_x(True)
maximaIdxs = get_extrema_x(False)

def get_extrema_y(isMin):
  return [h[x] for x in range(len(d1))
    if (d2[x] > 0 if isMin else d2[x] < 0) and
      (d1[x] == 0 or #slope is 0
        (x != len(d1) - 1 and #check next day
          (d1[x] > 0 and d1[x+1] < 0 and
           h[x] >= h[x+1] or
           d1[x] < 0 and d1[x+1] > 0 and
           h[x] <= h[x+1]) or
         x != 0 and #check prior day
          (d1[x-1] > 0 and d1[x] < 0 and
           h[x-1] < h[x] or
           d1[x-1] < 0 and d1[x] > 0 and
           h[x-1] > h[x])))]

minimay= get_extrema_y(True)
maximay = get_extrema_y(False)



plt.style.use("ggplot")
plt.plot(minimaIdxs,minimay,marker="*",linestyle="none")
plt.plot(maximaIdxs,maximay,marker="*",linestyle="none")
plt.plot(np.arange(rows),h)
plt.show()

