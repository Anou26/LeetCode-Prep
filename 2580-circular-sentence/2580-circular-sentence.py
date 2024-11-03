class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        if not words:
            return False
        n = len(words)
        for i in range(n):
            current_word = words[i]
            next_word = words[(i + 1) % n]
            if current_word[-1] != next_word[0]:
                return False
        return True

        