import azure.functions as func
import logging
import newrelic.agent

app = func.FunctionApp()


newrelic.agent.initialize()
newrelic.agent.register_application(timeout=2)


@app.function_name(name="HttpExample")
@app.route(
    route="hello",
    auth_level=func.AuthLevel.ANONYMOUS,
)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    application = newrelic.agent.application()
    newrelic.agent.record_custom_event(
        "CustomEvent",
        {"key": "value"},
        application,
    )
    return func.HttpResponse("HttpExample function processed a request!")
