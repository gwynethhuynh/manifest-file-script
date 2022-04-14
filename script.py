import os
import csv

#input: absolute file path of FASTQ directory
fastq_folder = input("Enter your the absolute file path of your FASTQ directory: ")
#Create .tsv file with sampleID, foward, and reverse columns


with open('./manifest.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter="\t")
    tsv_writer.writerow(['sample-id','forward-absolute-filepath', 'reverse-absolute-filepath'])

#iterate through sample folders in FASTQ directory 
    for subdir, dirs, files in os.walk(fastq_folder):
        for dir in dirs:
            sample_dir = os.path.join(subdir, dir)
            for path, d, s_files in os.walk(sample_dir):
                for name in s_files:
                    sample_path = os.path.join(path, name)
                    print(sample_path)
                    substrings = name.split('_')
                    sample_id = substrings[0]
                    if (len(substrings) != 5):
                        continue
                    if (substrings[3] == 'R1'):
                        forward = sample_path
                    elif (substrings[3] == 'R2'):
                        reverse = sample_path 
                tsv_writer.writerow([sample_id, forward, reverse])


"""
for each sample folder: 
    sampleID = "string" before "_" in folder name
    add sampleID to .tsv file
    for each file in folder:
        forward = filepath of R1
        reverse = filepath of R2
        add foward to .tsv file
        add reverse to .tsv file
"""








