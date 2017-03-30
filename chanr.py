import os, shutil, sys, sox
from OSSniffer import path_slash
from setup import src_path, out_path
from setup import NORMALIZE, SILENCE, PADDING, INDIVIDUAL_SAMPLES
from utility import _removeVowels

# -- Global variabiles
samples = [];
processed_samples = []

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

def _renameSample(sample_path):

    # Extract sample name
    sample_name = sample_path.split(path_slash)[-1]

    #remove .wav or .aiff extension from the sample name
    sample_name = sample_name.split('.')[0]

    #lowercase conversion
    sample_name.lower()

    #remove vowels from sample name
    sample_name = _removeVowels(sample_name)

    #space removal
    sample_name = sample_name.replace(' ', '_');


    # append extension
    sample_name += '.wav'

    return sample_name

def _processSamples(sample_list):

    for sample in sample_list:

        # Rename
        sample_new_name = _renameSample(sample)

        # Join output path with new name
        _out = os.path.join(out_path,sample_new_name)

        # Saves the file path in the processed samples list
        processed_samples.append(_out);

        _in = sample

        # Lettura file e Conversione
        tfm = sox.Transformer()

        tfm.convert(samplerate=44100, n_channels=2, bitdepth=16)

        if NORMALIZE:
            tfm.norm(db_level=-3)

        if SILENCE:
            tfm.silence(location=-1,silence_threshold=0.05, min_silence_duration=0.1 )

        if PADDING:
            tfm.pad(0,PADDING)


        tfm.build(_in,_out)

def _concatSamples(sample_list, output_chain_name):

    output_chain_name += '.wav'

    cbn = sox.Combiner()

    cbn.build(sample_list, os.path.join(out_path,output_chain_name) , 'concatenate')

def _removeIndividualSamples(samples):

    for file in samples:
        os.remove(file)


# -- MAIN

# Mapping samples
_mapping(src_path)

# Create new folder with Album_Title name
if not os.path.exists(out_path):
    os.makedirs(out_path)

# Ask the user how he wants to call the sample chain
chain_name = raw_input('How do you wanna call the sample chain? : ')

# Sample processing & output
_processSamples(samples)

# Sample concatenation
_concatSamples(processed_samples, chain_name)

# Remove the individual samples before the chain is created
if not INDIVIDUAL_SAMPLES:
    _removeIndividualSamples(processed_samples)
