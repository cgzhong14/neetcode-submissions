class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        #start by assuming the entire first string is the common prefix
        #bat
        prefix = strs[0]

        #compare this prefix with every other prefix
        for s in strs[1:]:
            # reduce the prefix untiil it matches with the start of the string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# "dag".startswith("dance") → ❌
# "dag".startswith("danc") → ❌
# "dag".startswith("dan")  → ❌
# "dag".startswith("da")   → ✅

# "feet".startswith("neet") → ❌
# "feet".startswith("nee")  → ❌
# "feet".startswith("ne")   → ❌
# "feet".startswith("n")    → ❌
# "feet".startswith("")     → ✅
