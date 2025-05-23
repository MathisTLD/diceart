# diceart

Create images using dices

<div style="display: flex; justify-content: space-around; flex-direction: row;">
  <div>
    <p style="text-align: center">Original</p>
    <img src="tests/data/robert_smith-2-1.jpg" width="200"/>
  </div>
  <div>
    <p style="text-align: center">Dice Art</p>
    <img src="tests/data/robert_smith-2-1.diceart.png" width="200"/>
  </div>
</div>

## Usage

```bash
# clone the repo
git clone https://github.com/MathisTLD/diceart.git
# cd to the project's root
cd diceart
# install deps and activate virtual env
pixi shell
# check help
diceart --help
# convert an image
diceart ./tests/data/robert_smith-1.jpg
```

## Development

### Pixi

This project uses [pixi](https://pixi.sh/) to manage the development environment.

To install all dependencies, run `pixi install`.

To activate the virtual environment, run `pixi shell`.

> **⚠️ ATTENTION** according to [the doc](https://pixi.sh/dev/features/environment/#caching-packages), pixi's cache will more likely be stored in your home directory by default. If you only have limited disk space available, you should set the `PIXI_CACHE_DIR` or `RATTLER_CACHE_DIR` to relocate this cache somewhere else.

#### VSCode

To use the virtual environment in VSCode, you can use the [Pixi VSCode extension](https://marketplace.visualstudio.com/items?itemName=jjjermiah.pixi-vscode). Then use the `Pixi: Set Python Interpreter` command to select the virtual environment.

Alternatively, using `"python.defaultInterpreterPath": "${workspaceFolder}/.pixi/envs/default/bin/python"` in [.vscode/settings.json](.vscode/settings.json) an then clicking `` Use Python from `python.defaultinterpreterPath` setting python `` after running the `Python: Select Interpreter` command should also work.

#### Tasks

Pixi allows you to define tasks (see [doc](https://pixi.sh/latest/features/advanced_tasks/)). To run a task, use `pixi run <task>`. For example, to run the `test` task, use `pixi run test`.

The following tasks are defined. Use `pixi task list` to list all available tasks:

- `test`: Runs `mypy` to check typing (only in the [src](src) directory) and `pytest` to run tests (see [testing](#testing)).

### Testing

Tests are run using [pytest](https://docs.pytest.org/). To run the tests, run `pytest ./tests` in the root of the project. See [the documentation](https://docs.pytest.org/en/stable/) for more information.
