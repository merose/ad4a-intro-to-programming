"""Generate PDF from Markdown files based on a configuration."""

import os
import yaml
from argparse import ArgumentParser
from pathlib import Path

from markdown_pdf import (
    MarkdownPdf,
    Section
)


def main():
    parser = ArgumentParser(description='Create PDF from Markdown files')
    parser.add_argument('config', help='YAML configuration file')
    parser.add_argument('result', help='PDF result file')
    args = parser.parse_args()

    with open(args.config) as infile:
        config = yaml.safe_load(infile)

    base_dir = Path(args.config).parent.absolute()
    docs_dir = base_dir / 'docs'
    result_path = Path(args.result).absolute()

    # Move to the config directory so relative links work.
    os.chdir(base_dir)
    pdf = MarkdownPdf(toc_level=3, optimize=True)
    for f in config['nav']:
        if isinstance(f, str):
            file_path = docs_dir / f
        else:
            file_path = docs_dir / list(f.values())[0]
        print(f'Adding file {file_path}')
        with open(file_path) as infile:
            text = infile.read()
        pdf.add_section(Section(text))
    print(f'Writing result to {result_path}')
    with open(result_path, 'w') as outfile:
        pdf.save(outfile)
