## Make a loop for the first line

Use a `for` loop to write every character in your list.

### Step 1
Write each character

Replace the code that writes `line1[0]` with this loop.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 11-14
---
goto(-170, 100)
right(90)
for i in range(len(line1)):  # Gets length of a list
    write(line1[i], align='center')
    forward(15)
--- /code ---

</div>

### Now run your code
The letters in `my wavy words` appear one under another.

<div class="c-project-output">

![The letters in my wavy words appear one under another](images/step3.png)

</div>

> ### Tip
>
> `len(line1)` counts how many items are in the list.
{: .c-project-callout .c-project-callout--tip}

> ### Debugging
>
> The two lines inside the loop must be indented.
{: .c-project-callout .c-project-callout--debug}
