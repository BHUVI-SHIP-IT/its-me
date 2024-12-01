

// Helper function for backtracking
void backtrack(char** result, int* returnSize, char* currentCombination, char* digits, int index, char** digitToLetters) {
    // If we have processed all the digits, add the combination to the result
    if (digits[index] == '\\0') {
        result[*returnSize] = strdup(currentCombination);  // Copy the current combination to result
        (*returnSize)++;
        return;
    }
    
    // Get the digit and its corresponding letters
    int digit = digits[index] - '0';  // Convert char to corresponding int (e.g., '2' to 2)
    char* letters = digitToLetters[digit];
    
    // Loop through the letters corresponding to the current digit
    for (int i = 0; letters[i] != '\\0'; i++) {
        currentCombination[index] = letters[i];  // Add the current letter to the combination
        backtrack(result, returnSize, currentCombination, digits, index + 1, digitToLetters);  // Move to the next digit
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** letterCombinations(char* digits, int* returnSize) {
    // Initialize the result and returnSize
    *returnSize = 0;
    
    // Base case: if digits are empty, return an empty list
    if (digits[0] == '\\0') {
        return NULL;
    }

    // Mapping of digits to their corresponding letters
    char* digitToLetters[10] = {
        \\,     // 0
        \\,     // 1
        \abc\,  // 2
        \def\,  // 3
        \ghi\,  // 4
        \jkl\,  // 5
        \mno\,  // 6
        \pqrs\, // 7
        \tuv\,  // 8
        \wxyz\  // 9
    };
    
    // Calculate the maximum number of combinations (4^digits length is the max size)
    int maxSize = 1;
    int len = strlen(digits);
    for (int i = 0; i < len; i++) {
        maxSize *= 4;  // At most, each digit can map to 4 letters (e.g., '7' -> 'pqrs')
    }

    // Allocate memory for the result
    char** result = (char**)malloc(maxSize * sizeof(char*));
    char* currentCombination = (char*)malloc((len + 1) * sizeof(char));  // Current combination string
    currentCombination[len] = '\\0';  // Null-terminate the string

    // Call the backtracking function
    backtrack(result, returnSize, currentCombination, digits, 0, digitToLetters);

    // Free the temporary combination buffer
    free(currentCombination);
    
    return result;
}
