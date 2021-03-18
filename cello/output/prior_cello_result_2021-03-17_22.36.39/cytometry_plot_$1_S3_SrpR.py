import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / S3_SrpR")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,5.130376e-06,5.130376e-06,9.802763e-06,0.000000e+00,1.026075e-05,0.000000e+00,2.006351e-05,0.000000e+00,5.130376e-06,5.130376e-06,1.026075e-05,0.000000e+00,1.539113e-05,2.006351e-05,4.672387e-06,5.130376e-06,5.130376e-06,1.026075e-05,9.802763e-06,9.802763e-06,2.006351e-05,1.539113e-05,0.000000e+00,9.802763e-06,1.539113e-05,1.539113e-05,1.539113e-05,2.519389e-05,9.802763e-06,5.130376e-06,1.539113e-05,1.026075e-05,2.473590e-05,1.539113e-05,9.802763e-06,3.499665e-05,3.591263e-05,2.986628e-05,3.032427e-05,0.000000e+00,1.493314e-05,4.058502e-05,4.012703e-05,2.052150e-05,7.558167e-05,5.643413e-05,3.078225e-05,4.617338e-05,4.992979e-05,6.019054e-05,5.038778e-05,6.394695e-05,5.506017e-05,9.610317e-05,6.019054e-05,6.019054e-05,8.675840e-05,1.418186e-04,7.090928e-05,1.012336e-04,1.268854e-04,1.012336e-04,1.175407e-04,1.567517e-04,1.320158e-04,1.474069e-04,1.464910e-04,1.516213e-04,1.427345e-04,2.071395e-04,1.968787e-04,1.866180e-04,2.598172e-04,2.710864e-04,3.148774e-04,2.780488e-04,2.715444e-04,3.690216e-04,3.895431e-04,4.151950e-04,3.951314e-04,5.173445e-04,5.342021e-04,5.387820e-04,4.930666e-04,6.479863e-04,6.689658e-04,7.892544e-04,8.924124e-04,8.387262e-04,9.441742e-04,1.191441e-03,1.213794e-03,1.303851e-03,1.534718e-03,1.461884e-03,1.716205e-03,1.943774e-03,2.018440e-03,2.117749e-03,2.613656e-03,2.600647e-03,3.000724e-03,3.145383e-03,3.416927e-03,3.534102e-03,3.881960e-03,4.406266e-03,4.712534e-03,5.033366e-03,5.761972e-03,6.131178e-03,6.635421e-03,7.353401e-03,7.871939e-03,8.323690e-03,8.818315e-03,9.319538e-03,9.971095e-03,1.046527e-02,1.144023e-02,1.158929e-02,1.287399e-02,1.357420e-02,1.438389e-02,1.538167e-02,1.580135e-02,1.646876e-02,1.706343e-02,1.853266e-02,1.845817e-02,1.904817e-02,2.005529e-02,1.997853e-02,2.053691e-02,2.086206e-02,2.123155e-02,2.155403e-02,2.180726e-02,2.226288e-02,2.293900e-02,2.236028e-02,2.226803e-02,2.212055e-02,2.287107e-02,2.251387e-02,2.246678e-02,2.185930e-02,2.097514e-02,2.014658e-02,1.962346e-02,1.877787e-02,1.843441e-02,1.816846e-02,1.712350e-02,1.667276e-02,1.604072e-02,1.444112e-02,1.434200e-02,1.354366e-02,1.217090e-02,1.116588e-02,1.008977e-02,9.131658e-03,8.399653e-03,7.558808e-03,6.514303e-03,5.771851e-03,4.875030e-03,4.311045e-03,3.688429e-03,3.115557e-03,3.039976e-03,2.597107e-03,2.116402e-03,2.020114e-03,1.801062e-03,1.641835e-03,1.409775e-03,1.291406e-03,1.073363e-03,9.248552e-04,8.300335e-04,9.448262e-04,7.178962e-04,7.058035e-04,6.571551e-04,5.871618e-04,5.641654e-04,4.432338e-04,4.688857e-04,4.679697e-04,2.914275e-04,3.316470e-04,3.651772e-04,1.863450e-04,2.381992e-04,2.437876e-04,2.139213e-04,1.727858e-04,1.961478e-04,1.592267e-04,1.770002e-04,1.289024e-04,1.017840e-04,6.678739e-05,4.672387e-05,5.506017e-05,8.080455e-05,5.790060e-05,3.875306e-05,4.342545e-05,2.940829e-05,9.344774e-06,4.388344e-05,2.895030e-05,3.829507e-05,1.401716e-05,1.447515e-05,3.032427e-05,9.344774e-06,0.000000e+00,9.344774e-06,1.493314e-05,0.000000e+00,0.000000e+00,0.000000e+00,5.130376e-06,5.130376e-06,5.130376e-06,0.000000e+00,0.000000e+00,4.672387e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_S3_SrpR.png", bbox_inches='tight')