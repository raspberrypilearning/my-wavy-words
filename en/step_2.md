## Make the first line into a list

A list lets your program use one character at a time.

### Create a list

Add this code after the two `import` lines.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 4
---
line1 = list('my wavy words')  # List from a string
--- /code ---

### Write the first item

Change your `write()` code so it writes the first item from the list.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 11
---
goto(-170, 100)
write(line1[0], align='center')
--- /code ---

### Now run your code
Only the first letter, `m`, appears in the turtle window.

<div class="c-project-output">

![Only the first letter m appears in the turtle window](images/step2.png)

</div>

> ### Tip
>
> Lists start counting from `0`, so `line1[0]` is the first item.
{: .c-project-callout .c-project-callout--tip}

> ### Debugging
>
> If you see an error, check that `line1` has the number `1`, not the letter `l`.
{: .c-project-callout .c-project-callout--debug}
