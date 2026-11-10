# Program usage

Unpack the [runtime bundle](downloads.md), then inspect the commands:

```bash
../release-assets/runtime/SeqArcDecompress --help
../release-assets/runtime/SeqArcIndex --help
```

Decompress an archive that does not use an external reference:

```bash
../release-assets/runtime/SeqArcDecompress -i example.fastq.arc -o restored.fastq --type 1 -t 4
```

For an archive compressed with an external reference, use the exact reference assembly version. After obtaining and checking the FASTA listed in [examples/references.json](../examples/references.json):

```bash
../release-assets/runtime/SeqArcIndex -r work/reference.fa -o work -t 4
../release-assets/runtime/SeqArcDecompress -i example.fastq.arc -o restored.fastq --type 1 -t 4 -r work/reference.fa
```

Use `--type 0` with an output filename ending in `.fastq.gz` for gzip FASTQ; `--type 1` writes plain FASTQ. For a complete example with reference download, index construction, decompression and checksum checking, use `python3 scripts/examples.py data45_ref --work example-work/data45-ref` from the repository root.
