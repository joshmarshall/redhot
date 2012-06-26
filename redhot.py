import interfaces

class RedBucket(object):

    def __init__(self, name, connection):
        self._name = name
        self._connection = connection

    def _get_object_key(self, object_key):
        return "%s:%s" % (self._name, object_key)

    def save(self, obj):
        object_key = self._get_object_key(obj.get_key())
        for key, value in obj.get_dict().iteritems():
            self._connection.hset(object_key, key, value)

    def fetch(self, key, redcls):
        object_key = self._get_object_key(key)
        object_dict = self._connection.hgetall(object_key)
        return redcls.from_dict(object_dict)


@interfaces.define
class _RedObject(object):

    @interfaces.require
    def get_dict(self):
        """All RedObject implementations must implement `get_dict(self)`."""
        pass

    @interfaces.require
    def get_key(self):
        """All RedObject implementations must implement `get_key(self)`."""
        pass

    @interfaces.require
    def from_dict(self, dictionary):
        """All RedObject's must have a @classmethod `from_dict(self, d)`"""


def redobject(cls):
    """Decorator for implementing redhot objects."""
    return interfaces.implement(_RedObject)(cls)
