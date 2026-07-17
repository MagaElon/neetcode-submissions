class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # 1. Initialize the counts for the first window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            
        # 2. Count how many character frequencies match initially
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
                
        # 3. Slide the window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            # Add the right character entering the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
                
            # Remove the left character leaving the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
            
        return matches == 26