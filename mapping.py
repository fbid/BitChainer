from os import walk, path
from sys import exit

def _mapping(_path):

    sample_list = [];

    for paths,dirs,files in walk(_path):

        for sample in files:
            # For each sample in the current folder

            if sample.endswith('.wav') or sample.endswith('.aiff'):
                sample_path = path.join(paths,sample)
                sample_list.append(sample_path)

            elif not sample.startswith('.'):
                # sample is not hidden='.*' nor *.wav, *.aiff
                err_str = 'INVALID FILE EXTENSION for file: ' + sample.split(path_slash)[-1]
                exit(err_str)

    return sample_list
