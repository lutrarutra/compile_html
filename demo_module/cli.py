import argparse

import demo_module

def main() -> int:
    parser = argparse.ArgumentParser(description="Template Project")

    args = parser.parse_args()
    print(f"Hello, World from '{demo_module.__name__}'!")
    print(f"Version: v{demo_module.__version__}")

    return 0

if __name__ == "__main__":
    exit(main())

