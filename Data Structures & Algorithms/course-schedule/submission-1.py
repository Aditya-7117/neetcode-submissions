class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []: # Base case 
                return True

            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre): # Causing recursion 
                    return False
            visit.remove(course) 
            preMap[course] = [] # Clearing out the Hashmap values 
            return True 
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True