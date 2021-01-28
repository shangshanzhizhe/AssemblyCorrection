import sys
sys.path.append('src')
import randomGenerator
import multiControl
import DealSequences
import Statistics
    
if __name__ == "__main__":
    reference = DealSequences.readFasta('data/TAR10.1.OMOL01000003.1.fa')['OMOL01000003.1']
    randomGenerator.iteraction(1, reference, 'data/TAIR.1.contig.simulate.fastq')
    