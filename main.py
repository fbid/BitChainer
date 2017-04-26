import os, shutil, sys
from setup import src_path, out_path
from soundProcessing import _processAndConcat

# -- Samples List
samples = [];

# -- Procedures

def _mapping(_path):

    for paths,dirs,files in os.walk(_path):

        i = 0

        for sample in files:

            # For each sample in the current folder

            if sample.endswith('.wav') or sample.endswith('.aiff'):

                sample_path = os.path.join(paths,sample)

                samples.append(sample_path)

                i += 1

            elif not sample.startswith('.'):
                # . is to ignore hidden files

                err_str = 'INVALID FILE EXTENSION for file: ' + sample.split(path_slash)[-1]
                sys.exit(err_str)


 # MAIN

# Mapping samples
_mapping(src_path)

# Create new folder with Album_Title name
if not os.path.exists(out_path):
    os.makedirs(out_path)

# Sample processing, concatenation & output
_processAndConcat(samples)
