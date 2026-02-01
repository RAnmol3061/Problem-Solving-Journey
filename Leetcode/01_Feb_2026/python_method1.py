class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_ascii = ord(target)
        letters_ascii = []

        for i in letters:
            letters_ascii.append(ord(i))

        
        for i in letters_ascii:
            if target_ascii < i:
                return chr(i)
            elif target_ascii == i:
                pass
            
        return chr(letters_ascii[0])
        