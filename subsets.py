def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        subsets = []
        for msk in range(2**n):
            s = []
            for p in range(n):
                if (msk >> p) & 1:
                    s.append(nums[p])
            subsets.append(s)
        return subsets