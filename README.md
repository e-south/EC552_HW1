# EC552_HW1
Genetic Circuit Design
# Template
A template repository for ECE552 Homework 1

This repository contains an input directory and an output directory. Part of your homework is plumbing these input files into celloapi2.

```
input
├── input_options
│   └── options.csv
├── input_sensor
│   ├── Bth
│   │   └── Bth1C1G1T1.input.json
│   ├── Eco
│   │   ├── Eco1C1G1T1.input.json
│   │   ├── Eco1C2G2T2.input.json
│   │   └── Eco2C1G3T1.input.json
│   └── SC
│       └── SC1C1G1T1.input.json
├── output_device
│   ├── Bth
│   │   └── Bth1C1G1T1.output.json
│   ├── Eco
│   │   ├── Eco1C1G1T1.output.json
│   │   ├── Eco1C2G2T2.output.json
│   │   └── Eco2C1G3T1.output.json
│   └── SC
│       └── SC1C1G1T1.output.json
├── ucf
│   ├── Bth
│   │   └── Bth1C1G1T1.UCF.json
│   ├── Eco
│   │   ├── Eco1C1G1T1.UCF.json
│   │   ├── Eco1C2G2T2.UCF.json
│   │   └── Eco2C1G3T1.UCF.json
│   └── SC
│       └── SC1C1G1T1.UCF.json
└── verilog_files
    ├── and.v
    ├── nand.v
    ├── struct.v
    └── xor.v

```

# Suggested Reading
1. Vaidyanathan, P., Der, B. S., Bhatia, S., Roehner, N., Silva, R., Voigt, C. A., & Dens- more, D. (2015). A Framework for Genetic Logic Synthesis. Proceedings of the IEEE, 103(11), 2196-2207.
(This Paper should help understand the basic framework, terms and defini- tions of Logic Synthesis applied for Genetic circuits. Specifically, Sections 1,2,3 as well as Fig 2 will be helpful)
2. Yaman, F., Bhatia, S., Adler, A., Densmore, D., & Beal, J. (2012). Automated selec- tion of synthetic biology parts for genetic regulatory networks. ACS synthetic biology, 1(8), 332-344.
(The Results section as well as Fig 5 will be useful)
3. Stanton, B. C., Nielsen, A. A., Tamsir, A., Clancy, K., Peterson, T., & Voigt, C. A. (2014). Genomic mining of prokaryotic repressors for orthogonal logic gates. Nature chemical biology, 10(2), 99-105.
