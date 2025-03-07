import argparse

from . import __version__
from .compile import make_standalone_html


def main() -> int:
    parser = argparse.ArgumentParser(description="Embeds CSS, JS, and images into a single HTML file.")
    parser.add_argument("-i", "--source", type=str, required=True, help="The folder containing the assets.")
    parser.add_argument("-o", "--output", type=str, required=True, help="The output HTML file.")
    parser.add_argument("--entry", type=str, default="index.html", help="The main HTML file to inline assets into.")
    args = parser.parse_args()

    print(f"compile_html: v{__version__}")
    
    try:
        make_standalone_html(source_folder=args.source, output_file=args.output, main_html=args.entry)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())