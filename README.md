# ISOKANNtool
In the main.py file exist two workflows first the docking flow, that creates multiple docking positions for your ligand and protein, then the conversion to ISOKANN. 
In main.py you can input the ID from RCSB.
Include the ligand file path and also input the slug of the orignal ligand from rcsb so that the binding site can be automatically determined. If you want to change the site manually you can adjust this in the main.py file.


Dependencies: 

MGLTOOLS: Change the path in the file mgltools.py also you need to uncomment line 104 and comment line 105! in the file {MGLTOOLS_PATH}/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py.
OpenBabel, smina, meekomk, pdbfixer, pdb2pqr, Bio python package
