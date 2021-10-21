import sys
from io import StringIO
from pyenf_extraction.pyenf import pyENF

def extract_enf_signal(wav_file_path):
    mysignal = pyENF(filename=wav_file_path, nominal=50, harmonic_multiples=8, duration=0.1, strip_index=0)
    x, fs = mysignal.read_initial_data()
    spectro_strip, frequency_support = mysignal.compute_spectrogam_strips()
    
    sys.stdout = StringIO()
    weights = mysignal.compute_combining_weights_from_harmonics()
    sys.stdout = sys.__stdout__

    OurStripCell, initial_frequency = mysignal.compute_combined_spectrum(
        spectro_strip, weights, frequency_support
    )

    return mysignal.compute_ENF_from_combined_strip(OurStripCell,initial_frequency)
