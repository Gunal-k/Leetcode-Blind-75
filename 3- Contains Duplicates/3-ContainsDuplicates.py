class solution:
    def containsDuplicate(self,nums:list[int])->bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            hashmap[i] = i
        return False
        # return len(set(nums)) < len(nums)

# Create an instance of the Solution class
sol = solution()
print(sol.containsDuplicate([1,2,3,1]))