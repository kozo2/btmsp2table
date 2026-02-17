# btmsp2table

Extract the main spectrum table from Bruker's MALDI Biotyper `.btmsp` files.

> **Note:** The core extraction logic is not yet implemented. Contributions are welcome.

## Installation

Requires Python >= 3.12.

```bash
pip install btmsp2table
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv pip install btmsp2table
```

### From source

```bash
git clone https://github.com/kozo2/btmsp2table.git
cd btmsp2table
uv pip install .
```

## Usage

### Command-line interface

```bash
btmsp2table path/to/file.btmsp
```

### Python API

```python
from btmsp2table import extract_spectrum_table

result = extract_spectrum_table("path/to/file.btmsp")
```

An example `.btmsp` file is included under [`examples/`](examples/).

### API reference

#### `extract_spectrum_table(btmsp_file: str) -> dict`

Extract the main spectrum table from a `.btmsp` file.

**Parameters:**

- `btmsp_file` — Path to the `.btmsp` file.

**Returns:**

A dictionary containing the spectrum table data.

**Raises:**

- `FileNotFoundError` — If the file does not exist.
- `ValueError` — If the file format is invalid.

## Development

```bash
git clone https://github.com/kozo2/btmsp2table.git
cd btmsp2table
uv sync --dev
```

### Running tests

```bash
uv run pytest
```

## License

Apache-2.0. See [LICENSE](LICENSE) for details.
