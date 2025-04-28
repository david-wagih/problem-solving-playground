from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort citations in descending order
        citations.sort(reverse=True)
        
        # Iterate through the sorted citations
        for i, citation in enumerate(citations):
            # If the current citation is less than i+1,
            # the previous i is our h-index
            if citation < i + 1:
                return i
                
        # If we haven't returned yet, the h-index is the length of the array
        return len(citations) 