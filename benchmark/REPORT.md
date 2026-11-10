# Benchmark results summary

This report summarizes benchmark measurements. See [protocol](README.md), [full results workbook](results.xlsx), [source cohort table](data/V9_CohortSummary.tsv) and [figures](figures).

Within each panel all tools use the same validated dataset set. Panels can contain different sets and must not be compared as if they used identical inputs. External-reference panels include reference-free SPRING where applicable, explicitly labelled; reference acquisition, index construction and separate reference storage are excluded.

Compression ratio = uncompressed FASTQ bytes / compressed archive bytes (higher is better). Times below are summed elapsed seconds for smaller short reads and hours for the other groups; memory is median per-dataset peak RSS, not a sum. Short-read size strata use mean prepared gzip size per file, with 0.5 GiB as the boundary.

## Smaller short-read datasets — no external reference

Common validated datasets: 12. Exact IDs are retained in the source table.

| Tool | Reference | Archive GiB | Compression ratio | Compression s | Decompression s | Compression RSS GiB | Decompression RSS GiB |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SeqArc_noref | none | 1.71 | 8.12 | 78.43 | 53.31 | 1.44 | 1.02 |
| Genozip_noref | none | 1.74 | 7.99 | 90.02 | 33.28 | 1.06 | 1.04 |
| SPRING | none | 1.03 | 13.55 | 306.11 | 128.58 | 1.72 | 1.28 |

## Smaller short-read datasets — reference options

Common validated datasets: 6. Exact IDs are retained in the source table.

| Tool | Reference | Archive GiB | Compression ratio | Compression s | Decompression s | Compression RSS GiB | Decompression RSS GiB |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SeqArc_ref | assigned external reference | 0.72 | 14.92 | 56.43 | 26.01 | 2.54 | 1.89 |
| Genozip_ref | assigned external reference | 0.87 | 12.37 | 305.51 | 21.52 | 3.15 | 0.97 |
| SPRING | none | 0.71 | 15.25 | 184.51 | 82.28 | 2.76 | 2.23 |

## Larger short-read datasets — no external reference

Common validated datasets: 28. Exact IDs are retained in the source table.

| Tool | Reference | Archive GiB | Compression ratio | Compression h | Decompression h | Compression RSS GiB | Decompression RSS GiB |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SeqArc_noref | none | 275.56 | 7.69 | 0.834 | 0.804 | 2.89 | 3.11 |
| Genozip_noref | none | 281.83 | 7.52 | 2.132 | 0.921 | 1.49 | 1.13 |
| SPRING | none | 152.60 | 13.89 | 18.969 | 2.964 | 5.71 | 6.02 |

## Larger short-read datasets — reference options

Common validated datasets: 22. Exact IDs are retained in the source table.

| Tool | Reference | Archive GiB | Compression ratio | Compression h | Decompression h | Compression RSS GiB | Decompression RSS GiB |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SeqArc_ref | assigned external reference | 112.42 | 16.05 | 1.266 | 0.456 | 5.24 | 3.52 |
| Genozip_ref | assigned external reference | 119.39 | 15.11 | 2.673 | 0.630 | 4.44 | 1.92 |
| SPRING | none | 120.07 | 15.03 | 17.002 | 2.458 | 5.84 | 6.23 |

With references on the common 22 datasets, SeqArc used 18.08 CPU h for compression, compared with 33.38 for Genozip and 202.82 for SPRING. Median peak compression memory was 5.24, 4.44 and 5.84 GiB, respectively; median peak decompression memory was 3.52, 1.92 and 6.23 GiB.

## Long-read datasets — no external reference

Common validated datasets: 8. Exact IDs are retained in the source table.

| Tool | Reference | Archive GiB | Compression ratio | Compression h | Decompression h | Compression RSS GiB | Decompression RSS GiB |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SeqArc_noref | none | 180.87 | 4.31 | 0.294 | 0.373 | 2.79 | 2.33 |
| Genozip_noref | none | 182.84 | 4.26 | 0.894 | 0.460 | 1.91 | 1.32 |
| SPRING | none | 179.32 | 4.35 | 4.189 | 1.627 | 17.42 | 17.11 |
| CoLoRd_noref | none | 128.27 | 6.08 | 6.969 | 4.344 | 10.14 | 2.00 |

## Long-read datasets — reference options

Common validated datasets: 6. Exact IDs are retained in the source table.

| Tool | Reference | Archive GiB | Compression ratio | Compression h | Decompression h | Compression RSS GiB | Decompression RSS GiB |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SeqArc_ref | assigned external reference | 115.22 | 5.71 | 1.311 | 0.275 | 8.81 | 8.20 |
| Genozip_ref | assigned external reference | 155.57 | 4.23 | 0.954 | 0.473 | 2.00 | 1.73 |
| SPRING | none | 151.12 | 4.35 | 3.609 | 1.369 | 19.59 | 19.77 |
| CoLoRd_ref | assigned external reference | 98.83 | 6.66 | 10.658 | 3.433 | 9.18 | 4.78 |


## Throughput

Throughput uses total prepared gzip input MiB divided by summed elapsed seconds for both stages. It is not based on uncompressed FASTQ size. Values come from the same cohort table and common input sets shown above.

| Stratum | Comparison | Tool | Compression MiB/s | Decompression MiB/s |
| --- | --- | --- | ---: | ---: |
| short_small | no_external_reference | SeqArc_noref | 40.32 | 59.32 |
| short_small | no_external_reference | Genozip_noref | 35.13 | 95.02 |
| short_small | no_external_reference | SPRING | 10.33 | 24.59 |
| short_small | reference_options | SeqArc_ref | 43.55 | 94.49 |
| short_small | reference_options | Genozip_ref | 8.04 | 114.21 |
| short_small | reference_options | SPRING | 13.32 | 29.87 |
| short_large | no_external_reference | SeqArc_noref | 156.16 | 161.89 |
| short_large | no_external_reference | Genozip_noref | 61.06 | 141.30 |
| short_large | no_external_reference | SPRING | 6.86 | 43.92 |
| short_large | reference_options | SeqArc_ref | 83.33 | 231.26 |
| short_large | reference_options | Genozip_ref | 39.46 | 167.39 |
| short_large | reference_options | SPRING | 6.20 | 42.92 |
| long | no_external_reference | SeqArc_noref | 231.25 | 182.40 |
| long | no_external_reference | Genozip_noref | 76.08 | 147.88 |
| long | no_external_reference | SPRING | 16.24 | 41.82 |
| long | no_external_reference | CoLoRd_noref | 9.76 | 15.66 |
| long | reference_options | SeqArc_ref | 43.65 | 207.76 |
| long | reference_options | Genozip_ref | 59.94 | 121.00 |
| long | reference_options | SPRING | 15.85 | 41.78 |
| long | reference_options | CoLoRd_ref | 5.37 | 16.66 |
