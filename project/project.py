"""
Final Project: Chemical Spectra Sonifier (CSS)

This program converts chemical spectroscopic data (FTIR, Raman, or Mass Spec)
into an audible experience using the strauss library. It parses 1D spectral data
from TXT files, identifies key peaks, and uses the strauss.Spectraliser and 
strauss.Generator modules to render these peaks as a musical chord or an evolving
soundscape.
"""
import argparse
import os
import sys
from typing import Any, List

# from scipy.signal import find_peaks, savgol_filter

def load_spectrum(filename: str):
    """
    Load a spectrum file (.csv or .txt) and return x and y data.
    Data files should have two columns: x (e.g., wavenumber, m/z) and y (intensity).

    Args:
        filename (str)

    Returns:
        tuple[List[float], List[float]]: (x, y)

    Raises:
        ValueError if data cannot be parsed
    """
    if not os.path.isfile(filename):
        raise ValueError(f"File {filename} does not exist.")
    
    VALID_EXTENSIONS = ['.csv', '.txt']
    _, ext = os.path.splitext(filename)
    
    if not ext.lower() in VALID_EXTENSIONS:
        raise ValueError(f"Unsupported file extension: {ext}. Supported extensions are: {VALID_EXTENSIONS}")
    
    x, y = [], []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 2:
                continue
            try:
                x_val = float(parts[0])
                y_val = float(parts[1])
                x.append(x_val)
                y.append(y_val)
            except ValueError:
                continue
    return x, y

def main() -> None:
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Chemical Spectra Sonifier (CSS)")
    parser.add_argument("input_filename", type=str, help="Path to the input spectrum file (.csv or .txt)")
    parser.add_argument("--method", type=str, choices=["chord", "evolving"], default="chord",
                        help="Sonification method: 'chord' for strauss.Spectraliser, 'evolving' for strauss.Generator")
    parser.add_argument("--smoothing", type=int, default=5, 
                        help="Window length for Savitzky-Golay smoothing (must be odd integer)")
    args: List[Any] = parser.parse_args()        

    # Load spectrum data
    try:
        x, y = load_spectrum(args.input_filename)
    except ValueError as e:
        print(e)
        sys.exit()

    print('Success!')



if __name__ == "__main__":
    main()