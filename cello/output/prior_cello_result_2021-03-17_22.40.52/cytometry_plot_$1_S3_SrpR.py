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
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,4.688954e-06,4.688954e-06,9.804072e-06,0.000000e+00,9.377908e-06,0.000000e+00,1.918198e-05,0.000000e+00,4.688954e-06,4.688954e-06,9.377908e-06,0.000000e+00,1.406686e-05,1.918198e-05,5.115118e-06,4.688954e-06,4.688954e-06,9.377908e-06,9.804072e-06,9.804072e-06,1.918198e-05,1.406686e-05,0.000000e+00,9.804072e-06,1.406686e-05,1.406686e-05,1.406686e-05,2.387093e-05,9.804072e-06,4.688954e-06,1.406686e-05,9.377908e-06,2.429710e-05,1.406686e-05,9.804072e-06,3.367501e-05,3.282268e-05,2.898605e-05,2.855989e-05,0.000000e+00,1.449303e-05,3.793779e-05,3.836396e-05,1.875582e-05,7.161280e-05,5.157849e-05,2.813372e-05,4.220058e-05,4.816803e-05,5.754594e-05,4.774187e-05,6.351339e-05,5.285698e-05,9.036862e-05,5.754594e-05,5.754594e-05,8.013838e-05,1.329954e-04,6.649768e-05,9.505757e-05,1.185023e-04,9.505757e-05,1.082721e-04,1.474884e-04,1.231913e-04,1.372582e-04,1.381105e-04,1.427994e-04,1.321430e-04,1.952303e-04,1.858523e-04,1.764744e-04,2.408413e-04,2.587436e-04,2.936983e-04,2.617279e-04,2.583175e-04,3.474076e-04,3.661634e-04,3.896082e-04,3.704262e-04,4.838134e-04,5.059786e-04,5.017169e-04,4.590902e-04,6.082832e-04,6.266129e-04,7.323280e-04,8.350577e-04,7.809222e-04,8.815210e-04,1.115115e-03,1.132166e-03,1.218698e-03,1.429701e-03,1.355532e-03,1.601487e-03,1.806096e-03,1.878561e-03,1.965947e-03,2.431857e-03,2.425036e-03,2.781397e-03,2.921213e-03,3.179530e-03,3.297605e-03,3.607929e-03,4.094727e-03,4.405899e-03,4.694057e-03,5.369266e-03,5.735427e-03,6.203043e-03,6.878676e-03,7.389767e-03,7.830525e-03,8.307091e-03,8.796443e-03,9.391940e-03,9.916241e-03,1.087321e-02,1.103732e-02,1.228329e-02,1.293761e-02,1.372663e-02,1.474753e-02,1.517081e-02,1.582725e-02,1.641891e-02,1.790955e-02,1.780853e-02,1.839507e-02,1.937889e-02,1.942193e-02,1.994325e-02,2.034095e-02,2.078255e-02,2.105025e-02,2.142024e-02,2.201827e-02,2.276124e-02,2.228722e-02,2.230682e-02,2.230211e-02,2.318404e-02,2.291079e-02,2.291675e-02,2.243165e-02,2.168354e-02,2.090262e-02,2.039579e-02,1.962126e-02,1.933523e-02,1.917580e-02,1.810417e-02,1.767194e-02,1.708667e-02,1.540507e-02,1.533644e-02,1.448008e-02,1.307001e-02,1.197068e-02,1.083342e-02,9.803996e-03,9.018398e-03,8.116430e-03,6.997069e-03,6.183339e-03,5.229367e-03,4.609159e-03,3.948880e-03,3.318016e-03,3.246403e-03,2.768992e-03,2.251085e-03,2.141963e-03,1.910503e-03,1.746392e-03,1.508111e-03,1.362758e-03,1.139822e-03,9.846631e-04,8.836392e-04,9.944683e-04,7.608764e-04,7.532031e-04,6.943799e-04,6.270298e-04,5.916513e-04,4.676089e-04,4.910536e-04,4.919060e-04,3.060559e-04,3.537966e-04,3.793734e-04,1.956541e-04,2.514943e-04,2.557570e-04,2.267710e-04,1.798826e-04,2.054582e-04,1.641111e-04,1.854239e-04,1.355512e-04,1.040082e-04,7.033316e-05,5.115118e-05,5.285698e-05,8.567851e-05,5.967676e-05,3.964245e-05,4.475757e-05,2.941222e-05,1.023024e-05,4.433141e-05,2.983838e-05,4.006862e-05,1.534535e-05,1.491919e-05,2.855989e-05,1.023024e-05,0.000000e+00,1.023024e-05,1.449303e-05,0.000000e+00,0.000000e+00,0.000000e+00,4.688954e-06,4.688954e-06,4.688954e-06,0.000000e+00,0.000000e+00,5.115118e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_S3_SrpR.png", bbox_inches='tight')
