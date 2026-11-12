class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1] #Track the first end. 
        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end #Update the end if no overlap is observed. 
            else:
                res += 1
                prevEnd = min(prevEnd, end) #We are doing this specifically to handle and decide upon, potentially, which interval has to get removed. This new prevEnd value will help to deal with future intervals. 
        return res

