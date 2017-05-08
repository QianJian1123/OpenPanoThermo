# Input: location of FLIR thermo images which comprise the panorama
# Output: a color normalized panorama of the thermo images
#
# Options:
#  -o specify location of output file
#  -k don't clean up hidden and temprorary files (keep them)
import argparse
from subprocess import check_call

# local imports
import ThermoNormalizer.NormalizeFLIRThermoImages as normalize

def run():
    print args
    normalize.process_files(args.path)

if __name__ == "__main__":
    # parse command line arguments
    parser = argparse.ArgumentParser(description='thermographic panorama pipeline')
    parser.add_argument('path', default='.')
    parser.add_argument('--output', '-o', default='./out.jpg', help='output filepath')
    parser.add_argument('--keep', '-k', action='store_false', help='keep hidden and temporary files')
    args = parser.parse_args()

    # run the scripts in the pipeline
    run()
