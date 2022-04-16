import filecmp
import os

def manifest_test():
    manifest_file = input("Enter your the absolute file path of your manifest file: ")
    print(filecmp.cmp(manifest_file, 'test/manifest-file-test.tsv'))

manifest_test()