from typing import Dict

import requests


def notify_others_about_change(notify: Dict[str, str]) -> None:

    for key in notify:
        url = f"{notify[key]}/config_changed"
        response = requests.put(url)
        if response.status_code != 200:
            print("cound't notify ", key)
