import azure.functions as func
import logging

# comment the below import to successfully deploy with PYTHON_ISOLATE_WORKER_DEPENDENCIES=1
import newrelic.agent

app = func.FunctionApp()


@app.function_name(name="HttpExample")
@app.route(
    route="hello",
    auth_level=func.AuthLevel.ANONYMOUS,
)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    return func.HttpResponse("HttpExample function processed a request!")
