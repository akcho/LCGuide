# time: O(n)
# space: O(1) -> 26, going through each char

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Max_length is the longest overall subsequence (final answer)
        # Max_count is just the highest count of chars within the curr subsequence
        max_length = max_count = 0
        # count keeps track of all of the chars that we are looking at in the subsequence
        count = defaultdict(int)
        for i in range(len(s)):
            c = s[i]
            # Add char to the count dict
            count[c] += 1

            # Find the new max_count. This is much like Kadane's,
            # where we only consider if the new length exceeds the max_length.
            max_count = max(max_count, count[c])

            # The answer must always be max_count + k.
            if max_length < k + max_count:
                max_length += 1
            else:
                # s[i-max_length] removes the char at the start of a following subsequence:
                # This serves as the "correction" for a subsequence problem
                count[s[i-max_length]] -= 1
        return max_length