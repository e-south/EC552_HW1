import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([2.837857e+00,2.837857e+00,2.837857e+00,2.837857e+00,2.837856e+00,2.837856e+00,2.837856e+00,2.837855e+00,2.837854e+00,2.837852e+00,2.837850e+00,2.837848e+00,2.837844e+00,2.837838e+00,2.837831e+00,2.837820e+00,2.837806e+00,2.837786e+00,2.837757e+00,2.837718e+00,2.837663e+00,2.837587e+00,2.837481e+00,2.837333e+00,2.837126e+00,2.836839e+00,2.836439e+00,2.835881e+00,2.835105e+00,2.834024e+00,2.832520e+00,2.830427e+00,2.827516e+00,2.823470e+00,2.817853e+00,2.810065e+00,2.799288e+00,2.784411e+00,2.763950e+00,2.735947e+00,2.697878e+00,2.646599e+00,2.578369e+00,2.489057e+00,2.374616e+00,2.231920e+00,2.059921e+00,1.860869e+00,1.641075e+00,1.410609e+00,1.181694e+00,9.662313e-01,7.734604e-01,6.086634e-01,4.731730e-01,3.653069e-01,2.816131e-01,2.179612e-01,1.702847e-01,1.349806e-01,1.090591e-01,9.014502e-02,7.640684e-02,6.646113e-02,5.927821e-02,5.409961e-02,5.037071e-02,4.768808e-02,4.575942e-02,4.437345e-02,4.337781e-02,4.266275e-02,4.214928e-02,4.178061e-02,4.151594e-02,4.132594e-02,4.118954e-02,4.109164e-02,4.102136e-02,4.097092e-02,4.093471e-02,4.090872e-02,4.089007e-02,4.087668e-02,4.086707e-02,4.086017e-02,4.085522e-02,4.085166e-02,4.084911e-02,4.084728e-02,4.084597e-02,4.084503e-02,4.084435e-02,4.084386e-02,4.084351e-02,4.084326e-02,4.084308e-02,4.084295e-02,4.084286e-02,4.084280e-02,4.084275e-02,])
c = "#5455a4"

hi_x = np.array([4.000000e-02,4.000000e-02,])
hi_y = np.array([2.827374e+00,2.827374e+00,])
lo_x = np.array([1.967000e+00,1.967000e+00,])
lo_y = np.array([5.076897e-02,5.076897e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$2 / E1_BetI")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$2_E1_BetI.png", bbox_inches='tight')
