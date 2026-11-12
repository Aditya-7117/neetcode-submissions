class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Use a hash map for prerequisites. 
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # visitSet = all courses along current DFS path 
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        #This is specifically done for Edge case if there are two different graphs given straight away. 
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True 