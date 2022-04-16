import os
import csv


def create_manifest():
    #input: absolute file path of FASTQ directory
    fastq_folder = input("Enter your the absolute file path of your FASTQ directory: ")
    manifest_folder = input("Enter your the absolute file path of the directory you want the manifest folder to be in: ")
    manifest_path = os.path.join(manifest_folder, 'manifest.tsv')

    #Create .tsv file with sampleID, foward, and reverse columns
    with open(manifest_path, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        tsv_writer.writerow(['sample-id','forward-absolute-filepath', 'reverse-absolute-filepath'])

    #iterate through sample folders in FASTQ directory 
        for subdir, dirs, files in os.walk(fastq_folder):
            dirs = sorted(dirs)
            for dir in dirs:
                sample_dir = os.path.join(subdir, dir)
                for path, d, s_files in os.walk(sample_dir):
                    for name in s_files:
                        sample_path = os.path.join(path, name)
                        substrings = name.split('_')
                        sample_id = substrings[0]
                        if (len(substrings) != 5):
                            continue
                        if (substrings[3] == 'R1'):
                            forward = sample_path
                        elif (substrings[3] == 'R2'):
                            reverse = sample_path 
                    tsv_writer.writerow([sample_id, forward, reverse])

create_manifest()









