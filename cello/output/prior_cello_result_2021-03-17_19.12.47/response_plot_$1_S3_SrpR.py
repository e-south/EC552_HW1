import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([3.055511e+00,3.055503e+00,3.055493e+00,3.055479e+00,3.055460e+00,3.055434e+00,3.055399e+00,3.055352e+00,3.055287e+00,3.055200e+00,3.055081e+00,3.054920e+00,3.054700e+00,3.054403e+00,3.053999e+00,3.053451e+00,3.052707e+00,3.051698e+00,3.050328e+00,3.048470e+00,3.045951e+00,3.042536e+00,3.037912e+00,3.031655e+00,3.023201e+00,3.011795e+00,2.996445e+00,2.975850e+00,2.948334e+00,2.911776e+00,2.863563e+00,2.800597e+00,2.719406e+00,2.616419e+00,2.488466e+00,2.333533e+00,2.151671e+00,1.945822e+00,1.722197e+00,1.489845e+00,1.259332e+00,1.040899e+00,8.427287e-01,6.699156e-01,5.243390e-01,4.052373e-01,3.101035e-01,2.355585e-01,1.780200e-01,1.341227e-01,1.009293e-01,7.599818e-02,5.736745e-02,4.349753e-02,3.320095e-02,2.557309e-02,1.993103e-02,1.576258e-02,1.268548e-02,1.041542e-02,8.741505e-03,7.507605e-03,6.598282e-03,5.928281e-03,5.434683e-03,5.071079e-03,4.803255e-03,4.605990e-03,4.460701e-03,4.353698e-03,4.274892e-03,4.216854e-03,4.174112e-03,4.142634e-03,4.119453e-03,4.102381e-03,4.089809e-03,4.080550e-03,4.073732e-03,4.068710e-03,4.065012e-03,4.062289e-03,4.060284e-03,4.058807e-03,4.057719e-03,4.056918e-03,4.056328e-03,4.055894e-03,4.055574e-03,4.055338e-03,4.055165e-03,4.055037e-03,4.054943e-03,4.054874e-03,4.054823e-03,4.054785e-03,4.054757e-03,4.054737e-03,4.054722e-03,4.054711e-03,4.054703e-03,])
c = "#6fcde1"

hi_x = np.array([4.523695e-02,])
hi_y = np.array([2.679082e+00,])
lo_x = np.array([9.235293e+00,7.128375e+00,2.152154e+00,])
lo_y = np.array([4.165476e-03,4.810330e-03,4.669508e-03,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$1 / S3_SrpR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$1_S3_SrpR.png", bbox_inches='tight')
