if __name__ == "__main__":
    import tkinter as tk
    import logging as logg
    from tkinter import *
    from tkinter import filedialog as fd
    from tkinter import messagebox as mb
    import sys

class askLogPath:
    """A class representing the logs"""
    # def __init__(self,):
    def LogDirPath(logPath):
        # self.logPath = logPath
        if len(logPath) > 4:
            return True
        elif len(logPath) <= 4:
            return False
            _separator = "/"
            _log_Path = fd.askdirectory()
            _logPath = (_log_Path + _separator)
            print(_log_Path)
        return logPath
    def MainLogPath(self, logPath):
        _theLogPath = logPath
        mainLog_path = (_theLogPath + "mainLog.log")
        return mainLog_path
    def StdOutPath(self, logPath):
        _theLogPath = logPath
        stdout_path = (_theLogPath + "output.log")
        print(stdout_path)
        return stdout_path
    if:
        separator = "/"
        logPath = []
