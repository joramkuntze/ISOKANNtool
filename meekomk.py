import subprocess

def mk_prepare_ligand(input, output):
    print(input)
    subprocess.call(['mk_prepare_ligand.py','-i', input, '-o', output])

def mk_export(input, output):
    subprocess.call(['mk_export.py', input, '-o', output])
 