## Add a second loop

Make a second line of words grow upwards from your first line.

### Create another list

Add a second list after `line1`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 5
---
line1 = list('my wavy words')  # List from a string
line2 = list('growing up')
--- /code ---

### Write the second line

Add this code after your first `for` loop.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 18-25
---
forward(30)
left(90)
forward(30)
left(90)
for i in range(len(line2)):
    write(line2[i], align='center')
    right(randint(-5, 5))
    forward(15)
--- /code ---

### Now run your code

A second line of letters grows upwards from the first line.

<div class="c-project-output">

![A second line of letters grows upwards from the first line](images/step4.png)

</div>

> ### Tip
>
> `randint(-5, 5)` chooses a random number from `-5` to `5`.
{: .c-project-callout .c-project-callout--tip}

> ### Debugging
>
> If the second line does not wiggle, check that you imported `randint` at the top of your program.
{: .c-project-callout .c-project-callout--debug}
