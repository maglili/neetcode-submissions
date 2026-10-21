class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adj list
        adj = {c: set() for w in words for c in w}
        in_deg = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))

            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_deg[w2[j]] += 1
                    break

        # bfs
        res = []
        q = deque([c for c in in_deg if in_deg[c] == 0])
        while q:
            char = q.popleft()
            res.append(char)
            for nei in adj[char]:
                in_deg[nei] -= 1

                if in_deg[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(adj) else ""
