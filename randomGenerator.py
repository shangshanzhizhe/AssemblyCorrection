#!/usr/bin/python3

import sys, random
import re
import DealSequences
import multiControl

def randomError(base):
    base = DealSequences.dealRareBase(base)
    if base == 'N':
        return base
    else:
        bases = {'A':1, 'T':1, 'C':1, 'G':1}
        prob = random.uniform(0.05, 0.15)
        number = random.randint(1,100)
        if number / 100 <= prob:
            del bases[base]
            new =  list(bases.keys())[random.randint(0,2)]
            return(new)
        else:
            return(base)


def GetRandomSeq(reference):
    length = random.randint(2000, len(reference))
    start = random.randint(0, len(reference) - 1)
    end = start + length

    if end > len(reference) - 1:
        end = len(reference) - 1
    
    sequence = reference[start:end]
    directionMarker = random.randint(0, 1)
    sequence_list = []
    for i in iter(sequence):
        sequence_list.append(randomError(i))
    sequence = ''.join(sequence_list)
    if directionMarker == 1:
        sequence = DealSequences.reverseSeq(sequence)
    return(sequence)

def iteraction(number, reference, outfile):
    i = 1
    out = open(outfile,'w')
    while i <= iteraction:
        randomSequence = GetRandomSeq(reference)
        if randomSequence == '':
            continue
        print(randomSequence, file = out)
        i += 1