import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518354e+00,4.518353e+00,4.518353e+00,4.518352e+00,4.518351e+00,4.518349e+00,4.518347e+00,4.518342e+00,4.518334e+00,4.518321e+00,4.518300e+00,4.518265e+00,4.518207e+00,4.518112e+00,4.517956e+00,4.517699e+00,4.517276e+00,4.516581e+00,4.515439e+00,4.513560e+00,4.510473e+00,4.505404e+00,4.497089e+00,4.483479e+00,4.461269e+00,4.425210e+00,4.367154e+00,4.274918e+00,4.131445e+00,3.915447e+00,3.605747e+00,3.191404e+00,2.685578e+00,2.132801e+00,1.597247e+00,1.135612e+00,7.761130e-01,5.176615e-01,3.423447e-01,2.280594e-01,1.554794e-01,1.101472e-01,8.212754e-02,6.492032e-02,5.439508e-02,4.797269e-02,4.405963e-02,4.167763e-02,4.022843e-02,3.934703e-02,3.881109e-02,3.848523e-02,3.828713e-02,3.816670e-02,3.809349e-02,3.804899e-02,3.802194e-02,3.800549e-02,3.799550e-02,3.798942e-02,3.798573e-02,3.798348e-02,3.798212e-02,3.798129e-02,3.798078e-02,3.798048e-02,3.798029e-02,3.798018e-02,3.798011e-02,3.798006e-02,3.798004e-02,3.798002e-02,3.798001e-02,3.798001e-02,])
c = "#66bc46"

hi_x = np.array([2.000000e-02,2.000000e-02,])
hi_y = np.array([4.518354e+00,4.518354e+00,])
lo_x = np.array([4.200000e+00,4.200000e+00,])
lo_y = np.array([4.591158e-02,4.591158e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$2 / Q1_QacR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$2_Q1_QacR.png", bbox_inches='tight')