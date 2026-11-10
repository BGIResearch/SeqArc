#!/usr/bin/env python3
"""Download pinned public references and verify the published SeqArc examples."""
import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]

def digest(path, compressed=False):
    h = hashlib.sha256()
    size = 0
    with (gzip.open(path, 'rb') if compressed else path.open('rb')) as f:
        for block in iter(lambda: f.read(8*1024*1024), b''):
            h.update(block)
            size += len(block)
    return size, h.hexdigest()

def download(url, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(path.name+'.download')
    subprocess.run(['curl', '--fail', '--location', '--retry', '3', '--connect-timeout', '30', '--max-time', '1800', url, '-o', str(partial)], check=True)
    if not partial.is_file() or partial.stat().st_size == 0:
        raise SystemExit('Download produced no data; check the URL and network/proxy settings: '+url)
    partial.replace(path)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('example', help='Example ID (such as data40_noref), or list')
parser.add_argument('--assets', type=Path, default=ROOT.parent/'release-assets')
parser.add_argument('--runtime', type=Path, default=ROOT.parent/'release-assets/runtime')
parser.add_argument('--work', type=Path, default=Path('example-work'))
parser.add_argument('--threads', type=int, default=4)
parser.add_argument('--check-original', action='store_true', help='Download original public gzip FASTQ and compare its uncompressed contents too')
args = parser.parse_args()
with (ROOT/'examples/manifest.tsv').open() as f:
    all_rows = list(csv.DictReader(f, delimiter='\t'))
if args.example == 'list':
    for name in dict.fromkeys(r['example'] for r in all_rows):
        rows = [r for r in all_rows if r['example']==name]
        print(name, rows[0]['organism'], rows[0]['technology'], rows[0]['assay'], sum(int(r['archive_bytes']) for r in rows), 'archive bytes')
    raise SystemExit(0)
rows = [r for r in all_rows if r['example']==args.example]
if not rows:
    parser.error('Unknown example; use list')
runtime = args.runtime.resolve()
work = args.work.resolve()
work.mkdir(parents=True, exist_ok=True)
references = {r['id']: r for r in json.loads((ROOT/'examples/references.json').read_text())}
reference = None
if rows[0]['reference']:
    ref = references[rows[0]['reference']]
    reference = work/(ref['id']+'.fa')
    expected = (int(ref['FASTA_bytes']), ref['FASTA_SHA256'])
    if not reference.exists() or digest(reference) != expected:
        bundle = work/(ref['accession']+'.zip')
        download(ref['download_url'], bundle)
        with ZipFile(bundle) as z, z.open(ref['zip_member']) as source, reference.open('wb') as destination:
            shutil.copyfileobj(source, destination)
        if digest(reference) != expected:
            raise SystemExit('Downloaded reference does not match the pinned FASTA bytes/checksum')
    subprocess.run([str(runtime/'SeqArcIndex'), '-r', str(reference), '-o', str(work), '-t', str(args.threads)], check=True)
report = []
for row in rows:
    archive = args.assets.resolve()/row['asset_path']
    if digest(archive) != (int(row['archive_bytes']), row['archive_SHA256']):
        raise SystemExit('Archive checksum mismatch: '+str(archive))
    output = work/row['input_file'].removesuffix('.gz')
    command = [str(runtime/'SeqArcDecompress'), '-i', str(archive), '-o', str(output), '--type', '1', '-t', str(args.threads)]
    if reference:
        command += ['-r', str(reference)]
    subprocess.run(command, check=True)
    observed = digest(output)
    expected = (int(row['expected_FASTQ_bytes']), row['expected_FASTQ_SHA256'])
    if observed != expected:
        raise SystemExit('Restored FASTQ differs from expected complete original: '+row['input_file'])
    checked_original = False
    if args.check_original:
        original = work/row['input_file']
        download(row['original_gzip_url'], original)
        if row['original_gzip_SHA256'] and digest(original) != (int(row['original_gzip_bytes']), row['original_gzip_SHA256']):
            raise SystemExit('Downloaded original gzip differs from pinned input')
        if digest(original, compressed=True) != observed:
            raise SystemExit('Decoded FASTQ differs from downloaded original gzip contents')
        checked_original = True
    report.append({'example': args.example, 'file': row['input_file'], 'FASTQ_bytes': observed[0], 'FASTQ_SHA256': observed[1], 'verified': True, 'downloaded_original_checked': checked_original, 'reference': row['reference']})
    print('PASS', row['input_file'], observed[0], observed[1])
(work/'verification.json').write_text(json.dumps(report, indent=2)+'\n')
