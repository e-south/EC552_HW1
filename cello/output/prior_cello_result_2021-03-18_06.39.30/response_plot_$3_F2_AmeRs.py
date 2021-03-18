import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([3.693389e+00,3.693212e+00,3.692996e+00,3.692731e+00,3.692408e+00,3.692014e+00,3.691532e+00,3.690944e+00,3.690225e+00,3.689348e+00,3.688276e+00,3.686968e+00,3.685371e+00,3.683421e+00,3.681042e+00,3.678140e+00,3.674601e+00,3.670286e+00,3.665028e+00,3.658625e+00,3.650832e+00,3.641357e+00,3.629848e+00,3.615886e+00,3.598974e+00,3.578528e+00,3.553863e+00,3.524192e+00,3.488612e+00,3.446114e+00,3.395590e+00,3.335856e+00,3.265695e+00,3.183917e+00,3.089450e+00,2.981449e+00,2.859425e+00,2.723386e+00,2.573959e+00,2.412485e+00,2.241038e+00,2.062377e+00,1.879789e+00,1.696864e+00,1.517221e+00,1.344222e+00,1.180736e+00,1.028970e+00,8.904003e-01,7.657805e-01,6.552232e-01,5.583210e-01,4.742839e-01,4.020721e-01,3.405109e-01,2.883829e-01,2.444944e-01,2.077208e-01,1.770329e-01,1.515098e-01,1.303417e-01,1.128264e-01,9.836147e-02,8.643461e-02,7.661341e-02,6.853485e-02,6.189562e-02,5.644328e-02,5.196832e-02,4.829736e-02,4.528716e-02,4.281959e-02,4.079740e-02,3.914057e-02,3.778333e-02,3.667167e-02,3.576127e-02,3.501577e-02,3.440535e-02,3.390557e-02,3.349640e-02,3.316142e-02,3.288719e-02,3.266271e-02,3.247894e-02,3.232852e-02,3.220539e-02,3.210460e-02,3.202210e-02,3.195457e-02,3.189930e-02,3.185405e-02,3.181702e-02,3.178671e-02,3.176189e-02,3.174159e-02,3.172496e-02,3.171136e-02,3.170022e-02,3.169111e-02,3.168365e-02,])
c = "#6fcde1"

hi_x = np.array([2.000000e-02,2.000000e-02,])
hi_y = np.array([3.553306e+00,3.553306e+00,])
lo_x = np.array([4.200000e+00,4.200000e+00,])
lo_y = np.array([3.998585e-02,3.998585e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$3 / F2_AmeRs")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$3_F2_AmeRs.png", bbox_inches='tight')
