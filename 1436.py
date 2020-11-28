class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pathSet = set(())
        for path in paths:
            if path[0] not in pathSet:
                pathSet.add(path[0])
        for path in paths:
            if path[1] not in pathSet:
                return path[1]
        return 0
