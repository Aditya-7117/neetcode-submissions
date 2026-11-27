class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        cycle, visit = set(), set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visit:
                return True
            
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            res.append(course)
            cycle.remove(course)
            visit.add(course)
            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res
                
            
            
            
         