import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / P2_PhlF")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,1.714446e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.770658e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.911186e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.545812e-02,0.000000e+00,0.000000e+00,0.000000e+00,1.798763e-02,0.000000e+00,0.000000e+00,1.611392e-02,0.000000e+00,0.000000e+00,1.794079e-02,0.000000e+00,1.681656e-02,0.000000e+00,1.634814e-02,0.000000e+00,1.644182e-02,0.000000e+00,1.733183e-02,1.728499e-02,0.000000e+00,1.517707e-02,1.644182e-02,1.723815e-02,1.714446e-02,1.728499e-02,1.676972e-02,1.508338e-02,1.728499e-02,1.578602e-02,1.405284e-02,1.531759e-02,3.129099e-02,1.644182e-02,2.735619e-02,1.592655e-02,2.969833e-02,2.829305e-02,2.655987e-02,2.351508e-02,2.571669e-02,2.267191e-02,3.255574e-02,2.103242e-02,2.937043e-02,2.838673e-02,1.728499e-02,3.358628e-02,2.225033e-02,1.962713e-02,2.342140e-02,2.112610e-02,1.817500e-02,1.878396e-02,1.133596e-02,1.367810e-02,1.058647e-02,1.100806e-02,7.588533e-03,6.230092e-03,5.012179e-03,4.075323e-03,2.716882e-03,2.295297e-03,1.311598e-03,7.963275e-04,7.963275e-04,6.557991e-04,5.152708e-04,4.684280e-04,3.278996e-04,4.684280e-04,4.684280e-04,1.873712e-04,1.873712e-04,2.342140e-04,1.405284e-04,3.278996e-04,4.684280e-05,2.342140e-04,4.684280e-05,0.000000e+00,1.405284e-04,9.368559e-05,1.405284e-04,9.368559e-05,9.368559e-05,0.000000e+00,0.000000e+00,4.684280e-05,1.405284e-04,9.368559e-05,1.873712e-04,1.405284e-04,1.405284e-04,9.368559e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,4.684280e-05,4.684280e-05,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,4.684280e-05,4.684280e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,1.714446e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.770658e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.911186e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.545812e-02,0.000000e+00,0.000000e+00,0.000000e+00,1.798763e-02,0.000000e+00,0.000000e+00,1.611392e-02,0.000000e+00,0.000000e+00,1.794079e-02,0.000000e+00,1.681656e-02,0.000000e+00,1.634814e-02,0.000000e+00,1.644182e-02,0.000000e+00,1.733183e-02,1.728499e-02,0.000000e+00,1.517707e-02,1.644182e-02,1.723815e-02,1.714446e-02,1.728499e-02,1.676972e-02,1.508338e-02,1.728499e-02,1.578602e-02,1.405284e-02,1.531759e-02,3.129099e-02,1.644182e-02,2.735619e-02,1.592655e-02,2.969833e-02,2.829305e-02,2.655987e-02,2.351508e-02,2.571669e-02,2.267191e-02,3.255574e-02,2.103242e-02,2.937043e-02,2.838673e-02,1.728499e-02,3.358628e-02,2.225033e-02,1.962713e-02,2.342140e-02,2.112610e-02,1.817500e-02,1.878396e-02,1.133596e-02,1.367810e-02,1.058647e-02,1.100806e-02,7.588533e-03,6.230092e-03,5.012179e-03,4.075323e-03,2.716882e-03,2.295297e-03,1.311598e-03,7.963275e-04,7.963275e-04,6.557991e-04,5.152708e-04,4.684280e-04,3.278996e-04,4.684280e-04,4.684280e-04,1.873712e-04,1.873712e-04,2.342140e-04,1.405284e-04,3.278996e-04,4.684280e-05,2.342140e-04,4.684280e-05,0.000000e+00,1.405284e-04,9.368559e-05,1.405284e-04,9.368559e-05,9.368559e-05,0.000000e+00,0.000000e+00,4.684280e-05,1.405284e-04,9.368559e-05,1.873712e-04,1.405284e-04,1.405284e-04,9.368559e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,4.684280e-05,4.684280e-05,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,4.684280e-05,4.684280e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,4.684280e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,1.764074e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.564318e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.583190e-02,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.718656e-02,0.000000e+00,0.000000e+00,0.000000e+00,1.723019e-02,0.000000e+00,0.000000e+00,1.800381e-02,0.000000e+00,0.000000e+00,1.608276e-02,0.000000e+00,1.815125e-02,0.000000e+00,1.745116e-02,0.000000e+00,1.785785e-02,0.000000e+00,1.754296e-02,1.669904e-02,0.000000e+00,1.531644e-02,1.753457e-02,1.630223e-02,1.663862e-02,1.646968e-02,1.591036e-02,1.625193e-02,1.600946e-02,1.630976e-02,1.554925e-02,1.540502e-02,3.017485e-02,1.631643e-02,2.976344e-02,1.416389e-02,2.845608e-02,2.885956e-02,2.661200e-02,2.748966e-02,2.399281e-02,2.391199e-02,3.254749e-02,2.044566e-02,2.898551e-02,2.758790e-02,1.664937e-02,3.151014e-02,2.147312e-02,1.947407e-02,2.350443e-02,1.997360e-02,1.767448e-02,1.873270e-02,1.259171e-02,1.320949e-02,9.720795e-03,9.343127e-03,7.208869e-03,7.405981e-03,5.421755e-03,4.406534e-03,3.121542e-03,2.094709e-03,2.385979e-03,1.605694e-03,1.222220e-03,9.294553e-04,5.689745e-04,5.352315e-04,3.785307e-04,5.451187e-04,4.494657e-04,3.134016e-04,3.834743e-04,2.671846e-04,1.607822e-04,2.680469e-04,3.892802e-04,2.828777e-04,7.995996e-05,2.218299e-04,4.148604e-04,1.459513e-04,1.311205e-04,1.616444e-04,1.715316e-04,2.276358e-04,5.524192e-05,5.524192e-05,9.565302e-05,1.764752e-04,4.943607e-06,8.576580e-05,4.041110e-05,1.261769e-04,7.093498e-05,8.082220e-05,1.162897e-04,8.082220e-05,7.587859e-05,4.535471e-05,4.041110e-05,8.082220e-05,4.943607e-06,9.887214e-06,7.587859e-05,1.483082e-05,0.000000e+00,3.546749e-05,4.041110e-05,3.546749e-05,4.943607e-06,9.887214e-06,0.000000e+00,3.546749e-05,3.546749e-05,0.000000e+00,4.041110e-05,4.943607e-06,7.587859e-05,0.000000e+00,0.000000e+00,0.000000e+00,3.546749e-05,0.000000e+00,9.887214e-06,4.041110e-05,0.000000e+00,4.943607e-06,4.943607e-06,4.943607e-06,0.000000e+00,9.887214e-06,0.000000e+00,3.546749e-05,0.000000e+00,3.546749e-05,0.000000e+00,4.943607e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,3.546749e-05,0.000000e+00,3.546749e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,4.943607e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,1.154596e-04,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.096448e-04,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.239727e-04,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.700728e-04,0.000000e+00,0.000000e+00,0.000000e+00,2.537601e-04,0.000000e+00,0.000000e+00,1.297875e-04,0.000000e+00,0.000000e+00,2.363157e-04,0.000000e+00,1.038300e-04,0.000000e+00,9.531689e-05,0.000000e+00,9.801516e-05,0.000000e+00,9.531689e-05,1.123430e-04,0.000000e+00,9.261862e-05,8.950209e-05,1.038300e-04,1.038300e-04,1.329040e-04,7.787248e-05,1.239727e-04,6.354459e-05,6.042806e-05,4.651844e-05,6.354459e-05,2.739028e-04,8.638555e-05,1.731894e-04,5.191498e-05,1.960303e-04,1.181579e-04,1.615598e-04,7.787248e-05,1.557450e-04,1.441153e-04,2.278026e-04,1.356023e-04,2.161730e-04,1.817024e-04,3.758710e-05,1.530467e-04,1.185761e-04,1.038300e-04,9.801516e-05,9.801516e-05,5.503152e-05,1.038300e-04,7.205767e-05,9.801516e-05,3.177230e-05,1.297875e-04,5.814805e-06,4.610018e-05,2.595749e-05,2.014269e-05,0.000000e+00,2.595749e-05,2.014269e-05,2.014269e-05,5.814805e-06,2.595749e-05,0.000000e+00,2.595749e-05,6.042806e-05,5.814805e-06,5.814805e-06,5.814805e-06,2.014269e-05,5.814805e-06,4.028537e-05,4.028537e-05,5.814805e-06,3.177230e-05,2.595749e-05,0.000000e+00,5.814805e-06,5.814805e-06,6.624287e-05,4.028537e-05,0.000000e+00,3.177230e-05,0.000000e+00,0.000000e+00,2.595749e-05,5.814805e-06,2.595749e-05,2.595749e-05,3.177230e-05,2.595749e-05,4.028537e-05,8.368728e-05,4.340191e-05,1.038300e-04,4.028537e-05,1.038300e-04,9.220036e-05,1.929138e-04,8.638555e-05,2.676697e-04,2.331992e-04,3.195847e-04,3.885259e-04,4.059703e-04,5.617152e-04,6.190268e-04,7.976127e-04,1.036627e-03,1.140038e-03,1.408126e-03,1.808700e-03,3.076246e-03,3.853298e-03,5.080558e-03,6.640706e-03,9.020052e-03,1.207015e-02,1.647148e-02,2.057216e-02,2.567784e-02,3.297501e-02,3.608437e-02,4.381370e-02,4.809068e-02,5.265016e-02,5.616902e-02,5.806293e-02,5.830054e-02,5.600990e-02,5.418836e-02,4.999575e-02,4.779495e-02,4.015205e-02,3.743647e-02,3.230228e-02,2.599438e-02,2.376884e-02,1.967579e-02,1.685676e-02,1.391380e-02,1.180812e-02,9.658401e-03,7.944329e-03,7.054286e-03,5.878293e-03,4.524132e-03,3.790671e-03,3.874965e-03,2.770005e-03,2.533271e-03,2.347197e-03,2.062083e-03,1.631180e-03,1.352299e-03,1.054719e-03,8.291962e-04,9.236766e-04,9.008357e-04,7.889109e-04,6.958740e-04,4.998437e-04,3.848024e-04,4.107598e-04,2.626915e-04,3.289343e-04,4.157381e-04,2.774376e-04,3.374474e-04,2.080782e-04,2.712045e-04,1.243909e-04,1.185761e-04,9.801516e-05,8.950209e-05,9.531689e-05,3.758710e-05,8.950209e-05,3.758710e-05,8.098901e-05,5.814805e-06,6.042806e-05,0.000000e+00,2.014269e-05,6.042806e-05,3.177230e-05,1.162961e-05,5.814805e-06,2.014269e-05,0.000000e+00,5.814805e-06,4.028537e-05,5.814805e-06,0.000000e+00,5.814805e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_P2_PhlF.png", bbox_inches='tight')
