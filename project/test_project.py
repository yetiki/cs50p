from pathlib import Path
import pytest

from project import load_spectrum

def test_load_spectrum_valid_file():
    # Passes if no exception is raised for a valid file
    filename: str = Path(__file__).parent / "spectrum.txt"
    _, _ = load_spectrum(str(filename))

def test_load_spectrum_invalid_file():
    # Passes if ValueError is raised for a non-existent file
    filename: str = "non_existent_file.txt"

    with pytest.raises(ValueError):
        _, _ = load_spectrum(filename)

def test_load_spectrum_unsupported_extension():
    # Passes if ValueError is raised for unsupported file extension
    filename: str = Path(__file__).parent / "spectrum.unsupported"

    with pytest.raises(ValueError):
        _, _ = load_spectrum(str(filename))