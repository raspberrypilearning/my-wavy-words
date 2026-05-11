## Make words go around a circle

Use another loop and a turn angle to place words around a circle.

### Add more words

Add two more lists after `line2`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 6-7
---
line1 = list('my wavy words')  # List from a string
line2 = list('growing up')
line3 = list('falling down')
line4 = list('moving round and ')

penup()
hideturtle()
--- /code ---

### Add falling and round words

Add this code after your second `for` loop.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 31
line_highlights: 31-46
---
right(120)
forward(30)
for i in range(len(line3)):
    write(line3[i], align='center')
    forward(randint(15, 20))
    right(randint(2, 3))

goto(80, 100)
for i in range(len(line4)):
    write(line4[i], align='center')
    forward(20)
    right(360 / len(line4))  # turn fraction of a circle
--- /code ---

### Now run your code

The words `moving round and` appear in a circle on the right of the turtle window.

<div class="c-project-output">

![The words moving round and appear in a circle on the right of the turtle window](images/step5.png)

</div>

> ### Tip
>
> `360 / len(line4)` splits a full turn into equal parts.
{: .c-project-callout .c-project-callout--tip}

> ### Debugging
>
> If the circle is too wide or too small, change the number in `forward(20)`.
{: .c-project-callout .c-project-callout--debug}
