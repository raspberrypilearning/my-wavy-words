## Make some text appear

Use `turtle` to write your first words on the screen.

### Write your words

Move the turtle to the start position, then write your first line of text.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 4-7
---
penup()
hideturtle()
goto(-170, 100)
write('my wavy words', align='center')
--- /code ---

### Now run your code
The words `my wavy words` appear near the top left of the turtle window.

<div class="c-project-output">

![The words my wavy words appear near the top left of the turtle window](images/step1.png)

</div>

> ### Tip
>
> `penup()` stops the turtle drawing lines when it moves.
{: .c-project-callout .c-project-callout--tip}
