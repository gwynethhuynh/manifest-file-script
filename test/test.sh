gitdir=`git rev-parse --show-toplevel`
cp -r $gitdir/test/sample-fastq /tmp/
python3 $gitdir/script/script.py <<< "$(cat $gitdir/test/test_input.txt)"
echo ""
echo "diffstart"
diff $gitdir/test/manifest-file-test.tsv /tmp/manifest.tsv
echo "diffend (if above is empty it worked!)"
rm /tmp/manifest.tsv
