import os
from bio import download_and_strip_pdb
from mgltools import mgltools_receptor
from mgltools import mgltools_ligand
from protonation import protonation
from openbbl import smiles_to_pdb, pdbqt_to_pdb, pdbqt_to_sdfs
from smina import smina_docking
from pdbfixer import pdbfixer
from meekomk import mk_prepare_ligand, mk_export

def auto_dock(id, ligand_filename, output_folder="output", ligand_slug="XZD"):
    stripped_pdb, lc, ls = download_and_strip_pdb(id, output_folder, ligand_slug) 
    smiles_to_pdb(ligand_filename, f"output/{id}_ligand.sdf")
    protonation(stripped_pdb, f"output/{id}_protonated.pdb", f"output/{id}_protonated.pqr")
    mgltools_receptor(f"output/{id}_protonated.pdb", f"output/{id}_protonated.pdbqt")
    print("MK LIGAND")
    mk_prepare_ligand(f"output/{id}_ligand.sdf", f"output/{id}_ligand.pdbqt")
    # mgltools_ligand(f"output/{id}_ligand.pdb", f"output/{id}_ligand.pdbqt") #uncomment line 104 and comment line 105!!!
    center_x, center_y, center_z = lc
    size_x, size_y, size_z = ls
    smina_docking(f"output/{id}_protonated.pdbqt", f"output/{id}_ligand.pdbqt", center_x, center_y, center_z, size_x, size_y, size_z, f"output/{id}_docked.pdbqt", f"output/{id}_docked.log")   

def convert_for_isokann(receptor_pdbqt, ligand_pdbqt, docking_pdbqt):
    pdbqt_to_pdb(receptor_pdbqt, receptor_pdbqt.replace(".pdbqt", ".pdb"))
    pdbfixer(receptor_pdbqt, receptor_pdbqt.replace(".pdbqt", "_fixed.pdb"))
    mk_export(docking_pdbqt, docking_pdbqt.replace('.sdf', '_exported.sdf'))
    # pdbqt_to_sdfs(docking_pdbqt, docking_pdbqt.replace(".pdbqt", ".sdf"))
    # i = 1
    # while os.path.exists(docking_pdbqt.replace(".pdbqt", f"{i}.sdf")):
    #     sdf = docking_pdbqt.replace(".pdbqt", f"{i}.sdf")
    #     print("mk_prepare:" + sdf)
    #     print("prpared")
    #     mk_export(sdf.replace('.sdf', '_prepared.pdbqt'), sdf.replace('.sdf', 'abcd_prepared.sdf'))
    #     i += 1





'''
Usage: input pdb ID and save the the path to the new Ligand file, also add the ligand slug that is in the protein for automatically finding the docking coordinates.
'''
if __name__ == "__main__":
    id = "6O0K"
    auto_dock(id, "ligand.smi", output_folder="output", ligand_slug="XZD​")
    convert_for_isokann(f"output/{id}_protonated.pdbqt", f"output/{id}_ligand.pdbqt", f"output/{id}_docked.pdbqt")

