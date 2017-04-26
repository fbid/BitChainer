from mapping import _mapping as _map
from setup import src_path, out_path
from soundProcessing import _processAndConcat as _proc
from os.path import exists
from os import makedirs

def main():
    samples = _map(src_path)

    if not exists(out_path):
        makedirs(out_path)

    _proc(samples)

main()
