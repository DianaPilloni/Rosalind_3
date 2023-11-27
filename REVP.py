from Bio.Seq import Seq
from fastafunction import FASTA

ee=FASTA('revpfasta.txt')
seq=ee[0]
result=[]
for n in range(4,13):
    mylist=[seq[a:a+n] for a in range(len(seq)-(n-1))]
    for el in mylist:
        if el==str(Seq(el).reverse_complement()):
            result.append(el)

pairs=[] 
control=[]
for el in result:
    indices = [index+1 for index, _ in enumerate(seq) if seq.startswith(el, index)]
    if indices not in control:
        for id in indices:
            pairs.append((id,len(el)))
    control.append(indices)

for pair in sorted(pairs):
    print(' '.join (str(el)for el in pair))
