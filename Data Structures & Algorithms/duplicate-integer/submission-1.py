class Solution: 
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for ijk in nums:
            if ijk in seen:
                return True
            seen.add(ijk)
        return False        