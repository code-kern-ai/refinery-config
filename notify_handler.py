from typing import Dict

import requests
import traceback


def notify_others_about_change(notify: Dict[str, str]) -> None:

    for key in notify:
        url = f"{notify[key]}/config_changed"
        try:
            response = requests.put(url)
            if response.status_code != 200:
                print("couldn't notify ", key)
        except requests.exceptions.ConnectionError:
            print("couldn't notify ", key)
        except Exception:
            print(traceback.format_exc(), flush=True)
