## Draw a line of words

The starting position is in the middle of the output window, so before drawing use `goto()` to move where you want first line of text to appear. 

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 4-7
---
goto(-170, 100)
write('my wavy words', align='center')
--- /code ---

</div>

### Now run your code
The turtle moves to the top left.

<div class="c-project-output">

![The words my wavy words appear near the top left of the turtle window](images/step1.png)

</div>

Tip 
Alight center makes the words apear in a line - try removeing this to see what happens.
