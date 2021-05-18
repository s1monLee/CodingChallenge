class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for path in paths:
            t = path.split()
            for i in t:
                key = re.findall(r"\(\w+\)", i)
                if len(key) > 0:
                    mem[key[0]].append(t[0] + "/" + i[:-len(key[0])])
        ans = []
        for key in mem:
            if len(mem[key]) > 1:
                ans.append(mem[key])
        return ans
