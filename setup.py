# SETUP
# pip install sox

# -- CONFIG VARIABLES

import ConfigParser, os

config = ConfigParser.ConfigParser()
config.readfp(open(r'config.txt'))

# Get current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

src_path = os.path.join(current_dir,config.get('Config', 'source_directory'))
out_path = os.path.join(current_dir,config.get('Config', 'output_directory'))

NORMALIZE = config.get('Config', 'normalize')
SILENCE = config.get('Config', 'cut_silence')
PADDING = config.get('Config', 'sample_padding')
INDIVIDUAL_SAMPLES = config.get('Config', 'individual_samples')

def _onOfftoBool(param):
    if param == 'on':
        return True
    else:
        return False


NORMALIZE = _onOfftoBool(NORMALIZE)
SILENCE = _onOfftoBool(SILENCE)
INDIVIDUAL_SAMPLES = _onOfftoBool(INDIVIDUAL_SAMPLES)
