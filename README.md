# EC552_HW1
## Documentation
Our tool was designed to take a custom Eco2C1G3T1.input.json, recognize it’s available signal pairings, and then reference our catalogue of pairwise gate combinations (that were associated with previously successful CelloQuery() runs) to modify the custom input.

## Navigating our Modules
- main.py: provide an custom Eco2C1G3T1.input.json file, receive an initial CelloQuery() score, then receive a second score after our modifications.
- linear_coeff_gridsearch.py: provide a list of *.input.json files and then conduct a parameter gridsearch, which produces a CSV file that maps CelloQuery() scores to parameter modifications, chassis, and signal pairs.
- screen_visuals.py: takes a CSV file (produced from linear_coeff_gridsearch.py) and produces a series of exploratory visuals.
- cello_pre_work.py: generates a set of *.input.json files with modified linear coefficients, which then feeds into the linear_coeff_gridsearch.py module.

## Project Dependencies
We used Poetry (https://python-poetry.org/) for dependencies management in our repository. The celloapi2 usage example (https://github.com/CIDARLAB/celloapi2) should run without errors-- so long as you 1) call poetry install to get all dependencies and 2) have a docker container running the cidarlab/cello-dnacompiler:latest on your local machine. I’ve modified the original template’s directory structure (https://github.com/CIDARLAB/homework1-template), as Celloapi2/CelloQuery() was throwing errors for some reason--Jackson helped me troubleshoot this early on. Try running main.py on your machine (you should only need to change the absolute paths for in_dir and out_dir).

## Suggested Reading
1. Vaidyanathan, P., Der, B. S., Bhatia, S., Roehner, N., Silva, R., Voigt, C. A., & Dens- more, D. (2015). A Framework for Genetic Logic Synthesis. Proceedings of the IEEE, 103(11), 2196-2207.
(This Paper should help understand the basic framework, terms and defini- tions of Logic Synthesis applied for Genetic circuits. Specifically, Sections 1,2,3 as well as Fig 2 will be helpful)
2. Yaman, F., Bhatia, S., Adler, A., Densmore, D., & Beal, J. (2012). Automated selec- tion of synthetic biology parts for genetic regulatory networks. ACS synthetic biology, 1(8), 332-344.
(The Results section as well as Fig 5 will be useful)
3. Stanton, B. C., Nielsen, A. A., Tamsir, A., Clancy, K., Peterson, T., & Voigt, C. A. (2014). Genomic mining of prokaryotic repressors for orthogonal logic gates. Nature chemical biology, 10(2), 99-105.
