from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import random
from config import *


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


def send(date1, num11, time11, price11, num12, time12, price12, date2, num21, time21, price21, num22, time22, price22,
         date3, num31, time31, price31, num32, time32, price32):
    client = WeChatClient(app_id, app_secret)
    wm = WeChatMessage(client)
    # {{dPlace.DATA}} ✈ {{aPlace.DATA}}
    data = {"dPlace": {"value": dCity, "color": get_random_color()},
            "aPlace": {"value": aCity, "color": get_random_color()},
            "date1": {"value": date1, "color": get_random_color()},
            "num11": {"value": num11, "color": get_random_color()},
            "time11": {"value": time11, "color": get_random_color()},
            "price11": {"value": price11, "color": get_random_color()},
            "num12": {"value": num12, "color": get_random_color()},
            "time12": {"value": time12, "color": get_random_color()},
            "price12": {"value": price12, "color": get_random_color()},

            "date2": {"value": date2, "color": get_random_color()},
            "num21": {"value": num21, "color": get_random_color()},
            "time21": {"value": time21, "color": get_random_color()},
            "price21": {"value": price21, "color": get_random_color()},
            "num22": {"value": num22, "color": get_random_color()},
            "time22": {"value": time22, "color": get_random_color()},
            "price22": {"value": price22, "color": get_random_color()},

            "date3": {"value": date3, "color": get_random_color()},
            "num31": {"value": num31, "color": get_random_color()},
            "time31": {"value": time31, "color": get_random_color()},
            "price31": {"value": price31, "color": get_random_color()},
            "num32": {"value": num32, "color": get_random_color()},
            "time32": {"value": time32, "color": get_random_color()},
            "price32": {"value": price32, "color": get_random_color()},
            }
    res = wm.send_template(user_id, template_id, data)
    # res2 = wm.send_template(user_id2, template_id, data)
    print(res)
    # print(res2)
