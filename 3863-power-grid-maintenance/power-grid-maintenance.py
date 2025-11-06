
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                if pa < pb: parent[pb] = pa
                else: parent[pa] = pb

        for u, v in connections:
            union(u, v)

        comps = defaultdict(list)
        for i in range(1, c + 1):
            heapq.heappush(comps[find(i)], i)

        online = [True] * (c + 1)
        res = []

        for t, x in queries:
            if t == 2:
                online[x] = False
            else:
                if online[x]:
                    res.append(x)
                else:
                    h = comps[find(x)]
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    res.append(h[0] if h else -1)
        return res
