#!/bin/bash
  #SBATCH --job-name my_first_job
  #SBATCH --time 05:00
  #SBATCH --output test-job_%A_%a.out
  #SBATCH --error test-job_%A_%a.err
  #SBATCH --partition=remeis
  #SBATCH --ntasks=8
  #SBATCH --mem-per-cpu=1G
  setenv OMP_NUM_THREADS 8
  #SBATCH --mail-type=ALL
  #SBATCH --mail-user=aakashbhat7@gmail.com          
  #SBATCH --export=all
  srun -l ./rn
