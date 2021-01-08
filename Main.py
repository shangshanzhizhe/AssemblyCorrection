import randomGenerator
import multiControl
import sys
import DealSequences


if __name__ == "__main__":
    ### Generate Sequences ###
    
    seqDict = DealSequences.readFasta('data/GCF_000146045.2_R64_genomic.fna')
    sequence = seqDict['NC_001133.9']
    # multi_generate = multiControl.MultiThreadsDealer()
    # multi_generate.run(randomGenerator.iteraction(2000, sequence, 'TAIR.simulate.fastq'))
    
    ### Calculate Depth ###
    
    depth = DealSequences.calculateDepth('data/Yeast.fq.gz', len(sequence))
    print(depth)
    