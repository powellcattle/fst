import datetime

def to_pos_int_or_none(_str: str) -> int:
    try:
        integer = int(_str)
    except ValueError:
        return None
    else:
        return integer


def to_boolean_or_none(_str: str) -> bool:
    tf = None
    try:
        if _str.upper() == "TRUE":
            tf = True
        else:
            tf = False

    except ValueError:
        return None
    else:
        return tf


def to_pos_long_or_none(_str: str) -> int:
    try:
        lng = int(_str)
    except ValueError:
        return None
    else:
        return lng


def to_upper_or_none(_str: str) -> str:
    if _str is None or len(_str.strip()) == 0:
        return None
    else:
        return str(_str.strip().upper())


def to_date_or_none(_str: str, _format="%m/%d/%Y") -> datetime:
    try:
        date = datetime.datetime.strptime(_str, _format)
    except ValueError:
        return None
    else:
        return date


def to_float_or_none(_str: str) -> float:
    try:
        flt = float(_str)
    except ValueError:
        return None
    else:
        return flt
