#!/usr/bin/python3

import sys
import matplotlib.pyplot as pyplot
import seaborn as sns

import pandas as pd
import numpy
import common

def lengthDistribution(list):
    pass

def baseContribution(reads):
    max_length = 0
    for sequence in reads:
        length = len(sequence)
        if length > max_length:
            max_length = length
    result = pd.DataFrame(columns = ['pos', 'rate', 'base'])
    for i in range(max_length-1):
        count = {'A':0, 'T':0, 'C':0, 'G':0, 'N':0}
        read_number = 0
        for sequence in reads:
            if len(sequence) - 1 < i:
                continue
            count[sequence[i]] += 1
            read_number += 1
        result = result.append({'pos':i, 'rate':count['A'], 'base':'A'}, ignore_index=True)
        result = result.append({'pos':i, 'rate':count['T'], 'base':'T'}, ignore_index=True)
        result = result.append({'pos':i, 'rate':count['C'], 'base':'C'}, ignore_index=True)
        result = result.append({'pos':i, 'rate':count['G'], 'base':'G'}, ignore_index=True)
        result = result.append({'pos':i, 'rate':count['N'], 'base':'N'}, ignore_index=True)
    return(result)
        # sns.lineplot(x = "idx", y = "rate", hue = "base")