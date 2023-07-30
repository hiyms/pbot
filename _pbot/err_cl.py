"""
用来定义pbot有关异常
"""
from . import plog


class QbotException(Exception):
    def __init__(self, errorinfo):
        super().__init__(self)
        self.ERRORINFO = errorinfo
        plog.DEFAULT_LOG.error(f"{type(self).__name__} 内容：{self.ERRORINFO}")

    def __str__(self):
        return str(self.ERRORINFO)


class QbotPermissionError(QbotException):
    ...
