class Solution:
    def maxScore(self, s: str) -> int:
        # Initialize the number of 1's in the whole string
        right_ones = s.count('1')
        
        left_zeros = 0
        max_score = 0
        
        # Traverse the string and calculate the score for each split
        for i in range(len(s) - 1):  # We don't consider the last position for split
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            
            # Calculate score for the current split
            max_score = max(max_score, left_zeros + right_ones)
        
        return max_score
