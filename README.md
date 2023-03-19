# NGS


This repository contains multiple Python scrips to work on NGS dataset.

# 1) NCBI to UCSC SAM 
The script, ncbi_to_ucsc.py, takes an input file with NCBI chromosome codes and one or more SAM/BAM files with NCBI chromosome identifiers, and outputs modified SAM/BAM files with UCSC chromosome identifiers.
Run the script using the following command:
python2 ncbi_to_ucsc.py NC_chr.txt input.sam output.sam
## Requirements

- Python 2.7
- `NC_chr.txt` mapping file

- `NC_chr.txt`: Path to the mapping file downloaded from the NCBI website.
- `input.sam`: Path to the input SAM file.
- `output.sam`: Path to the output SAM file in UCSC format.

## Output

The output file will have the same format as the input file but with UCSC chromosome names instead of NCBI chromosome names.

## NC_chr.txt

The mapping file `NC_chr.txt` can be downloaded from the NCBI website using the following URL:
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.39_GRCh38.p13/GCF_000001405.39_GRCh38.p13_assembly_report.txt


