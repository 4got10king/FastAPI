from enum import Enum


class OrderStatus(str, Enum):
    in_process = "in_process"
    send = "send"
    done = "done"
