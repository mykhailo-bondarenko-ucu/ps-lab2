import hazelcast

client = hazelcast.HazelcastClient()
distributed_map = client.get_map("distributed-map")
for i in range(1000):
    distributed_map.set(i, f"value{i}").result()

print("Map size:", distributed_map.size().result())

client.shutdown()