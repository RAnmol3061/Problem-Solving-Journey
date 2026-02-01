class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        for i in letters:
            if target < i:
                return i
            elif target == i:
                pass
            
        return letters[0]
        