# Example archive verification

All ten [example archives](../examples/manifest.tsv) were decompressed with the distributed executables. The resulting FASTQ files matched the expected full-file byte counts and SHA-256 digests. [The verification record](../examples/runtime_verification.json) gives the binary hashes and per-file results.

For the four reference-based files in Data 45 and Data 46, the exact public FASTAs were downloaded and checked against [recorded reference checksums](../examples/references.json), then indexed with `SeqArcIndex` before decompression. One Data 40 archive was also decompressed to gzip FASTQ; the uncompressed contents matched the expected FASTQ digest.

The [example runner](../scripts/examples.py) repeats these checks. Adding `--check-original` also downloads the original public gzip FASTQ and compares its uncompressed stream with the decoder output. This additional download check was not completed during release verification; the recorded checks used the retained original inputs. The original public URLs and hashes remain in the [manifest](../examples/manifest.tsv).
