# HTML to PNG/PDF Converter

A command-line utility to convert HTML files to PNG or PDF format using Playwright for rendering and capturing.

## Features

- Convert any HTML file to PNG or PDF format
- Customizable viewport dimensions
- Adjustable wait time to ensure JavaScript execution completes
- Full-page screenshots for PNG output
- PDF output in A4 format

## Prerequisites

- Python 3.6+
- Playwright

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/html-converter.git
cd html-converter
```

2. Install the required packages:
```bash
pip install playwright
```

3. Install the Playwright browser binaries:
```bash
python -m playwright install chromium
```

## Usage

```bash
python html_converter.py --input <html_file_path> --output <output_file_path> --format <png|pdf>
```

### Arguments

| Argument | Short | Required | Default | Description |
|----------|-------|----------|---------|-------------|
| `--input` | `-i` | Yes | N/A | Path to input HTML file |
| `--output` | `-o` | Yes | N/A | Path to output file (PNG or PDF) |
| `--format` | `-f` | No | `pdf` | Output format (`png` or `pdf`) |
| `--width` | `-w` | No | `1200` | Viewport width in pixels |
| `--height` | `-ht` | No | `900` | Viewport height in pixels |
| `--wait` | N/A | No | `2` | Wait time in seconds for JavaScript rendering |

### Examples

Convert an HTML file to PNG:
```bash
python html_converter.py --input page.html --output page.png --format png
```

Convert an HTML file to PDF with custom dimensions and longer wait time:
```bash
python html_converter.py --input dashboard.html --output dashboard.pdf --width 1600 --height 1200 --wait 5
```

## Troubleshooting

If you encounter an error like "Please make sure you have Chrome installed", try:

1. Make sure you've installed Playwright's browser binaries:
```bash
python -m playwright install chromium
```

2. Check that the input HTML file exists and is accessible.

3. Ensure you have proper write permissions for the output directory.

## How It Works

This utility uses Playwright to:

1. Launch a headless Chromium browser
2. Navigate to the local HTML file
3. Wait for the specified amount of time for any JavaScript to execute
4. Capture the content as either PNG (screenshot) or PDF
5. Save the output to the specified location


## License

This project is licensed under the MIT License - see the LICENSE file for details.
