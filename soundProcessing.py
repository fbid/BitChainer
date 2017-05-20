from os.path import join
from sox import Transformer, Combiner
from utility import _renameSample, _removeIndividualSamples
from setup import out_path
from setup import NORMALIZE, SILENCE, PADDING, INDIVIDUAL_SAMPLES

# Processed samples list
processed_samples = []

def _processAndConcat(sample_list):
    chain_name = raw_input('How do you wanna call the sample chain? : ')
    _processSamples(sample_list)
    _concatSamples(sample_list, chain_name)

def _processSamples(sample_list):

    for sample in sample_list:

        sample_new_name = _renameSample(sample)
        _out = join(out_path,sample_new_name)
        processed_samples.append(_out);
        _in = sample

        # Sox processing using Transform instance
        tfm = Transformer()
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

    cbn = Combiner()
    cbn.build(sample_list, join(out_path,output_chain_name) , 'concatenate')

    # Remove the individual samples before the chain is created
    if not INDIVIDUAL_SAMPLES:
        _removeIndividualSamples(processed_samples)
