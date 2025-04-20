"""
HTML to PNG/PDF Converter

This script converts HTML files to PNG or PDF format using either
playwright or selenium for rendering and capturing.

Usage:

python html_converter.py --input pipeline.html --output pipeline.pdf --format pdf
python html_converter.py --input pipeline.html --output pipeline.png --format png
"""

import os
import sys
import argparse
from playwright.sync_api import sync_playwright

def convert_with_playwright(input_file, output_file, format_type, width=1200, height=900, wait_time=2):
    """Convert HTML to PNG/PDF using Playwright"""
    abs_input_path = os.path.abspath(input_file)
    file_url = f"file://{abs_input_path}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(file_url)
        
        page.wait_for_timeout(wait_time * 1000)
        
        if format_type.lower() == 'pdf':
            page.pdf(path=output_file, format="A4")
        else:
            page.screenshot(path=output_file, full_page=True)
        
        browser.close()
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Convert HTML files to PNG or PDF')
    parser.add_argument('--input', '-i', required=True, help='Input HTML file path')
    parser.add_argument('--output', '-o', required=True, help='Output file path (PNG or PDF)')
    parser.add_argument('--format', '-f', choices=['png', 'pdf'], default='pdf',
                       help='Output format (png or pdf)')
    parser.add_argument('--width', '-w', type=int, default=1200, help='Viewport width')
    parser.add_argument('--height', '-ht', type=int, default=900, help='Viewport height')
    parser.add_argument('--wait', type=int, default=2, 
                        help='Wait time in seconds for JavaScript rendering')
    
    args = parser.parse_args()
    
    output_ext = os.path.splitext(args.output)[1].lower()
    if args.format == 'pdf' and not output_ext == '.pdf':
        args.output += '.pdf'
    elif args.format == 'png' and not output_ext == '.png':
        args.output += '.png'
    
    print(f"Converting {args.input} to {args.format.upper()}...")
    
    try:
        convert_with_playwright(
            args.input, args.output, args.format, 
            args.width, args.height, args.wait
        )
        print(f"Successfully converted to {args.output}")
    except Exception as e:
        print("Conversion failed. Please make sure you have Chrome installed.")
        sys.exit(1)

if __name__ == "__main__":
    main()