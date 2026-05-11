## Challenge

Style and colour your wavy words.

### Step 1
Change the colours and fonts

Add two font styles after `hideturtle()`.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 11-12
---
style1 = ('Courier', 16)
style2 = ('Times New Roman', 14)
--- /code ---

</div>

### Step 2
Use `font=style1` in the first three loops.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 18
---
write(line1[i], font=style1, align='center')
--- /code ---

</div>

### Step 3
Add colours and use `style2` for the circle.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 34
line_highlights: 34, 36, 41, 43
---
color('green')
for i in range(len(line3)):
    write(line3[i], font=style1, align='center')
    forward(randint(15, 20))
    right(randint(2, 3))

goto(80, 100)
color('orange')
for i in range(len(line4)):
    write(line4[i], font=style2, align='center')
    forward(20)
    right(360 / len(line4))  # turn fraction of a circle
--- /code ---

</div>

### Now run your code

Your turtle window shows your own styled and coloured wavy words.

<div class="c-project-output">

![Styled and coloured wavy words in the turtle window](images/step6.png)

</div>

> ### Tip
>
> Try colours such as `blue`, `purple`, `red`, `green`, `orange`, or `black`.
{: .c-project-callout .c-project-callout--tip}

> ### Debugging
>
> Colour and font names must be inside quote marks, like `color('blue')`.
{: .c-project-callout .c-project-callout--debug}
