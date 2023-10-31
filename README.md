# Python Azure Function PYTHON_ISOLATE_WORKER_DEPENDENCIES Error

This repository is a minimal example for the issue described here: <https://github.com/Azure/azure-functions-python-worker/issues/1339>

## Deployment

* Python 3.10
* Linux Consumption Plan
* Python V2 Programming Model

## App Settings

The only app setting required is:

* `PYTHON_ISOLATE_WORKER_DEPENDENCIES`: `1`

which is what causes the issue.
