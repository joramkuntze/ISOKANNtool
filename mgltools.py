import subprocess

def mgltools_receptor(input, output):
    MGLTOOLS_PATH = "mgltools_x86_64Linux2_1.5.7"
    command = f"{MGLTOOLS_PATH}/bin/pythonsh {MGLTOOLS_PATH}/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py -r {input} -o {output}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

def mgltools_ligand(input, output):
    MGLTOOLS_PATH = "mgltools_x86_64Linux2_1.5.7"
    command = f"{MGLTOOLS_PATH}/bin/pythonsh {MGLTOOLS_PATH}/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -l {input} -o {output}"
    print(command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
