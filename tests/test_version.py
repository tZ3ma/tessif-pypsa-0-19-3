# tests/test_version.py
"""Examplary test package to test version related issues."""
from tessif_pypsa_0_19_3 import __version__


def test_verssion_access():
    """Test for correct package version."""
    assert __version__ == "0.1.1"
