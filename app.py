from fastapi import FastAPI, responses, status
from pydantic import BaseModel
from config_handler import init_config, get_config, change_config, SERVICES_TO_NOTIFY
import json
from notify_handler import notify_others_about_change_thread


init_config()
app = FastAPI()
notify_others_about_change_thread(SERVICES_TO_NOTIFY)


class ChangeRequest(BaseModel):
    dict_string: str


@app.post("/change_config")
def change(request: ChangeRequest) -> responses.PlainTextResponse:
    if change_config(json.loads(request.dict_string)):
        notify_others_about_change_thread(SERVICES_TO_NOTIFY)
    return responses.PlainTextResponse(status_code=status.HTTP_200_OK)


@app.get("/full_config")
def full_config() -> responses.JSONResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK, content=get_config(False)
    )


@app.get("/base_config")
def base_config() -> responses.JSONResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK, content=get_config(True)
    )


@app.get("/healthcheck")
def healthcheck() -> responses.PlainTextResponse:
    return responses.PlainTextResponse("OK")
