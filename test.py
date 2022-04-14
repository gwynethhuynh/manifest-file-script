
import csv
name = "610C_S84_L001_R1_001.fastq.gz"
substrings = name.split('_')
print(substrings)

"""
with open('./manifest.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter="\t")
    a = "s1"
    b = "s2"
    c = "s3"
    tsv_writer.writerow(['sample-id','forward-absolute-filepath', 'reverse-absolute-filepath'])
    tsv_writer.writerow([a, b, c])
"""
"""
for i in range(10):
    for j in range(2):
        name = j % 1
        if j % 2 == 1:
            odd = j
        else:
            even = j
    print([name, odd, even])

"""