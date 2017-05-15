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
    check_call('mkdir thermo_images_temp_file', shell=True)
    normalize.process_files(relevant_path=args.path, normalize=True, output_path='./thermo_images_temp_file')
    check_call('cd src && make', shell=True)
    check_call('cd src && ./image-stitching ../thermo_images_temp_file/*', shell=True)

    # remove temporary files unless otherwise specified
    if not args.keep:
        check_call('rm ./thermo_images_temp_file/*', shell=True)
        check_call('rmdir thermo_images_temp_file', shell=True)

    check_call('mv ./src/out.jpg ' + args.output, shell=True)
    

if __name__ == "__main__":
    # parse command line arguments
    parser = argparse.ArgumentParser(description='thermographic panorama pipeline')
    parser.add_argument('path', default='.')
    parser.add_argument('--output', '-o', default='./out.jpg', help='output filepath')
    parser.add_argument('--keep', '-k', action='store_true', help='keep hidden and temporary files')
    args = parser.parse_args()

    # run the scripts in the pipeline
    run()
