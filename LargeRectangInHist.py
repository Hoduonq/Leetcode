def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        barStack = []

        largest = 0

        for i, h in enumerate(heights):
            if barStack and barStack[-1][1] == h:
                continue
            start_i = i
            while barStack and barStack[-1][1] > h:
                last_i, last_h = barStack.pop()
                area = last_h * (i - last_i)
                largest = max(largest, area)
                start_i = last_i
            
            barStack.append((start_i, h))
        
        while len(barStack) > 0:
            last_i, last_h = barStack.pop()
            area = last_h * (len(heights)- last_i)
            largest = max(largest, area)
        
        return largest