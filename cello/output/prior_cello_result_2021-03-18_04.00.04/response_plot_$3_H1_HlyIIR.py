import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([2.056070e+00,2.056067e+00,2.056064e+00,2.056060e+00,2.056054e+00,2.056046e+00,2.056036e+00,2.056022e+00,2.056003e+00,2.055977e+00,2.055942e+00,2.055895e+00,2.055832e+00,2.055748e+00,2.055634e+00,2.055480e+00,2.055273e+00,2.054994e+00,2.054618e+00,2.054112e+00,2.053431e+00,2.052514e+00,2.051281e+00,2.049621e+00,2.047390e+00,2.044392e+00,2.040366e+00,2.034969e+00,2.027743e+00,2.018090e+00,2.005231e+00,1.988165e+00,1.965631e+00,1.936071e+00,1.897631e+00,1.848203e+00,1.785559e+00,1.707604e+00,1.612776e+00,1.500560e+00,1.372018e+00,1.230151e+00,1.079864e+00,9.274095e-01,7.794081e-01,6.417360e-01,5.186668e-01,4.125030e-01,3.237014e-01,2.513173e-01,1.935482e-01,1.482151e-01,1.131100e-01,8.620378e-02,6.574379e-02,5.027891e-02,3.864269e-02,2.991718e-02,2.339109e-02,1.851938e-02,1.488787e-02,1.218375e-02,1.017178e-02,8.675686e-03,7.563690e-03,6.737451e-03,6.123684e-03,5.667834e-03,5.329316e-03,5.077954e-03,4.891323e-03,4.752761e-03,4.649891e-03,4.573522e-03,4.516828e-03,4.474741e-03,4.443497e-03,4.420304e-03,4.403087e-03,4.390306e-03,4.380818e-03,4.373776e-03,4.368547e-03,4.364666e-03,4.361785e-03,4.359647e-03,4.358059e-03,4.356881e-03,4.356006e-03,4.355357e-03,4.354875e-03,4.354517e-03,4.354251e-03,4.354054e-03,4.353908e-03,4.353799e-03,4.353718e-03,4.353658e-03,4.353614e-03,4.353581e-03,4.353557e-03,])
c = "#8fc73e"

hi_x = np.array([3.000000e-02,3.000000e-02,])
hi_y = np.array([2.011571e+00,2.011571e+00,])
lo_x = np.array([2.234000e+00,2.234000e+00,])
lo_y = np.array([5.675030e-03,5.675030e-03,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$3 / H1_HlyIIR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$3_H1_HlyIIR.png", bbox_inches='tight')
