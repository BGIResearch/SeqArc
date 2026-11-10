# Runtime and example downloads

The [SeqArc v4.0.0 release](https://github.com/BGIResearch/SeqArc/releases/tag/v4.0.0) provides the Linux runtime and complete example archives as separate downloads. From a checkout of this repository, the commands below install them in `../release-assets`.

## Install the runtime

The [runtime bundle](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/SeqArc-runtime-linux-x86_64.tar.gz) contains `SeqArcDecompress`, `SeqArcIndex`, the [research license](../LICENSE), checksums and third-party notices. The [release checksums](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/SHA256SUMS) cover the bundle and every example archive.

From the repository root:

```bash
mkdir -p ../release-assets/core ../release-assets/optional
curl --fail --location --retry 3 -o ../release-assets/SeqArc-runtime-linux-x86_64.tar.gz \
  https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/SeqArc-runtime-linux-x86_64.tar.gz
curl --fail --location --retry 3 -o ../release-assets/SHA256SUMS \
  https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/SHA256SUMS
(cd ../release-assets && sha256sum --ignore-missing -c SHA256SUMS)
tar -xzf ../release-assets/SeqArc-runtime-linux-x86_64.tar.gz -C ../release-assets
(cd ../release-assets/runtime && sha256sum -c SHA256SUMS)
../release-assets/runtime/SeqArcDecompress --help
```

`--ignore-missing` checks the downloads you selected. Both checksum commands should report `OK` for every file checked.

## Download and run the smallest example

Download both mates of the fungal ITS example (10.2 MiB in total):

```bash
curl --fail --location --retry 3 -o ../release-assets/core/Data40_noref_SRR30515680_1.fastq.arc \
  https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data40_noref_SRR30515680_1.fastq.arc
curl --fail --location --retry 3 -o ../release-assets/core/Data40_noref_SRR30515680_2.fastq.arc \
  https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data40_noref_SRR30515680_2.fastq.arc
(cd ../release-assets && sha256sum --ignore-missing -c SHA256SUMS)
python3 scripts/examples.py data40_noref --work example-work/data40
```

This restores both complete FASTQ files and checks their byte counts and SHA-256 digests.

## Other example downloads

Save each archive to the folder shown below, keeping its filename. Paired examples require both mates. All paths are relative to the repository root.

| Example | Download | Save under |
| --- | --- | --- |
| `data45_noref` | [Data45_noref_DRR171213_1.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data45_noref_DRR171213_1.fastq.arc) | `../release-assets/core/` |
| `data45_noref` | [Data45_noref_DRR171213_2.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data45_noref_DRR171213_2.fastq.arc) | `../release-assets/core/` |
| `data45_ref` | [Data45_ref_DRR171213_1.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data45_ref_DRR171213_1.fastq.arc) | `../release-assets/core/` |
| `data45_ref` | [Data45_ref_DRR171213_2.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data45_ref_DRR171213_2.fastq.arc) | `../release-assets/core/` |
| `data46_ref` | [Data46_ref_SRR30502372_1.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data46_ref_SRR30502372_1.fastq.arc) | `../release-assets/core/` |
| `data46_ref` | [Data46_ref_SRR30502372_2.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data46_ref_SRR30502372_2.fastq.arc) | `../release-assets/core/` |
| `data25_noref` | [Data25_noref_DRR1089360.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data25_noref_DRR1089360.fastq.arc) | `../release-assets/core/` |
| `data40_noref` | [Data40_noref_SRR30515680_1.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data40_noref_SRR30515680_1.fastq.arc) | `../release-assets/core/` |
| `data40_noref` | [Data40_noref_SRR30515680_2.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data40_noref_SRR30515680_2.fastq.arc) | `../release-assets/core/` |
| `data28_noref` | [Data28_noref_SRR36288068_1.fastq.arc](https://github.com/BGIResearch/SeqArc/releases/download/v4.0.0/Data28_noref_SRR36288068_1.fastq.arc) | `../release-assets/optional/` |

After downloading an example, verify it and run its example ID:

```bash
(cd ../release-assets && sha256sum --ignore-missing -c SHA256SUMS)
python3 scripts/examples.py data45_ref --work example-work/data45-ref
```

Reference-based examples download the pinned public FASTA and build an index locally. No separately supplied FASTA or prebuilt index is needed. [Reference records](../examples/references.json) specify the assemblies, download locations and exact FASTA checksums.

Use `python3 scripts/examples.py list` to list the examples and download sizes. The [manifest](../examples/manifest.tsv) records file sizes and checksums. Alternative local locations can be supplied with `--runtime` and `--assets`.

```text
parent/
  SeqArc/                 repository checkout
  release-assets/
    SeqArc-runtime-linux-x86_64.tar.gz
    SHA256SUMS
    runtime/
      SeqArcDecompress
      SeqArcIndex
      LICENSE
      SHA256SUMS
      notices/
    core/                 selected core .arc files
    optional/             optional ONT .arc file
```
