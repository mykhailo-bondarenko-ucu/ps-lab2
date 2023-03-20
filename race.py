import argparse
import hazelcast
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("id", type=int)
id = parser.parse_args().id

client = hazelcast.HazelcastClient()
locking_map = client.get_map("race-map")

if locking_map.get(0).result() is None: locking_map.set(0, 0).result()

for _ in range(1000):
    c = locking_map.get(0).result()
    sleep(0.01)
    locking_map.replace_if_same(0, c, c + 1).result()

print("c =", locking_map.get(0).result())

client.shutdown()