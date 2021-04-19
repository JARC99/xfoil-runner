"""Runs an XFOIL analysis for a given airfoil and flow conditions"""
import os
import subprocess
import numpy as np

# %% Inputs

airfoil_name = "NACA0012"
alpha_i = 0
alpha_f = 10
alpha_step = 0.25
Re = 1000000
n_iter = 100

# %% XFOIL input file writer 

if os.path.exists("polar_file.txt"):
    os.remove("polar_file.txt")

input_file = open("input_file.in", 'w')
input_file.write("LOAD {0}.dat\n".format(airfoil_name))
input_file.write(airfoil_name + '\n')
input_file.write("PANE\n")
input_file.write("OPER\n")
input_file.write("Visc {0}\n".format(Re))
input_file.write("PACC\n")
input_file.write("polar_file.txt\n\n")
input_file.write("ITER {0}\n".format(n_iter))
input_file.write("ASeq {0} {1} {2}\n".format(alpha_i, alpha_f,
                                             alpha_step))
input_file.write("\n\n")
input_file.write("quit\n")
input_file.close()

subprocess.call("xfoil.exe < input_file.in", shell=True)

polar_data = np.loadtxt("polar_file.txt", skiprows=12)