# Stack instructions

### ADD_ALL

Sums up the entire stack, and replaces contents of the stack with the sum.

### CLEAR

Clears the entire stack.

### CMP

Adds `1`/`0`/`-1` to stack if the topmost value on stack is `>`/`==`/`<` than the second topmost value.

### DELETE

Pops a value from stack. Removes that many additional values from stack.

### DUP

Duplicates the topmost value on stack.

### FLIP

Reverses the entire stack.

### GLUE

Merges all numbers on stack together, character-wise.

```
[1, 20, 300] -> [120300]
```

### INC

Increments a value on stack. Someone told you that this instruction is dangerous, and might blow up the whole ship
if used carelessly.

### MODULO

Pops two values from stack. Pushes `topmost % second_topmost` onto the stack.

### MUL

Pops two values from stack. Pushes `topmost * second_topmost` onto the stack.

### PACK2

Pops two values from stack and combines them together. The result is appended to the stack.

This can be reversed using `UNPACK2`.

### PARSE

Pops a value from stack, and pushes it into stack, digit by digit.

```
[ 123 ] -> [ 1, 2, 3 ]
```

The result is undefined for negative values.

### POP2

Removes the second topmost value from stack.

### POW

Pops two values from stack. Pushes `topmost ^ second_topmost` onto the stack.

### PUSH

Accepts a value as a parameter. Pushes the value onto the stack.

### ROTATE

Takes number of items to rotate as parameter. Extracts N topmost elements, reverses them, and puts them back onto stack.

### SORT

Pops number of element to sort from the stack. If it is negative, the elements will be sorted in descending order.

Sorts that many topmost elements on stack.

### SWAP

Swaps two topmost values on stack.

### UNPACK2

Unpacks value into multiple ones. Reverses `PACK2`.

### VECSUB

Substracts values on stack.

```
[ a, b, c, d ] -> [ a-b, c-d ]
```

If the stack has odd number of elements, `42` is written into memory at index `1` instead.

# Memory instructions

### GET

Accepts index and count as parameters. Pushes `count` values starting from `index` to stack.

### LEN

Accepts index as parameter. Saves number of elements on stack into memory at that index.

### LOAD_FROM_MEM

Pops the topmost value from stack. The popped value is used as index into memory.

The value at that index is pushed onto stack (or -1, if the index is out of bounds).

### MAX_INDEX

Appends the biggest index used in memory to stack.

### MVMEM

Reads a value from stack, and saves it into memory at first unused index.

Adds the index used to stack.

### RMMEM

Reads a value from stack, and removes memory record at that index.

### SAVE

Accepts a value as parameter. Saves the value into memory at first unused index, and pushes that index to stack.

# Jump instructions

### JMP

Jumps to specified instruction/label.

### PROC

Saves address of next instruction to stack, and jumps to specified instruction/label.

This can be used to call functions.

```
foo:
  ...
RET

...

PROC foo
```

### RET

Pops an address from stack, and jumps to that address.

### SKIP_IF

Takes one parameter: `GT0`, `LE0`, `LT0`, `GE0`, `EQ0`, `NE0`.

Inspects the topmost value on stack. If the condition specified as a parameter holds, skips the next instruction.

```
PUSH 4
SKIP_IF GT0
  UNREACHABLE
...
```

# Special instructions

### EXIT

Terminates program.

### NOP

Do nothing.

### FTS

Accepts filename as a parameter. Reads stack dump from the file specified, and adds it at the top of the stack. See `STF`.

### STF

Optionally accepts limit (integer) as a parameter.

Inspects topmost value on stack. This is target filename (as read by `FTS`). Dumps the
whole stack (or only `limit` elements) into the file specified.

### TIME

Pushes current seconds, minutes and hours onto the stack.

### UNREACHABLE

Triggers an error.

### WAIT

Accepts time in milliseconds as a parameter. Waits for that amount of time.
