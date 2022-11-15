#!/usr/bin/python
#usage : python [input.fasta] [kmer_size] [X-limit for kmer_spectra] [title for kmer_spectra]

import sys
import argparse
from Bio import SeqIO
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('fasta', type=str)
parser.add_argument('kmer_size',type=int)
parser.add_argument('x_lim',type=int)
parser.add_argument('title',type=str)
args = parser.parse_args()

#Count the number of kmers in a genome and save as a dictionary
def kmer_count(fasta, kmer_size):
    data = {}
    for seq_record in SeqIO.parse(str(fasta),'fasta'):
        length=len(seq_record)
    for i in range(length - kmer_size + 1):
        kmer = seq_record.seq[i: i + kmer_size]
        try:
            data[kmer] += 1
        except KeyError:
            data[kmer] = 1
    return data

#Measure kmer frequency in the genome and save as a dictionary
def kmer_frequency(kmer_dataset):
        coverage_frequency = {}
        for coverage in kmer_dataset.values():
            try:
                coverage_frequency[coverage] += 1
            except KeyError:
                coverage_frequency[coverage] = 1
        return coverage_frequency

#Using kmer_count and kmer_frequency function to count the kmers and frequency
df=kmer_count(args.fasta, args.kmer_size)
df1= kmer_frequency(df)

with open('kmer_frequency.txt','w') as data: 
      data.write(str(df1))
with open('kmer_count.txt','w') as data:
      data.write(str(df))

#Transform kmer to a dataframe for plotting kmer spectra
test=pd.DataFrame(df1.items())
test1=test[test[0]< args.x_lim]
plt.bar(test1[0],test1[1],color='g', width =1)
plt.ylabel('Frequency of appearance')
plt.xlabel('Number of k-mers')
plt.title(args.title)

plt.savefig('kmer_spectra.png', dpi=900, bbox_inches='tight')


args = parser.parse_args()
