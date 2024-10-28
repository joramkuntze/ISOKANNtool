import subprocess

def smina_docking(receptor_pdbqt, ligand_pdbqt, center_x, center_y, center_z, size_x, size_y, size_z, output, log_output):
    result = subprocess.run([
        'smina',
        '--receptor', receptor_pdbqt,
        '--ligand', ligand_pdbqt,
        '--center_x', str(center_x),
        '--center_y', str(center_y),
        '--center_z', str(center_z),
        '--size_x', str(size_x),
        '--size_y', str(size_y),
        '--size_z', str(size_z),
        '--out', output,
        '--log', log_output
    ])
    print(result)