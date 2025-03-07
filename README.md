# pyproject_template
- From pyproject template: [github.com/lutrarutra/pyproject_template](https://github.com/lutrarutra/pyproject_template)

## Installation
- pip:
    ```bash
    pip install -e .
    ```
- conda:
    ```bash
    conda install lutrarutra::compile_html
    ```

## Usage
- cli:
    ```bash
    compile-html -i <input_dir> -o <output_file> --entry <entry_html_file>
    ```
- python:
    ```python
    from compile_html.compile import make_standalone_html
    make_standalone_html(
        source_folder='<input_dir>',
        output_file='<output_file>',
        main_html='<entry_html_file>'
    )
    ```

