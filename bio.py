from Bio import PDB
import os

from Bio import PDB
import os

def download_and_strip_pdb(pdb_id, output_dir, ligand_slug):
    print(ligand_slug)
    pdb_list = PDB.PDBList()
    pdb_filename = pdb_list.retrieve_pdb_file(pdb_id, pdir=output_dir, file_format="pdb")
    
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, pdb_filename)

    input_dir = "input"  # Directory to save the PDB file
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    input_filename = os.path.join(input_dir, f"{pdb_id}.pdb")
    io = PDB.PDBIO()
    io.set_structure(structure)
    io.save(input_filename)
    
    def count_elements(struct):
        models = len(struct)
        chains = sum(1 for _ in struct.get_chains())
        residues = sum(1 for _ in struct.get_residues())
        atoms = sum(1 for _ in struct.get_atoms())
        return models, chains, residues, atoms

    original_counts = count_elements(structure)
    
    print(f"Original structure:")
    print(f"Models: {original_counts[0]}, Chains: {original_counts[1]}, Residues: {original_counts[2]}, Atoms: {original_counts[3]}")

    #find ligand center coordinate
    ligand_center = None
    for model in structure:
        for chain in model:
            for residue in chain:
                print(residue.resname)
                if residue.resname == "LBM":
                    print("Found Ligand")
                    max_x = -1000
                    max_y = -1000
                    max_z = -1000
                    min_x = 1000
                    min_y = 1000
                    min_z = 1000
                    for atom in residue.get_atoms():
                        if atom.get_coord()[0] > max_x:
                            max_x = atom.get_coord()[0]
                        if atom.get_coord()[1] > max_y:
                            max_y = atom.get_coord()[1]
                        if atom.get_coord()[2] > max_z:
                            max_z = atom.get_coord()[2]
                        if atom.get_coord()[0] < min_x:
                            min_x = atom.get_coord()[0]
                        if atom.get_coord()[1] < min_y:
                            min_y = atom.get_coord()[1]
                        if atom.get_coord()[2] < min_z:
                            min_z = atom.get_coord()[2]
                    center_x = (max_x + min_x) / 2
                    center_y = (max_y + min_y) / 2
                    center_z = (max_z + min_z) / 2
                    size_x = max_x - min_x + 5
                    size_y = max_y - min_y + 5
                    size_z = max_z - min_z + 5
                    ligand_center = (center_x, center_y, center_z)
                    ligand_size = (size_x, size_y, size_z)
            if ligand_center is not None:
                break
        if ligand_center is not None:
            break

    # Strip non-protein and handle alternate locations
    removed_residues = 0
    removed_atoms = 0
    for model in structure:
        for chain in model:
            for residue in list(chain):
                if residue.id[0] != " " or residue.resname not in PDB.Polypeptide.standard_aa_names:
                    chain.detach_child(residue.id)
                    removed_residues += 1
                else:
                    # Keep only the first alternate location
                    for atom in list(residue):
                        if atom.is_disordered():
                            atom.disordered_select(atom.disordered_get_id_list()[0])
                        if atom.altloc != " " and atom.altloc != "A":
                            residue.detach_child(atom.id)
                            removed_atoms += 1

    stripped_counts = count_elements(structure)
    
    print(f"\nStripped structure:")
    print(f"Models: {stripped_counts[0]}, Chains: {stripped_counts[1]}, Residues: {stripped_counts[2]}, Atoms: {stripped_counts[3]}")
    print(f"Removed residues: {removed_residues}, Removed atoms: {removed_atoms}")

    # Save the stripped structure
    io = PDB.PDBIO()
    io.set_structure(structure)
    output_filename = os.path.join(output_dir, f"{pdb_id}_stripped.pdb")
    io.save(output_filename)
    
    print(f"\nBereinigte Struktur gespeichert als: {output_filename}")

    return output_filename, ligand_center, ligand_size
