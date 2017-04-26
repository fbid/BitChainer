from mapping import _mapping
from setup import src_path, out_path
from soundProcessing import _processAndConcat
from os.path import exists
from os import makedirs


def main():
    # Mapping samples
    samples = _mapping(src_path)

    # Create new folder with Album_Title name
    if not exists(out_path):
        makedirs(out_path)

    # Sample processing, concatenation & output
    _processAndConcat(samples)


main()
