# Bytecode Breakdown

Here’s a detailed table that explains each instruction:

| Offset | Bytecode (Int) | Bytecode (Hex) | Opcode Name    | Operand | Description                                                                                 |
| ------ | -------------- | -------------- | -------------- | ------- | ------------------------------------------------------------------------------------------- |
| 0      | 151            | 0x97           | `LOAD_ATTR`    | 0       | Load an attribute from an object (or local variable).                                       |
| 2      | 100            | 0x64           | `LOAD_CONST`   | 1       | Push the constant at index 1 from `co_consts` array onto the stack.                         |
| 4      | 125            | 0x7D           | `STORE_FAST`   | 0       | Pop the value from the stack and store it into the local variable at index 0 (usually `a`). |
| 6      | 100            | 0x64           | `LOAD_CONST`   | 2       | Push the constant at index 2 from `co_consts` array onto the stack.                         |
| 8      | 125            | 0x7D           | `STORE_FAST`   | 1       | Pop the value from the stack and store it into the local variable at index 1 (usually `b`). |
| 10     | 124            | 0x7C           | `LOAD_FAST`    | 0       | Push the local variable value at index 0 (usually `a`) onto the stack.                      |
| 12     | 124            | 0x7C           | `LOAD_FAST`    | 1       | Push the local variable value at index 1 (usually `b`) onto the stack.                      |
| 14     | 122            | 0x7A           | `BINARY_ADD`   | 0       | Pop the top two values from the stack, add them, and push the result back onto the stack.   |
| 16     | 0              | 0x00           | Padding        | 0       | Padding for alignment.                                                                      |
| 17     | 0              | 0x00           | Padding        | 0       | Padding for alignment.                                                                      |
| 18     | 83             | 0x53           | `RETURN_VALUE` | 0       | Return the value from the top of the stack as the result of the function.                   |
| 20     | 0              | 0x00           | Padding        | 0       | Padding for alignment.                                                                      |

### Bytecode Explanation

- **`LOAD_ATTR` (0x97)**: Loads an attribute from an object on the stack.
- **`LOAD_CONST` (0x64)**: Pushes a constant from `co_consts` array onto the stack.
- **`STORE_FAST` (0x7D)**: Pops the top of the stack and stores it into a local variable.
- **`LOAD_FAST` (0x7C)**: Pushes the local variable value onto the stack.
- **`BINARY_ADD` (0x7A)**: Adds the top two values on the stack.
- **`RETURN_VALUE` (0x53)**: Returns the top value from the stack as the function’s result.
- **Padding**: Used for alignment.

Bytecode Breakdown
Bytecode Offset: Position in the bytecode sequence.
Opcode: Numeric representation of the bytecode instruction.
Operand: Extra data associated with the opcode.
Description: A textual description of what the opcode does.
Opcode Name: The name of the bytecode instruction.
Operand Value: The value used in the instruction (if any).
Stack Operation: What happens to the stack during this operation.
Notes: Additional information about the opcode or operation.

An attribute of an object in Python is a characteristic or behavior of that object

Code Object: A data structure that includes the bytecode as well as other metadata about the code.
Bytecode: A sequence of low-level instructions that the Python interpreter executes, contained within the code object.

## Python Source Code Structure

The Python source code repository contains various directories and files, but the core structure can be categorized into several main areas:

- Python Runtime Core: Contains the fundamental parts of the Python interpreter.
- Standard Library: The collection of modules and packages that come with Python.
- Tools and Utilities: Includes scripts and tools for building, testing, and managing Python.

## Important Components of the Python Interpreter

pythonrun.c: Contains the main entry point of the Python interpreter.
ceval.c: Implements the evaluation loop, responsible for executing bytecode.
compile.c: Handles the compilation of Python source code into bytecode.
bltinmodule.c: Contains implementations of built-in functions and objects.
object.c: Defines fundamental Python objects such as integers, floats, and strings.
pyframe.c: Manages the execution frames, which represent the call stack during execution.

https://chatgpt.com/share/b5b98698-8bc9-4b91-b165-bd54c804559b

# Why Stack?

### Advanced Stack Use Cases

- **Undo Mechanisms**:
- **Applications**: Text editors and version control systems use stacks to manage undo operations.
- **Example**: A stack of operations allows the last action to be reversed first.

- **Backtracking Algorithms**:
- **Algorithms**: Depth-first search (DFS), maze solving, and pathfinding algorithms use stacks to explore possibilities and backtrack.
- **Example**: Exploring a maze by pushing possible moves onto a stack and backtracking when hitting a dead end.

| Opcode Name       | Numerical Opcode |
| ----------------- | ---------------- |
| LOAD_CONST        | 100              |
| LOAD_FAST         | 124              |
| STORE_FAST        | 125              |
| LOAD_GLOBAL       | 116              |
| BINARY_ADD        | 23               |
| RETURN_VALUE      | 83               |
| POP_TOP           | 1                |
| JUMP_FORWARD      | 110              |
| POP_JUMP_IF_FALSE | 114              |
| POP_JUMP_IF_TRUE  | 115              |
| LOAD_ATTR         | 106              |
| CALL_FUNCTION     | 131              |

SETUP_FINALLY (151, 0): Sets up a try-finally block. The argument 0 indicates the jump target for the finally block.
LOAD_CONST (100, 1): Loads the constant 1 (which is 4 in the context of the function) onto the stack.
STORE_FAST (125, 0): Stores the top-of-stack value (4) into the local variable at index 0 (a).
LOAD_CONST (100, 2): Loads the constant 2 onto the stack.
STORE_FAST (125, 1): Stores the top-of-stack value (2) into the local variable at index 1 (b).
LOAD_FAST (124, 0): Loads the local variable a onto the stack.
LOAD_FAST (124, 1): Loads the local variable b onto the stack.

