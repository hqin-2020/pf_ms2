#!/bin/bash

#SBATCH --job-name=pf_ms
#SBATCH --output=pf_ms.%A_%a.out
#SBATCH --error=pf_ms.%A_%a.err
#SBATCH --time=0-8:00:00
#SBATCH --partition=broadwl
#SBATCH --nodes=1
#SBATCH --cpus-per-task=28
#SBATCH --mem-per-cpu=2000
#SBATCH --array=1-150
#SBATCH --constraint=edr

module load python/anaconda-2021.05

srun python3 Run_Aso1_0_CPU_$SLURM_ARRAY_TASK_ID.py  