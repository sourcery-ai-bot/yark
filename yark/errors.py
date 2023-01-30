"""Exceptions and error functions"""

from colorama import Style, Fore
import sys


class ArchiveNotFoundException(Exception):
    """Archive couldn't be found, the name was probably incorrect"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class VideoNotFoundException(Exception):
    """Video couldn't be found, the id was probably incorrect"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NoteNotFoundException(Exception):
    """Note couldn't be found, the id was probably incorrect"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TimestampException(Exception):
    """Invalid timestamp inputted for note"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def _err_msg(msg: str, report_msg: bool = False):
    """Provides a red-coloured error message to the user in the STDERR pipe"""
    msg = (
        f"{msg}\nPlease file a bug report if you think this is a problem with Yark!"
        if report_msg
        else msg
    )
    print(Fore.RED + Style.BRIGHT + msg + Style.NORMAL + Fore.RESET, file=sys.stderr)
