"""btmsp2table: Extract main spectrum table from Bruker's MALDI Biotyper .btmsp file."""

from btmsp2table.btmsp2table import extract_spectrum_table

__version__ = "0.1.0"
__all__ = ["extract_spectrum_table", "main"]


def main() -> None:
    """Command-line interface for btmsp2table."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: btmsp2table <path_to_btmsp_file>")
        print("Extract main spectrum table from Bruker's MALDI Biotyper .btmsp file")
        sys.exit(1)
    
    btmsp_file = sys.argv[1]
    
    try:
        result = extract_spectrum_table(btmsp_file)
        print(f"Successfully extracted spectrum table from {btmsp_file}")
        print(result)
    except FileNotFoundError:
        print(f"Error: File not found: {btmsp_file}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except NotImplementedError as e:
        print(f"Note: {e}", file=sys.stderr)
        print("This is a template package. Implementation needed.", file=sys.stderr)
        sys.exit(0)
