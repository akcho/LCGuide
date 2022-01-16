# time: O(n)
# space: O(1) -> 26, going through each char

def characterReplacement(self, s: str, k: int) -> int:
    max_len = 0

    for letter in ascii_uppercase:
        letter_counts, start = 0, 0
        for i in range(len(s)):
            if s[i] == letter:
                letter_counts += 1
            while i - start + 1 - letter_counts > k:
                letter_counts -= (letter == s[start])
                start += 1
            max_len = max(max_len, i - start + 1)
    return max_len