from fastapi import FastAPI
from pydantic import BaseModel
from config_handler import init_config, get_config, change_config
import json

from notify_handler import notify_others_about_change


init_config()
app = FastAPI()


class ChangeRequest(BaseModel):
    dict_string: str


@app.post("/change_config")
def change(request: ChangeRequest) -> int:
    if change_config(json.loads(request.dict_string)):
        notify_others_about_change(get_config(False)["services_to_notify"])
    return 200, None


@app.get("/full_config")
def full_config() -> str:
    return json.dumps(get_config(False))


@app.get("/base_config")
def base_config() -> str:
    return json.dumps(get_config(True))
