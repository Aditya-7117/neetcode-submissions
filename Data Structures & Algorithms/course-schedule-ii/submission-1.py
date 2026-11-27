class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list: course -> its prerequisites
        prereq = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            prereq[course].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            # If a course appears again in the CURRENT DFS path, there's a cycle
            if course in cycle:
                return False

            # Already processed this course and all its prerequisites
            if course in visit:
                return True

            # Mark this course as part of the current DFS path
            cycle.add(course)

            # Complete all prerequisites before adding the current course
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False

            # Finished exploring this course, so remove it from the current path
            cycle.remove(course)

            # Permanently mark as processed to avoid repeated DFS
            visit.add(course)

            # Append AFTER prerequisites to get the correct course order
            output.append(course)
            return True

        # Run DFS for every course, including disconnected ones
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output