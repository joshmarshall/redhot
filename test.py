from unittest2 import TestCase
import redis

from redhot import redobject, RedBucket
from interfaces import MissingRequiredAttribute

class TestRedObject(TestCase):

    def test_redobject(self):

        with self.assertRaises(MissingRequiredAttribute):
            @redobject
            class Person(object):
                pass

        @redobject
        class Person(object):

            def __init__(self, uid):
                self._uid = uid

            @classmethod
            def from_dict(cls, d):
                return cls(**d)

            def get_dict(self):
                return {
                    "uid": self._uid
                }

            def get_key(self):
                return "person:%s" % self._uid

        person = Person("foobar")
        self.assertEqual("person:foobar", person.get_key())

        person = Person.from_dict({"uid": "foobar"})
        self.assertEqual("person:foobar", person.get_key())


class TestRedBucket(TestCase):

    def setUp(self):
        self._conn = redis.Redis()

    def tearDown(self):
        self._conn.delete("people:foobar")

    def test_red_bucket(self):

        class MockObject(object):

            def get_dict(mock):
                return {"name": "foobar"}

            def get_key(mock):
                return "foobar"

            @classmethod
            def from_dict(cls, d):
                self.assertEqual({"name": "foobar"}, d)
                return "INSTANCE!"

        obj = MockObject()
        bucket = RedBucket("people", self._conn)
        result = bucket.fetch("foobar", MockObject)
        self.assertEqual(result, None)
        bucket.save(obj)
        self.assertEqual(["name"], list(self._conn.hkeys("people:foobar")))
        self.assertEqual("foobar", self._conn.hget("people:foobar", "name"))
        result = bucket.fetch("foobar", MockObject)
        self.assertNotEqual(None, result)
        self.assertEqual("INSTANCE!", result)

        results = list(bucket.fetch_all("foo*", MockObject))
        self.assertEqual(1, len(results))
        self.assertEqual("INSTANCE!", results[0])
