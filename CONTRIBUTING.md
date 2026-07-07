# Contributing

Please refer to the [DKPro Contribution Guidelines](https://dkpro.github.io/contributing) that govern all subprojects of INCEpTION.

## How to work on Pycaprio

### Setup your workplace

Fork the repository into your account and clone it in your work station.

To work on `pycaprio`, you will need Python 3.9+ and [uv](https://docs.astral.sh/uv/) installed.

Common development tasks are defined as [taskipy](https://github.com/taskipy/taskipy) tasks in `pyproject.toml`
and are run through `uv run task <name>`.

### Installing the dependencies

`uv` manages the virtual environment for you. To install both dev and prod dependencies, run:

```
uv sync --all-groups
```

At this point, you should have everything ready to start developing, but what is developing without tests...

### Run tests and the linter

This project has both unit tests and integration tests. Unit tests are fine to run in isolation by
just `uv run task unit-tests`.

You will need to then create an user there and enable `REMOTE_API` permissions.

The username and password should be `test-remote`, although you can override those values by using the
`TEST_USERNAME` and `TEST_PASSWORD` env variables.

To run the integration tests use: `uv run task integ-tests`

To run all tests use: `uv run task test`

To run the linter: `uv run task lint`

### Documentation

There's a [docs](https://github.com/JavierLuna/pycaprio/tree/main/docs) directory that contains all `pycaprio`'s
documentation.

You may add/change the files there if your contribution requires so.

To compile the documentation and serve them in a local webserver, do `uv run task docs`.

