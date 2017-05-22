from os import walk, path, chdir
from os.path import join
from sys import exit
from OSSniffer import path_slash


def _mapping(_path):

    sample_list = [];

    for paths,dirs,files in walk(_path):

        for sample in files:
            # For each sample in the current folder

            if sample.endswith('.wav') or sample.endswith('.aiff'):
                sample_path = join(paths,sample)
                sample_list.append(sample_path)

            elif not sample.startswith('.'):
                # sample is not hidden='.*' nor *.wav, *.aiff
                err_str = 'ERROR! Invalid file extension for file: ' + sample.split(path_slash)[-1]
                err_str += '\nRemove the file and launch the script again.\n'
                exit(err_str)

    return sample_list
