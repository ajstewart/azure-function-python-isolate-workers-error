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

## Reproducing the issue

1. Create the function app and other related resources.
2. Update the function app settings and add the `PYTHON_ISOLATE_WORKER_DEPENDENCIES=1` setting.
3. Attempt to deploy this function using the CLI `func azure functionapp publish <FUNC_NAME>`.

### Expected behavior

The function app should deploy successfully.

### Actual behavior

Fails to sync after deployment:

```terminal
Deployment successful. deployer = Push-Deployer deploymentPath = Functions App ZipDeploy. Extract zip. Remote build.
Remote build succeeded!
[2023-10-31T12:38:51.074Z] Syncing triggers...
[2023-10-31T12:39:02.129Z] Syncing triggers...
[2023-10-31T12:39:08.238Z] Syncing triggers...
[2023-10-31T12:39:13.464Z] Syncing triggers...
[2023-10-31T12:39:18.238Z] Syncing triggers...
[2023-10-31T12:39:22.567Z] Syncing triggers...
Error calling sync triggers (BadRequest). Request ID = '0662ffb0-1263-4b14-9240-84a47bd1a202'.
```

### Workaround

Either:

* remove the `PYTHON_ISOLATE_WORKER_DEPENDENCIES` app setting and redeploy, or
* comment out the `import newrelic.agent` line in `function_app.py`.
