# -*- encoding: utf-8 -*-
import action

infos = {
    "phone": "13355379535",
    "password": "9103b4e46d7aa692e7e98f36ebf7d778",
    # "sc_key": ["XXXX"],
    # "tg_bot_key": ["XXXX", "XXXXX"],
    # "bark_key": ["XXXX"],
    # "wecom_key": ["XXXX", "XXXX", "XXXX"],
     "push_plus_key": ["35629a7229e340f196f353a7fef0878a"],
}


def main_handler(event, context):
    action.task_pool(infos)


if __name__ == "__main__":
    main_handler("", "")
