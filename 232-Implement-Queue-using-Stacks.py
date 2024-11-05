class MyQueue:

    def __init__(self):
        self.input_stack = []  # Stack to hold incoming elements
        self.output_stack = []  # Stack to hold outgoing elements

    def push(self, x: int) -> None:
        # Push element onto the input stack
        self.input_stack.append(x)

    def pop(self) -> int:
        # Ensure output stack has the oldest elements
        self.peek()  # This will fill the output stack if it's empty
        return self.output_stack.pop()

    def peek(self) -> int:
        # Ensure output stack has the oldest elements
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]  # Return the top element of output stack

    def empty(self) -> bool:
        # The queue is empty if both stacks are empty
        return not self.input_stack and not self.output_stack

        


