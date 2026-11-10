#!/usr/bin/env python3
"""Download selected original benchmark inputs; no reference substitution or conversion."""
import argparse
import csv
import hashlib
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--ids', required=True, help='Comma-separated dataset IDs, or all')
p.add_argument('--output', type=Path, required=True)
args = p.parse_args()
with (ROOT/'benchmark/dataset/files.tsv').open() as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
wanted = {r['dataset'] for r in rows} if args.ids=='all' else set(args.ids.split(','))
if wanted - {r['dataset'] for r in rows}:
    p.error('Unknown dataset ID')
seen = set()
for row in rows:
    if row['dataset'] not in wanted or row['source_URL'] in seen:
        continue
    seen.add(row['source_URL'])
    output = args.output/f'Data_{row["dataset"]}'/row['source_filename']
    output.parent.mkdir(parents=True, exist_ok=True)
    partial = output.with_name(output.name+'.download')
    subprocess.run(['curl', '--fail', '--location', '--retry', '3', row['source_URL'], '-o', str(partial)], check=True)
    if not partial.is_file() or partial.stat().st_size == 0:
        raise SystemExit('Download produced no data; check network/proxy settings: '+row['source_URL'])
    if row['source_publisher_MD5']:
        h = hashlib.md5()
        with partial.open('rb') as f:
            for block in iter(lambda: f.read(8*1024*1024), b''):
                h.update(block)
        if h.hexdigest() != row['source_publisher_MD5']:
            raise SystemExit('Publisher MD5 mismatch: '+str(output))
    partial.replace(output)
    print('Downloaded', output)
    if row['dataset']=='6':
        print('Dataset 6 is a BAM source: see benchmark/dataset/README.md for the completed benchmark preparation record.')
