import os
import subprocess
from rdkit import Chem


# Can specify speed/accuracy between 1 to 5 or slowest, slow, med, fast, fastest
def smiles_to_pdb(input_smi, output_pdb, speed="med"):
    subprocess.run(["obabel", "-ismi", input_smi, "-osdf", "-O", output_pdb, "-p", "7.4", "--gen3d", speed])
    return output_pdb

def pdbqt_to_pdb(input_pdbqt, output_pdb):
    subprocess.run(["obabel", "-ipdbqt", input_pdbqt, "-opdb", "-O", output_pdb])
    return output_pdb

# Creates multiple SDF files which are retured as a list
def pdbqt_to_sdfs(input_pdbqt, output_sdf):
    print("---------")
    subprocess.run(["obabel", "-ipdbqt", input_pdbqt, "-osdf", "-O", output_sdf, "-m", "-h"])
    print("---------")