from fastafunction import FASTA
a=FASTA('kmp.txt')
seq=a[0]
def failarr(seq):
    n = len(seq)
    array = [0] * n

    for k in range(1, n):
        j = array[k - 1]

        while j > 0 and seq[k] != seq[j]:
            j = array[j - 1]

        if seq[k] == seq[j]:
            j += 1

        array[k] = j

    return array

result=failarr(seq)
with open('solkmp.txt','w') as file:
    file.truncate()
    file.write(' '.join(map(str,result)))
