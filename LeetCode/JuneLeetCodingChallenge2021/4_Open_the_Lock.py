class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        nums = []
        deadends = set(deadends)
        if "0000" in deadends: return -1
        
        for i in range(10000):
            tmp = "0000"+str(i)
            nums.append(tmp[-4:])
        adjList = defaultdict(list)
        for n in nums:
            for i in range(4):
                for digit in [((int(n[i])+1)%10),((int(n[i])-1)%10)]:
                    nx = n[:i]+str(digit)+n[i+1:]
                    if nx not in deadends:
                        adjList[n].append(nx)
        #bfs
        q = deque([("0000",0)])
        visited = set()
        while q:
            val, stp = q.popleft()
            if val == target: return stp
            for nx in adjList[val]:
                if nx not in visited:
                    visited.add(nx)
                    q.append((nx,stp+1))
        return -1
