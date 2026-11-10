# Benchmark dataset

The collection contains 52 public input units represented by 91 prepared gzip FASTQ files. Selection considered accumulated archive holdings, recent releases, research and sequencing applications, and variation in technology, organism, assay, read structure and natural file size. Small datasets were retained when they represented the selected application. Selection did not assign performance weights to datasets.

- `datasets.tsv`: identities, biological material, technology, assay and selection rationale for all 52 inputs.
- `files.tsv`: public source URLs, file membership, publisher checksums, prepared-input identities and preparation information.
- `coverage.tsv`: 16 overlapping application categories; counts are not disjoint.
- `references_used.tsv`: the 43 reference assignments actually used in the selected analysis, with recorded assembly versions and specific provenance qualifications.
- `selection_catalogue.csv`: the original selection catalogue, including ordering by public-archive stock share. This preserves selection rationale; executed reference assignments and completed preparation outcomes are recorded in the current tables above.
- `archive_shares.json`, `archive_shares.md` and `archive_base_shares.sql`: survey values, interpretation and the saved aggregation query used to inform selection.

The selection records derive from catalogue source snapshot version 1.2.0, source revision `3b051a1abe07b1ef6b343ba1340ef3d8390b05ba`. The selected input identities and completed preparation outcomes are recorded in `files.tsv` and the benchmark results.

Use `references_used.tsv` for assemblies used in the benchmark and `../../examples/references.json` for the runnable reference examples. These can differ from selection proposals in the source catalogue; use the recorded assembly version when building an index. The two example assemblies are downloaded directly from NCBI, and their exact FASTA digests are checked before indexing.

Download original public inputs from the repository root:

```bash
python3 scripts/download_inputs.py --ids 25,40,45,46 --output inputs
```

Use `--ids all` only when the storage and transfer requirements of the complete collection are intended. Public raw files remain at their source archives rather than being copied into Git.

Dataset 6 has a public BAM source. Its benchmark preparation was completed using SAMtools 1.22 name sorting and primary-read FASTQ export with stored quality scores, followed by pigz 2.8 `-n -6`. The prepared FASTQ contains 8,346,242 reads and 307,720,012,900 uncompressed bytes; its gzip file is 109,657,909,859 bytes. The downloader obtains the original BAM, not an already prepared gzip FASTQ. Exact retained preparation identities are included in the file records.

[Executed Data 6 preparation commands and checksums](data6_preparation.md) document the completed conversion.
