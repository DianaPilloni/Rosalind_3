import re
with open ('ctbl.txt','r') as file:
    f=file.read()

def create_a_character_table(tree):
    
    taxa = sorted(taxon for taxon in re.split('[(),]+', tree.rstrip(';')) if taxon)

    # find all the locations of pairs of matching parentheses
    pop = []
    ok = []
    for i in range(len(tree)):
        if tree[i] == '(':
            pop.append(i)
        if tree[i] == ')':
            ff = pop.pop()
            ok.append((ff, i))

    tab = []
    for (i, j) in ok[:-1]:
        sub = [taxon for taxon in re.split('[(),]+', tree[i:j+1]) if taxon]
        array = [int(taxa[k] in sub) for k in range(len(taxa))]
        tab.append(''.join(map(str, array)))
    return tab

with open ('ctblsol.txt','w') as file:
    file.truncate()
    file.write('\n'.join(create_a_character_table(f)))
