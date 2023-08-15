import logging

from assetsapi.kbeapi.baseapp import KBEngine

logger = logging.getLogger()


def countPlayers():
    """
    KBEngine.addWatcher("players", "UINT32", countPlayers)
    The above code adds this function to the monitor, and the return value
    of the function can be monitored in real time from tools such as GUIConsole
    """
    i = 0
    for e in KBEngine.entities.values():
        if e.__class__.__name__ == "Avatar":
            i += 1

    return i


def setup():
    KBEngine.addWatcher("players", "UINT32", countPlayers)
