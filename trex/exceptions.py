

class RedisError(Exception):
    pass


class ConnectionError(RedisError):
    pass


class ResponseError(RedisError):
    pass


class ScriptDoesNotExist(ResponseError):
    pass


class NoScriptRunning(ResponseError):
    pass


class InvalidResponse(RedisError):
    pass


class InvalidData(RedisError):
    pass


class WatchError(RedisError):
    pass
