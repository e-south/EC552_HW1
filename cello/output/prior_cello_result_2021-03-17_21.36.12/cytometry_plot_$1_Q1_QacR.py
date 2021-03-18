import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / Q1_QacR")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.484351e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.684021e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.040783e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.559227e-03,0.000000e+00,0.000000e+00,0.000000e+00,9.858733e-03,0.000000e+00,0.000000e+00,1.025807e-02,0.000000e+00,0.000000e+00,9.783857e-03,0.000000e+00,1.028303e-02,0.000000e+00,1.045774e-02,0.000000e+00,1.018320e-02,0.000000e+00,1.073229e-02,1.040783e-02,0.000000e+00,1.108172e-02,1.080717e-02,1.105676e-02,0.000000e+00,1.065742e-02,1.055758e-02,1.173064e-02,1.120651e-02,1.165577e-02,2.263765e-02,1.123147e-02,1.070733e-02,2.256277e-02,1.025807e-02,2.293715e-02,1.040783e-02,2.136475e-02,2.036640e-02,2.166425e-02,2.148954e-02,2.151450e-02,2.176409e-02,3.167274e-02,2.066590e-02,3.119852e-02,2.890231e-02,2.842809e-02,2.810363e-02,3.491739e-02,2.575750e-02,3.199720e-02,3.000050e-02,2.715519e-02,3.204712e-02,2.867768e-02,2.523336e-02,2.308691e-02,1.964259e-02,2.016672e-02,1.914341e-02,1.405181e-02,1.287875e-02,1.018320e-02,6.888634e-03,7.637398e-03,4.068287e-03,2.970099e-03,2.321170e-03,1.247941e-03,8.236410e-04,6.738881e-04,2.745470e-04,4.991764e-05,4.991764e-05,2.495882e-05,0.000000e+00,2.495882e-05,2.495882e-05,0.000000e+00,2.495882e-05,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,0.000000e+00,2.495882e-05,2.495882e-05,0.000000e+00,0.000000e+00,2.495882e-05,2.495882e-05,0.000000e+00,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,3.104087e-03,0.000000e+00,0.000000e+00,3.447917e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,3.046756e-03,0.000000e+00,0.000000e+00,0.000000e+00,3.391161e-03,0.000000e+00,0.000000e+00,0.000000e+00,3.390745e-03,0.000000e+00,0.000000e+00,3.291838e-03,0.000000e+00,3.005805e-03,0.000000e+00,0.000000e+00,3.476295e-03,3.013995e-03,0.000000e+00,0.000000e+00,6.732188e-03,0.000000e+00,0.000000e+00,3.276082e-03,3.235082e-03,3.374364e-03,3.476295e-03,3.407125e-03,0.000000e+00,7.135589e-03,0.000000e+00,7.109403e-03,0.000000e+00,7.043305e-03,3.366174e-03,7.517186e-03,3.419539e-03,3.259701e-03,7.637626e-03,7.782393e-03,7.247838e-03,7.911710e-03,7.496887e-03,3.923108e-03,1.099964e-02,1.229944e-02,7.758974e-03,1.178003e-02,8.114051e-03,1.594339e-02,1.201201e-02,8.430702e-03,1.671779e-02,1.698565e-02,1.929239e-02,1.200475e-02,1.661213e-02,1.962186e-02,2.169871e-02,1.963802e-02,1.932725e-02,2.406798e-02,2.754618e-02,2.522087e-02,2.559114e-02,2.568320e-02,2.973053e-02,2.688220e-02,2.819953e-02,2.845398e-02,2.776244e-02,3.290679e-02,3.003661e-02,2.679082e-02,2.602072e-02,2.815876e-02,2.433814e-02,2.329325e-02,2.330214e-02,2.121938e-02,1.768115e-02,1.668666e-02,1.563864e-02,1.131528e-02,1.155650e-02,8.816877e-03,6.699955e-03,5.379806e-03,4.307444e-03,3.235082e-03,2.312800e-03,1.725054e-03,1.248628e-03,8.169608e-04,7.318270e-04,6.832614e-04,4.988050e-04,3.934835e-04,1.844564e-04,2.068356e-04,2.150258e-04,1.560785e-04,1.358908e-04,1.986454e-04,5.675583e-05,8.513374e-05,7.094479e-05,7.913499e-05,1.298921e-04,7.313624e-05,2.837791e-05,1.217019e-04,7.094479e-05,1.135117e-04,6.494603e-05,7.094479e-05,2.237916e-05,4.256687e-05,2.837791e-05,1.418896e-05,2.837791e-05,1.418896e-05,1.418896e-05,0.000000e+00,1.638041e-05,0.000000e+00,3.056937e-05,1.418896e-05,8.190204e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.418896e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.484351e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.684021e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.040783e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.559227e-03,0.000000e+00,0.000000e+00,0.000000e+00,9.858733e-03,0.000000e+00,0.000000e+00,1.025807e-02,0.000000e+00,0.000000e+00,9.783857e-03,0.000000e+00,1.028303e-02,0.000000e+00,1.045774e-02,0.000000e+00,1.018320e-02,0.000000e+00,1.073229e-02,1.040783e-02,0.000000e+00,1.108172e-02,1.080717e-02,1.105676e-02,0.000000e+00,1.065742e-02,1.055758e-02,1.173064e-02,1.120651e-02,1.165577e-02,2.263765e-02,1.123147e-02,1.070733e-02,2.256277e-02,1.025807e-02,2.293715e-02,1.040783e-02,2.136475e-02,2.036640e-02,2.166425e-02,2.148954e-02,2.151450e-02,2.176409e-02,3.167274e-02,2.066590e-02,3.119852e-02,2.890231e-02,2.842809e-02,2.810363e-02,3.491739e-02,2.575750e-02,3.199720e-02,3.000050e-02,2.715519e-02,3.204712e-02,2.867768e-02,2.523336e-02,2.308691e-02,1.964259e-02,2.016672e-02,1.914341e-02,1.405181e-02,1.287875e-02,1.018320e-02,6.888634e-03,7.637398e-03,4.068287e-03,2.970099e-03,2.321170e-03,1.247941e-03,8.236410e-04,6.738881e-04,2.745470e-04,4.991764e-05,4.991764e-05,2.495882e-05,0.000000e+00,2.495882e-05,2.495882e-05,0.000000e+00,2.495882e-05,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,0.000000e+00,2.495882e-05,2.495882e-05,0.000000e+00,0.000000e+00,2.495882e-05,2.495882e-05,0.000000e+00,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.495882e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.089964e-04,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.694803e-04,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.782371e-05,1.182717e-04,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.288936e-04,0.000000e+00,0.000000e+00,0.000000e+00,2.853341e-04,0.000000e+00,0.000000e+00,1.344030e-04,0.000000e+00,0.000000e+00,9.005107e-05,0.000000e+00,2.884256e-04,0.000000e+00,1.282199e-04,0.000000e+00,1.701539e-04,0.000000e+00,2.454210e-04,5.255589e-05,1.182717e-04,2.643671e-04,1.873557e-04,0.000000e+00,1.880294e-04,9.314260e-05,1.780812e-04,2.434001e-04,2.495831e-04,3.248502e-04,1.979776e-04,3.327775e-04,2.083228e-04,1.598088e-04,3.561624e-04,2.399116e-04,4.331737e-04,3.014653e-04,4.462134e-04,1.715012e-04,4.073709e-04,2.337286e-04,1.955598e-04,3.491855e-04,4.991662e-04,4.235022e-04,2.577871e-04,4.413777e-04,5.744333e-04,4.107392e-04,3.963522e-04,3.725704e-04,3.897722e-04,3.983731e-04,4.416544e-04,4.193401e-04,4.089950e-04,5.206867e-04,2.938148e-04,5.608765e-04,3.741944e-04,5.057826e-04,5.181487e-04,4.758178e-04,6.630534e-04,6.334855e-04,8.664203e-04,1.130667e-03,1.347747e-03,1.345330e-03,1.745207e-03,2.090904e-03,2.590503e-03,2.949120e-03,3.172900e-03,4.293066e-03,5.007725e-03,5.907839e-03,6.732962e-03,7.479847e-03,8.614399e-03,1.068098e-02,1.184867e-02,1.367237e-02,1.561183e-02,1.718076e-02,2.092201e-02,2.187215e-02,2.507281e-02,2.721023e-02,3.024887e-02,3.303361e-02,3.544779e-02,3.747221e-02,3.968961e-02,4.084272e-02,4.470237e-02,4.381054e-02,4.494416e-02,4.618435e-02,4.444663e-02,4.217834e-02,4.051525e-02,3.822905e-02,3.464836e-02,3.097853e-02,2.664172e-02,2.322687e-02,1.966270e-02,1.638859e-02,1.253763e-02,9.532443e-03,7.568594e-03,5.488218e-03,4.087903e-03,3.073993e-03,2.106179e-03,1.528931e-03,1.097105e-03,6.185085e-04,6.061424e-04,4.497019e-04,2.365434e-04,7.391980e-05,7.391980e-05,7.701132e-05,2.956792e-05,4.435188e-05,6.531889e-05,4.435188e-05,1.478396e-05,1.478396e-05,1.478396e-05,0.000000e+00,1.787548e-05,1.787548e-05,0.000000e+00,2.956792e-05,0.000000e+00,0.000000e+00,3.091523e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_Q1_QacR.png", bbox_inches='tight')