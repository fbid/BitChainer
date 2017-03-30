import sox, os


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

        # Write final samples
        tfm.build(_in,_out)

def _concatSamples(sample_list, output_chain_name):

    output_chain_name += '.wav'

    cbn = sox.Combiner()

    cbn.build(sample_list, os.path.join(out_path,output_chain_name) , 'concatenate')
