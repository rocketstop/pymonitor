from typing import Dict


def human_readable_bytes(num: int) -> str:
    """
    Converts number to human-readable format (MB, GB, TB)
    :param num:
    :return string representing human-readable size:
    """
    step_unit: int = 2 ** 10

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit


def get_attribute(target: object, attribute: str, to_human_readable=False) -> str:
    """
    return string representing value of supplied attribute on given object
    :param target:
    :param attribute:
    :param to_human_readable: default to false, true to convert value to human readable byte sizes (KB, GB, etc)
    :return:
    """
    if target is not None:
        value = getattr(target, attribute)
    return human_readable_bytes(value) if to_human_readable else value


def dict_to_string(target: Dict) -> str:
    """
    Builds string from k,v in dictionary
    :param target:
    :return:
    """
    value: str = ""
    for k, v in target.items():
        value += k+": {" + str(v) + "} "
    return value