dis, a module that lets us see what each byte value corresponds to. first one instruction and the second one is an argument.

### Summary of Stack Usage

| Task                        | Why Stack?                                | Benefits of Stack                               |
| --------------------------- | ----------------------------------------- | ----------------------------------------------- |
| **Function Calls**          | LIFO structure fits the call-return model | Automatically handles nested function calls     |
| **Local Variables**         | Function scope and lifetime management    | Automatic cleanup of variables on function exit |
| **Expression Evaluation**   | Intermediate results and operations       | Efficiently manages temporary values            |
| **Undo Mechanisms**         | LIFO model for reverting actions          | Simple and effective way to manage undo history |
| **Backtracking Algorithms** | Manage exploration paths and state        | Supports exploring and retracting choices       |

Stacks are used because their **LIFO** property aligns perfectly with the needs of managing function calls, local variables, and intermediate results during expression evaluation. They are simple to implement and efficient for these tasks, making them a preferred choice in these scenarios.

### Visual Summary

Here’s a visual summary of how stacks are used for different tasks:

| Use Case                    | Stack Operations                      | Example Representation                                       |
| --------------------------- | ------------------------------------- | ------------------------------------------------------------ |
| **Function Calls**          | Push frame on call, Pop on return     | `push(frameA) -> push(frameB) -> pop(frameB) -> pop(frameA)` |
| **Local Variables**         | Push variables on call, Pop on return | Local variables are managed in function call frames          |
| **Expression Evaluation**   | Push operands, Pop for operations     | `[5]`, `[5, 3]`, `[5, 3, 2]`, `*`, `[5, 6]`, `+`, `[11]`     |
| **Undo Mechanisms**         | Push actions, Pop for undo            | `[Action1, Action2, Action3]`, `undo(Action3)`               |
| **Backtracking Algorithms** | Push states, Pop for backtrack        | `[State1, State2, State3]`, `backtrack(State3)`              |

Stacks are versatile and efficient for managing the dynamic aspects of program execution, making them indispensable in many computing scenarios.

Byte code comes with two unist, first one instruction and second one is argument to that instruction.

- **Execution Process**:

| Instruction       | Stack State | Action                          |
| ----------------- | ----------- | ------------------------------- |
| `LOAD_CONST 1`    | [1]         | Push 1 onto the stack           |
| `LOAD_CONST 2`    | [1, 2]      | Push 2 onto the stack           |
| `LOAD_CONST 3`    | [1, 2, 3]   | Push 3 onto the stack           |
| `BINARY_MULTIPLY` | [1, 6]      | Multiply 2 and 3, push result 6 |
| `BINARY_ADD`      | [7]         | Add 1 and 6, push result 7      |
| `STORE_FAST 0`    | []          | Store 7 in variable `a`         |
| `RETURN_VALUE`    | []          | Return the value of `a`         |

```text
     [Module]
        |
     [FunctionDef]
        |
    +---+---+
    |       |
  [args]  [body]
           |
    +---+---+---+
    |   |   |   |
 [Assign] [Assign] [Return]
   |       |        |
  [Name]   [Name]  [BinOp]
   |       |      /   |   \
 [a]     [b]    [a]  [+ ]  [b]
                [Load]    [Load]

```

Source Code --> Compilation --> Bytecode --> Load Bytecode into RAM --> PVM Fetches Bytecode from RAM --> PVM Decodes Bytecode into Machine Code --> CPU Executes Machine Code

```
+----------------+       +-----------------------+        +--------------------------+
| Bytecode       |       | Opcode (0x00, 0x01)   |        | Opcode Table            |
| Instructions   | ----> | ...                   | -----> | Opcode -> Handler       |
+----------------+       +-----------------------+        +--------------------------+
                               |  Fetch Opcode               |
                               v  Get Opcode                   |
                        +----------------+                    |
                        | Opcode (0x00)   |                    |
                        | Handler:        |                    |
                        | handle_LOAD_FAST|                    |
                        +----------------+                    |
                               |                               |
                               v                               v
                     +------------------+            +--------------------+
                     | Handler Function |            | Function Call      |
                     | handle_LOAD_FAST |            | handle_LOAD_FAST() |
                     +------------------+            +--------------------+


```

```

+-------------------+    +--------------------+    +-------------------+
| Bytecode Stream   | -> | Fetch Opcode       | -> | Opcode (0x01)     |
| (e.g., [0x01, ...])|    | (Read Bytecode)    |    | (LOAD_FAST)       |
+-------------------+    +--------------------+    +-------------------+
                                   |                       |
                                   v                       v
                      +---------------------+      +---------------------+
                      | Opcode Table        |      | Lookup Opcode       |
                      | (Opcode -> Handler) |      | handler = opcode_table[opcode].handler |
                      +---------------------+      +---------------------+
                                   |                       |
                                   v                       v
                      +---------------------+      +---------------------+
                      | Handler Function    |      | Call Handler        |
                      | (e.g., handle_LOAD_FAST) |  | handler()           |
                      +---------------------+      +---------------------+
                                   |                       |
                                   v                       v
                      +---------------------+      +---------------------+
                      | Execute Bytecode    |      | Perform Operation   |
                      | (Perform Action)    |      | (Push to Stack, etc.)|
                      +---------------------+      +---------------------+


```
