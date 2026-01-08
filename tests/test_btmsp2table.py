"""Tests for btmsp2table module."""

import pytest
from btmsp2table import extract_spectrum_table


def test_extract_spectrum_table_not_implemented():
    """Test that extract_spectrum_table raises NotImplementedError."""
    with pytest.raises(NotImplementedError, match="not yet implemented"):
        extract_spectrum_table("dummy_file.btmsp")
