class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]] # First interval of the sorted interval list inserted for Edge case handling 

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] #-1 represents the last item in the output, and 1 represents the element at index 1 in the list. 

            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd) #Merge of intervals 
            else:
                output.append([start, end])
        return output

