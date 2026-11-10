# Runtime requirements

The Linux x86-64 release contains `SeqArcDecompress` and `SeqArcIndex`. The programs use host C/C++ and OpenMP runtime libraries; glibc 2.34 and GLIBCXX_3.4.30 or later are required. The decompressor writes plain or gzip FASTQ. The executables’ SHA-256 hashes are listed in the runtime checksum file.

The benchmark performance results were measured with SeqArc 4.0.0; the separately distributed executables provide decompression and reference indexing. [Verification](verification.md) records the example archive checks.
