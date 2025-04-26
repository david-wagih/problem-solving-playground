from typing import List

# this problem is solved using greedy algorithm
# we keep track of the farthest position we can reach with current jumps
# and the farthest position we can reach with one more jump
# we increment the number of jumps when we need to make a jump
# we update the current reach to the next reach when we can reach the end with current jumps

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        current_reach = 0  # The farthest position we can reach with current jumps
        next_reach = 0     # The farthest position we can reach with one more jump
        jumps = 0          # Number of jumps made
        
        for i in range(n):
            if i > current_reach:
                # We need to make a jump
                jumps += 1
                current_reach = next_reach
                
            next_reach = max(next_reach, i + nums[i])
            
            # If we can reach the end with current jumps
            if current_reach >= n - 1:
                return jumps
                
        return jumps
            

            