# Benchmark protocol and results

The benchmark comprises 52 selected datasets and 91 prepared gzip FASTQ files across 8 sequencing technology groups. The analytical inventory contains 259 dataset/tool/reference tests: 246 validated outcomes and 13 unsuccessful or unavailable-index outcomes. SeqArc passed all 52 reference-free and 43 reference-based tests. Both mates must pass for a paired dataset to count as validated.

The tested programs were SeqArc 4.0.0, Genozip 13.0.8, SPRING and CoLoRd 1.2.1. Genozip 13.0.8 was the latest version obtainable by the authors for this study without a commercial agreement. The tested SPRING executable does not print a version number.

Tests ran sequentially on a dual Intel Xeon Gold 6442Y machine with approximately 376 GiB RAM and Lustre storage. Commands requested 16 threads where supported; the evaluated CoLoRd decompressor had no explicit thread setting. Paired mates were processed separately. Compression read gzip FASTQ and decompression wrote plain FASTQ. Full-file validation compared uncompressed byte counts and XXH3-128 digests. The final timeout was four hours per file per compression or decompression stage; earlier-limit and manually terminated exceptions remain identified in `data/S7_Exceptions.tsv` and their retained records.

Compression ratio is uncompressed FASTQ bytes divided by archive bytes. Throughput uses prepared gzip input bytes per elapsed second for both compression and decompression. Input sizes, output sizes and times are summed across mates. Dataset peak memory is the larger mate peak; cohort memory summaries use medians. Reference preparation and separate storage are excluded, while reference loading during timed commands is included.

Short-read results distinguish mean prepared gzip size below 0.5 GiB per file from larger files; long reads are separate. Tools are compared on applicable, commonly validated inputs. Larger-short-read reference-option panels use 22 datasets shared by the three short-read tools; the wider SeqArc–Genozip pairwise comparison uses 23. Reference-free SPRING is explicitly labelled alongside external-reference methods in practical-options comparisons.

`results.xlsx` is the 25-sheet analytical workbook; matching TSV tables are in `data`. Local path prefixes in the published logs were replaced with portable placeholders. `log_provenance.tsv` gives original and published hashes for each transformed log.

`logs` contains 1,206 selected command, result and text-log files. `data/S3_Runs.tsv` links final per-file outcomes and exceptional historical command records. Unsuccessful results are preserved without imputed completion times or archive sizes. Figure source values are available in the cohort and per-dataset tables.

[Benchmark results report](REPORT.md) presents absolute compression ratios, sizes, times and memory for every common-input cohort.
