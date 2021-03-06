#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from Bio import SeqIO
import gzip
import re, sys

def readFasta(infile):
    seqDict = {}
    try:
        fa = open(infile, 'r')
        for record in SeqIO.parse(fa, 'fasta'):
            SeqID = record.id
            SeqSEQ = record.seq
            seqDict[SeqID] = SeqSEQ
    except IOError:
        raise("Error: No fasta file!" + infile + "!")
        
    return(seqDict)

def readFastq(infile):
    sequences = []
    qualities = []
    try:
        fq = open(infile, 'r')
        while True:
            fq.readline()
            seq = fq.readline().rstrip()
            fq.readline()
            qual = fq.readline().rstrip()
            if len(seq)==0:
                break
            sequences.append(seq)
            qualities.append(qual)
    except IOError:
        raise("Error: No fastq file" + infile + "!")
    return(sequences, qualities)

def reverseSeq(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        base = base.upper()
        t = complement[base] + t
    return t

def dealRareBase(base):
    base = base.upper()
    if base not in {'A':1, 'C':1, 'T':1, 'G':1, 'N':1}:
        return('N')
    else:
        return base

def calculateDepth(infile, genomeSize):
    file = open(infile,'r')
    length = 0
    for line in file:
        line = line.rstrip()
        length += len(line)
    return(length / genomeSize)

def covertFq2Fa(infile, outfile):
    out = open(outfile,'w')
    fq = open(infile, 'r')
    while True:
        nameLine = fq.readline().rstrip()
        seq = fq.readline().rstrip()
        fq.readline()
        qual = fq.readline().rstrip()
        if len(seq) == 0:
            break
        print('>' + nameLine, file = out)
        print(seq, file = out)
