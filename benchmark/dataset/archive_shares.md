# How to read the archive shares

[Benchmark](../README.md) · [Dataset documentation](README.md) · [Selection catalogue](selection_catalogue.csv)

The catalogue includes four percentages and an explanation of what each row counts. The percentages describe the public-archive category represented by an entry. They help show how common that category is in the archive.

| Column | Meaning |
|---|---|
| Workload: stock share | The workload's share of reported sequence bases in records first released through 30 September 2026. |
| Workload: annual share | Its share of reported sequence bases first released from 1 October 2025 through 30 September 2026. |
| Model combination: stock share | The stock share after also selecting the entry's submitted library-source label, sequencing platform and instrument model. |
| Model combination: annual share | The annual share for that narrower combination. |
| What these numbers cover | The category and model combination counted, including any features the survey cannot identify. |

Rows are sorted by **Workload: stock share**, highest first. Only when that value is equal does **Model combination: stock share** determine the order, also highest first. An unmeasurable model share goes last within its tied workload group. Remaining ties use Data ID. Data IDs, file names and download paths remain fixed.

Each percentage is `100 × matching reported bases / reported bases in the whole survey window`. Stock contains 102,706,156,796,947,692 reported bases; annual additions contain 23,531,275,808,337,950. The calculation was made on 5 November 2026 using the same ENA-indexed public INSDC metadata snapshot retrieved on 9 October 2026. This calculation did not refresh the survey.

These are shares of reported bases, not shares of benchmark file sizes or measured market production. Business value and useful technical differences are explained in the selection reasons. They are not included in this numerical sort. Categories overlap, and annual additions are part of stock, so the row percentages must not be added.

Some features are absent from the saved metadata. For example, the fields do not identify quality-value patterns, Smart-seq2, CITE tag roles, spatial protocols, ITS/16S targets, or HiFi/CLR processing. Such rows state the broader category used. CycloneSEQ has no identifiable dedicated platform or model label in this snapshot; its specific combination is shown as **Not measurable**, not as a measured zero. A numerical zero elsewhere means no reported bases matched that exact category and window.

Species categories explicitly pool the exact species name and its space-separated strain or subspecies suffixes. Whiteleg shrimp includes the names *Penaeus vannamei* and *Litopenaeus vannamei*; the broader *Mycobacterium tuberculosis* complex label is excluded. Community material categories use their stated exact archive labels. This is grouping of recorded names, not a complete taxonomy audit. Unknown names remain in the whole-window denominator. Missing or negative base values are excluded from base sums: 378 stock runs and no annual runs.

The [saved values and category filters](archive_shares.json) include exact base numerators and denominators. The [aggregation query](archive_base_shares.sql) records how the frozen metadata were grouped. Percentages are numerical cells in Excel and percentage strings in CSV; Excel displays rounded values. The machine-readable values retain twelve decimal places in percentage points.
