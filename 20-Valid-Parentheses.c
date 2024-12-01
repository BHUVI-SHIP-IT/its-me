

bool isValid(char* s) {
    int n = strlen(s);  // Get the length of the string
    
    // Stack to hold opening brackets
    char* stack = (char*)malloc(n * sizeof(char));
    int top = -1;  // Stack pointer
    
    // Traverse the string
    for (int i = 0; i < n; i++) {
        char current = s[i];
        
        // If it's an opening bracket, push it onto the stack
        if (current == '(' || current == '[' || current == '{') {
            stack[++top] = current;
        } 
        // If it's a closing bracket, check if it matches the top of the stack
        else {
            if (top == -1) {  // Stack is empty, unmatched closing bracket
                free(stack);
                return false;
            }
            char topChar = stack[top];
            if ((current == ')' && topChar == '(') ||
                (current == ']' && topChar == '[') ||
                (current == '}' && topChar == '{')) {
                top--;  // Pop the stack if it matches
            } else {
                free(stack);  // Unmatched closing bracket
                return false;
            }
        }
    }
    
    // After traversing, if the stack is empty, all brackets matched correctly
    bool result = (top == -1);
    free(stack);  // Free the allocated stack memory
    return result;
}
