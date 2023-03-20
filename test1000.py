import hazelcast

client = hazelcast.HazelcastClient()
distributed_map = client.get_map("distributed-map")
for i in range(1000):
    assert distributed_map.get(i).result() == f"value{i}"

print("All correct! Map size:", distributed_map.size().result())

client.shutdown()