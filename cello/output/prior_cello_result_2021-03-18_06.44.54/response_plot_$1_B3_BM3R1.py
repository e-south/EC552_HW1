import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([6.475589e-01,6.475589e-01,6.475589e-01,6.475589e-01,6.475588e-01,6.475587e-01,6.475586e-01,6.475585e-01,6.475583e-01,6.475581e-01,6.475577e-01,6.475572e-01,6.475566e-01,6.475557e-01,6.475545e-01,6.475529e-01,6.475506e-01,6.475475e-01,6.475433e-01,6.475376e-01,6.475297e-01,6.475190e-01,6.475044e-01,6.474844e-01,6.474570e-01,6.474197e-01,6.473686e-01,6.472989e-01,6.472036e-01,6.470735e-01,6.468958e-01,6.466531e-01,6.463218e-01,6.458696e-01,6.452528e-01,6.444119e-01,6.432664e-01,6.417079e-01,6.395905e-01,6.367201e-01,6.328396e-01,6.276139e-01,6.206126e-01,6.112973e-01,5.990160e-01,5.830191e-01,5.625070e-01,5.367285e-01,5.051377e-01,4.675975e-01,4.245854e-01,3.773161e-01,3.276895e-01,2.780272e-01,2.306572e-01,1.874971e-01,1.497836e-01,1.180151e-01,9.207003e-02,7.141141e-02,5.529165e-02,4.291102e-02,3.351730e-02,2.645552e-02,2.118364e-02,1.726841e-02,1.437193e-02,1.223525e-02,1.066239e-02,9.506360e-03,8.657673e-03,8.035140e-03,7.578777e-03,7.244380e-03,6.999434e-03,6.820054e-03,6.688714e-03,6.592560e-03,6.522172e-03,6.470650e-03,6.432939e-03,6.405338e-03,6.385137e-03,6.370352e-03,6.359532e-03,6.351613e-03,6.345817e-03,6.341576e-03,6.338472e-03,6.336200e-03,6.334537e-03,6.333321e-03,6.332430e-03,6.331778e-03,6.331302e-03,6.330953e-03,6.330697e-03,6.330510e-03,6.330373e-03,6.330273e-03,6.330200e-03,])
c = "#ee2f2b"

hi_x = np.array([1.369934e-01,])
hi_y = np.array([6.140359e-01,])
lo_x = np.array([9.597453e+00,4.524348e+00,5.210098e+00,])
lo_y = np.array([6.445070e-03,7.213246e-03,6.932659e-03,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$1 / B3_BM3R1")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$1_B3_BM3R1.png", bbox_inches='tight')
