class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the sentence into words
        if len(pattern) != len(words):
            return False  # If lengths differ, they can't have a 1-to-1 mapping
        
        # Create two dictionaries for forward and reverse mappings
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            # Check if the current pattern character maps to the current word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # Check if the current word maps back to the same pattern character
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True  # If we reach here, the pattern is matched



        