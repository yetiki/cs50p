"""
Final Project: Chemical Spectra Sonifier

This program converts chemical spectroscopic data (FTIR, Raman, or Mass Spec)
into an audible experience using the strauss library. It parses 1D spectral data
from TXT files, identifies key peaks, and uses the strauss.Spectraliser and 
strauss.Generator modules to render these peaks as a musical chord or an evolving
soundscape.

x corresponds to wavenumber (cm^-1) or m/z ratio, and y corresponds to intensity.

Usage:
    python project.py <input_filename> --method <chord|evolving>
    Optional arguments:
        --smoothing_window <int>: Window length for Savitzky-Golay smoothing (default: 5)
        --smoothing_poly_order <int>: Polynomial order for Savitzky-Golay smoothing (default: 2)
        --peaks <int>: Number of peaks to sonify (default: all detected peaks)

"""
import argparse
import os
import sys
from typing import Any, List, Tuple

import numpy as np
from scipy.signal import find_peaks, savgol_filter

def load_spectrum(filename: str) -> Tuple[np.ndarray, np.ndarray]:
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
            # Skip empty lines
            if not line.strip():
                continue

            # Split line into parts
            parts = line.strip().split(',')

            if len(parts) != 2:
                # Skip lines that do not have exactly two columns
                continue

            try:
                x_val = float(parts[0])
                y_val = float(parts[1])
                x.append(x_val)
                y.append(y_val)

            except ValueError:
                # Skip lines with non-numeric data
                continue

    return np.asarray(x), np.asarray(y)

def main() -> None:
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Chemical Spectra Sonifier")

    # Required argument: input filename
    parser.add_argument("input_filename", type=str,
                        help="Path to the input spectrum file (.csv or .txt)")

    # Optional arguments
    parser.add_argument("--method", type=str, choices=["chord", "evolving"], default="chord",
                        help="Sonification method: 'chord' for strauss.Spectraliser, 'evolving' for strauss.Generator")
    
    parser.add_argument("--smoothing_window", type=int, default=5, 
                        help="Window length for Savitzky-Golay smoothing (must be odd integer)")
    
    parser.add_argument("--smoothing_poly_order", type=int, default=2, 
                        help="Polynomial order for Savitzky-Golay smoothing (must be odd integer)")
    
    parser.add_argument("--peaks", type=int, default=None,
                        help="Number of peaks to sonify (default: all detected peaks)")
    
    args: List[Any] = parser.parse_args()        

    # Load spectrum data
    try:
        x, y = load_spectrum(args.input_filename)

    except ValueError as e:
        sys.exit(e)

    else:
        sys.exit("Spectrum loaded successfully.")


    smoothed_y: np.ndarray = savgol_filter(y, args.smoothing_window, polyorder=args.smoothing_poly_order)

    # Identify peaks
    peaks, _ = find_peaks(smoothed_y, height=np.mean(smoothed_y) + np.std(smoothed_y))
    peak_x: np.ndarray = x[peaks]

    # Sonification
    if args.method == "chord":
        # Use strauss.Spectraliser for chord sonification
        pass
    elif args.method == "evolving":
        # Use strauss.Generator for evolving soundscape
        pass



if __name__ == "__main__":
    main()