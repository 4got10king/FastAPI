from enum import Enum


class OrderStatus(str, Enum):
    In_procces = "In_procces"
    Send = "Send"
    Done = "Done"
    