"""Simple script to test connection to Redis and print an existing key."""
from redis import StrictRedis
import os

redis = StrictRedis(host=os.environ.get("REDIS_HOST", "localhost"),
                    port=os.environ.get("REDIS_PORT", 6379),
                    db=0)

print redis.get("hello")


"""
For documentation tips: please use the following link:
https://redis.io/commands

This is just a basic example if you want to run python scripts against a redis database.
Side note: Redis most commonly starts from db 0 unless otherwise specified.
It is can be faster in terms of storing and retrieving values for a single session
since everything is stored in memory and within the same space. This rule however is not relational
law. While Redis is a powerful db tool, it is not the only tool, please bear that in mind.

Will update with extra notes if necessary. But for now, the course RU101 course is fine.

Some common commands used include

set customer:1000 fred
# this sets a customer with the key 1000 as fred

get customer:1000
# should return:
# "fred"

del customer:1000
# removes key from memory

hset myhash field1 "hello"
hget myhash field1

# returns:
# "hello"

dbsize

#returns the size of the database you're using


"""