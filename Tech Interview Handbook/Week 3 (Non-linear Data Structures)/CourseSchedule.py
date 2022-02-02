# Recursive DFS
# time: O(num_prereqs + num_courses) == O(edges + visited) == O(|E| + |V|)
# space: O(num_prereqs + num_courses) == O(edges + visited) == O(|E| + |V|)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {course: [] for course in range(numCourses)}

        # assign key-value pairs in our prereq_map
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # visit_set = all courses along the curr DFS path
        visit_set = set()

        def dfs(course):
            # if we already visited this course, then we hit a loop
            if course in visit_set: return False
            # if we didn't populate prereqs in our key-value pair assignment, we're good to go
            if prereq_map[course] == []: return True

            visit_set.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq): return False

            # This particular course has been vetted at this point. We can remove it from our to-watch list.
            visit_set.remove(course)
            prereq_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True
