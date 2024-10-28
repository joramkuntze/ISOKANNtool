import subprocess

def protonation(input, output, output_pqr_file):
    subprocess.run(['pdb2pqr', '--ff=AMBER', '--titration-state-method', 'propka', '--with-ph=7.4', '--pdb-output', output, input, output_pqr_file])
