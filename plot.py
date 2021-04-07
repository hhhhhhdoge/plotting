import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
fig = plt.figure(figsize=(12, 13))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
ax.axis[:].set_visible(True)
#ax.axis["x"] = ax.new_floating_axis(0,0)
#ax.axis["x"].set_axisline_style("->", size = 1.0)
#ax.axis["y"] = ax.new_floating_axis(1,0)
#ax.axis["y"].set_axisline_style("-|>", size = 1.0)
#ax.axis["x"].set_axis_direction("top")
#ax.axis["y"].set_axis_direction("right")
x=np.linspace(0, 1, 11)
y1=[]
y2=[]
plt.grid()
#平滑曲线
from scipy.interpolate import make_interp_spline
xnew = np.linspace(x.min(),x.max(),300)
power_smooth1 = make_interp_spline(x,y1)(xnew)
power_smooth2 = make_interp_spline(x,y2)(xnew)
plt.scatter(x, y1, c='black',marker='o')
plt.scatter(x, y2, c='black',marker='s')
plt.plot(xnew,power_smooth1, c='black')
plt.plot(xnew,power_smooth2, c='black')
plt.show()
#描点画直线
#plt.plot(x1, y1, c='black', markerfacecolor='black', marker='o')
#plt.plot(x2, y2, c='black', markerfacecolor='black', marker='s')
#plt.show()