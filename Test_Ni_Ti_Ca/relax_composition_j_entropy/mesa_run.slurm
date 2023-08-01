#!/bin/bash
  #SBATCH --job-name relax_wd
  #SBATCH --time 06:00:00
  #SBATCH --output test-job_%A_%a.out
  #SBATCH --error test-job_%A_%a.err
  #SBATCH --partition=remeis
  #SBATCH --nodes=1
  #SBATCH --ntasks=8
  #SBATCH --mem-per-cpu=7000
  #SBATCH --mail-type=ALL
  #SBATCH --mail-user=aakashbhat7@gmail.com          
  #SBATCH --export=all
  srun -l ./rn
