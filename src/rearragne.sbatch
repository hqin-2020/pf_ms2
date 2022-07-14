#!/bin/bash

#SBATCH --job-name=rearrange
#SBATCH --output=rearrange.out
#SBATCH --error=rearrange.err
#SBATCH --time=0-8:00:00
#SBATCH --partition=bigmem2
#SBATCH --nodes=1
#SBATCH --cpus-per-task=28
#SBATCH --mem=500G

module load python/anaconda-2021.05

python3 rearrange.py  