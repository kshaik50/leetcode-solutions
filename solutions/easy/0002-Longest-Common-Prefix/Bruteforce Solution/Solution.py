from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = ""

        # Take first word as reference
        first = strs[0]

        # Loop through each character index
        for i in range(len(first)):
            char = first[i]

            # Compare with all other words
            for word in strs:
                # Check bounds + mismatch
                if i >= len(word) or word[i] != char:
                    return result

            # If all matched, add to result
            result += char

        return result
