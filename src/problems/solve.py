import sys
import code.problem345

def main(argv):
    inputfile = open(argv[0], 'r')
    outputfile = open(argv[1], 'w')
    
    # Process the text
    code.problem345.solve(inputfile, outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
