## a script to convert simple molecules from mol to csv
import json
import pandas as pd
colors = json.loads(open("colors.json").read())
colors = {key:[e[0]/255,e[1]/255,e[2]/255] for key,e in colors.items()}
## normalize colors

## make a rep of the molecule using https://en.wikipedia.org/wiki/Chemical_table_file 
# seems to be based on leading spaces
with open("ATP_model.sdf","r") as phile:
    atom_block =[]
    bond_block = []
    for lineind,line in enumerate(phile):
        # number of leading white space chars
        for i,char in enumerate(line):
            if not char.isspace():
                break
        print(lineind,i,line)
        if i == 1:
            # we are in atom counter
            pass
        elif i == 3:
            ## fancy trick for removing consecutive white spaces
            atom_block.append(' '.join(line.split()).split())
        elif i == 2:                                
            bond_block.append(' '.join(line.split()).split())
    print(atom_block)
    print()
    print(bond_block)
    # loop over bonds make an entry for each
    # this is complete with starting position and color and connection index
    # TODO think about how to prevent redrawing molecules that have multiple bonds
    
    rows = []

    for bond in bond_block:
        start_ind = int(bond[0])
        end_ind = int(bond[1])
        bond_type = int(bond[2])
        start_atom = atom_block[start_ind][:4]
        start_color = color[start_atom[3]]
        end_atom = atom_block[end_ind][:4]

        # could include something to indicate whether the start atom need's being drawn the first time or not?
        row_data = dict(
            X = 
        )

