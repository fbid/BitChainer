from os import remove
from OSSniffer import path_slash

def _renameSample(sample_path):

    # Extract sample name
    sample_name = sample_path.split(path_slash)[-1]
    #remove .wav or .aiff extension from the sample name
    sample_name = sample_name.split('.')[0]

    sample_name = sample_name.replace(' ', '_');
    sample_name.lower()
    sample_name += '.wav'

    return sample_name

def _removeIndividualSamples(samples):
    for file in samples:
        remove(file)
