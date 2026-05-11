## Move the words into a list

### Step 1
Write your first line of text into a list. Replace `my wavy words` with your own writing.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 4
---
line1 = list('my wavy words')  # Make a list from your text
--- /code ---

</div>

> ### Tip
>
> A list XXX add what list is. 
> then write here that you can call the list 
{: .c-project-callout .c-project-callout--tip}


### Step 2
Add `write()` to draw the first item in the list - `line1[0]`.

<div class="c-project-code">

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

</div>

### Now run your code
The first letter, `m`, appears in the turtle window.

<div class="c-project-output">

![Only the first letter m appears in the turtle window](images/step2.png)

</div>

