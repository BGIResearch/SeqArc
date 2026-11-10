# Dataset 6: completed BAM preparation

The benchmark used SAMtools 1.22 with HTSlib 1.22 and pigz 2.8. The commands below preserve the executed options and replace local paths with portable names. Obtain the source BAM using the URL in [files.tsv](files.tsv), naming it `calls.sorted.bam` in a dedicated working directory. These commands record the benchmark preparation.

```bash
LC_ALL=C samtools sort -n -@ 63 -m 768M -o name_sorted.bam calls.sorted.bam
LC_ALL=C samtools fastq -@ 63 -n -F 0x900 name_sorted.bam > Data_6.fastq
pigz -n -6 -p 64 -c -- Data_6.fastq > Data_6.fastq.gz
```

Before FASTQ export, the execution driver checked the primary alignment records with `LC_ALL=C samtools view -@ 63 -F 0x900 name_sorted.bam`, including flags, names, sequences and stored qualities. That check was separate from the FASTQ export stream. No missing quality values were synthesized. The source BAM was name-sorted before export; secondary and supplementary alignments were excluded.

| Object | Bytes | SHA-256 |
| --- | ---: | --- |
| Source BAM | 171763325052 | `6c55dff396d6fabc037459a7c305a82fa6c6c0db0118ddcb11ef13e24f1d1eb6` |
| Prepared FASTQ | 307720012900 | `c5fd12f1456894567dfb3615cc40633e33e9828b6b37b235fdaf052ae57f1ef5` |
| Prepared gzip FASTQ | 109657909859 | `458a7a2da2e472856e6a0738a9a26e099be8c0f606a219581bb67b609dba24df` |

The completed export contained 8,346,242 FASTQ records. The recorded full gzip decompression check matched the prepared FASTQ byte count and SHA-256. [Preparation provenance](data6_preparation_provenance.json) identifies the conversion receipt, run log and final check by checksum.
