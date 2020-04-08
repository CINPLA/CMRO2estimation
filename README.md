# Spatially Resolved Estimation of Metabolic Oxygen Consumption From Optical Measurements in Cortex

This code was used to produce the results presented in Sætra et al. 20XX: [paper]

## Requirements 

If you want to reproduce Figures 7 and 8, navigate to the top directory of the repo and enter the following
command in the terminal: 
```bash
python3 setup.py install
```

Figures 7 and 8 also require [FEniCS](https://fenics.readthedocs.io/en/latest/installation.html#debian-ubuntu-packages).

Other requirements are given in `requirements.txt` and can be installed by the following command:
```bash
pip install -r requirements.txt
```
The remaining figures require Matlab (R2017b).

The code was run with Ubuntu 18.04.3. 

## Reproducing the results of the paper

All data can be downloaded from the data folder or be reproduced by running the script `run_all.sh`. This might run for a few days on a normal computer.
To plot and save the figures, run `plot_all.sh` in the figure folder.
Note that some of the figures have been edited in Inkscape for publication purposes.
