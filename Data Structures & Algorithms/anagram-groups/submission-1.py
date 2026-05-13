class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        # Process each string once
        for s in strs:
            # Count frequencies for 'a' to 'z'
            count = [0] * 26
            # Build the frequency array for the current string
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Convert list to tuple so it can be used as a hash key
            key = tuple(count)
            # Group strings with the same frequency signature
            groups[key].append(s)
        # Return all grouped anagrams
        return list(groups.values())