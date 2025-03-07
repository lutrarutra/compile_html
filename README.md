# pyproject_template
Template repository for python modules/tools supporting pyproject.toml and conda recipe

## Installation
- pip:
    ```bash
    pip install -e .
    ```

## Usage (demo)
- cli:
    ```bash
    test_cli --help
    ```
- python:
    ```python
    from demo_module.test import test_function
    test_function()
    ```

## Create conda package

### Prerequisites
- `conda install conda-build anaconda-client`

```bash
conda build purge
build_path=$(conda build --output .)
conda build --debug .
anaconda upload "$build_path"
```

## Considerations
 - Make sure that `dependencies` in `pyproject.toml` match with `run requirements` in `conda.recipe/meta.yaml`

