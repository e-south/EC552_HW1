import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([4.563551e+00,4.563045e+00,4.562441e+00,4.561720e+00,4.560859e+00,4.559832e+00,4.558605e+00,4.557141e+00,4.555394e+00,4.553309e+00,4.550822e+00,4.547856e+00,4.544318e+00,4.540101e+00,4.535076e+00,4.529090e+00,4.521963e+00,4.513483e+00,4.503400e+00,4.491420e+00,4.477203e+00,4.460348e+00,4.440396e+00,4.416816e+00,4.389004e+00,4.356275e+00,4.317866e+00,4.272935e+00,4.220570e+00,4.159808e+00,4.089657e+00,4.009139e+00,3.917338e+00,3.813468e+00,3.696954e+00,3.567514e+00,3.425252e+00,3.270733e+00,3.105036e+00,2.929778e+00,2.747079e+00,2.559484e+00,2.369830e+00,2.181083e+00,1.996153e+00,1.817715e+00,1.648069e+00,1.489032e+00,1.341896e+00,1.207420e+00,1.085879e+00,9.771325e-01,8.807087e-01,7.958937e-01,7.218143e-01,6.575092e-01,6.019867e-01,5.542685e-01,5.134203e-01,4.785718e-01,4.489280e-01,4.237738e-01,4.024740e-01,3.844699e-01,3.692745e-01,3.564659e-01,3.456806e-01,3.366072e-01,3.289798e-01,3.225720e-01,3.171917e-01,3.126761e-01,3.088877e-01,3.057104e-01,3.030464e-01,3.008131e-01,2.989414e-01,2.973728e-01,2.960586e-01,2.949575e-01,2.940351e-01,2.932625e-01,2.926153e-01,2.920732e-01,2.916193e-01,2.912391e-01,2.909207e-01,2.906541e-01,2.904308e-01,2.902438e-01,2.900872e-01,2.899561e-01,2.898463e-01,2.897544e-01,2.896774e-01,2.896129e-01,2.895589e-01,2.895138e-01,2.894759e-01,2.894442e-01,2.894177e-01,])
c = "#6fcde1"

hi_x = np.array([4.000000e-02,4.000000e-02,])
hi_y = np.array([3.913302e+00,3.913302e+00,])
lo_x = np.array([1.967000e+00,1.967000e+00,])
lo_y = np.array([3.469182e-01,3.469182e-01,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$3 / F1_AmeR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$3_F1_AmeR.png", bbox_inches='tight')