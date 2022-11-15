# Kspectra
Generate k-mer spectra from fasta sequences to observe modalities of distribution.

## Author
- Selvalakshmi (https://github.com/Selvalakshmi27)

## Dependencies
- Python (3.9.12)
- matplotlib (3.5.2)
- biopython (1.79)
- pandas (1.3.4)

## Usage
```
python kspectra.py [input.fasta] [k-mer size] [x-limit] [title]
```
- input.fasta = Genome sequence in fasta format
- k-mer size = Desired k-mer size (Ex: 3,9,11)
- x-limit = X-limit value for the kmer spectra graph
- title = Title for the gragh

## Example
```
python kspectra.py e.coli_refseq.fasta 8 400 E.coli_K=8
```
## Output
Three files are generated as the output:
- kmer_count.txt
- kmer_frequency.txt
- kmer_spectra.png

Sample output files and reference e.coli genome is found under Example folder


