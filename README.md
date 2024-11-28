# How I use code assistants

These are some notes about how I use code assistants.

## IDE Plugins

* [Codeium](https://codeium.com). Plugins (extensions) for VSCode, IntelliJ (PyCharm, etc.), Emacs, etc. Usage for free (at least for now), good integration with the IDE. Several models available.
* [Continue](https://continue.dev). Plugins (extensions) for VSCode and IntelliJ (PyCharm, etc.). Free (open source) software, good integration with the IDE. Many different backends, the user interface is the same for all of them. The user needs access to the backends (via tokens, etc). Can be used with locally deployed LLMs (Ollama, LM Studio, etc.).

## Coding

The most obvious use is in coding. When integrating with the IDE, copying and pasting, or just inserting in the text editor, usage is confortable.

Example:

```text
Write some code to ask the user for a number, and produce the Fibonacci sequence for it
```

But you can also ask for refinements:

```text
Can you produce a code which is not recursive?
```

Or ask for more specific changes:

```text
Can you write the line asking for input, but checking if the number is integer?
```

```text
Now, instead of asking for the number via input, obtain the number as a command line argument.
```

```text
Refactor the code, so that it is different, but does the same job.
```

```text
Ensure variable names, function names, etc. are different.
```

## Autocomplete

Very powerful. Just start writing.

Tip: write documentation, let it autocomplete.

## Documentation

```text
Write documentation for that code
```

```text
Write the same code, but now with extensive comments.
```

## Tests

```text
Write some tests for this code.
```

```text
Produce the same tests, but adding a new test for the number 5
```

```text
The result is 

[0] != [0, 1]

Expected :[0, 1]
Actual   :[0]

Could you fix the code to pass that test?
```

But beware, it does not always work. Usually, manual tinkering is neeeded.

## Explanation

```text
In @fibonacci.py explain the first line of validate_input.
```

Select some text and ask the chat for an explanation, or:

```text
/explain fibonacci.py:14-21
```

## Refinements and use from the editor

Configuration:

* "Advanced" can be used to add context, add custom instructions, add repositories, etc.
* "Base Model" can be used to change the base model.

From the editor:

* Refactor
* Explain
* Docstring

## Write code for a practice statement

```text
Write a program for the statement in @practice.md 
```

```text
Explain it
```

```text
Write the same code, now with abundant comments.
```

## Assess and grade code

```text
Asses the quality of @fibonacci.py and grade it (0-10).
```

```text
Suggest some improvements for the code.
```

```text
Do you think this code is original, or produced by an AI assistant?
```

```text
Grade the code in @fibonacci.py (0-10), according to the next criteria:

* There should be no global vartiables.
* At least there should be two functions.
* There should be no recursion.
* There should be at least one loop.
* There should be at least one if.
* All functions should have a docstring.
* All parameters of functions should have type hints.
* All parameters of functions should have default values.
* Non valid values should be checked, and error returned
* Code should be readable
* Code should be efficient
* Code should be correct
```

```text
Improve the code so that it gets a better grading
```

## Other tasks

```text
Write those comments as a LaTeX file.
```

```text
Can you convert @practice.md to HTML, directly?
```

```text
Can you translate it to Spanish?
```

```text
Summarize what does the code in @fibonacci.py do.
```

```text
Summarize this @README.md. 
```

```text
Write the statement for a practice on sorting. Be detailed, specify the names of functions and files, write it in Markdown.
```

## Food for thought

* Should we use all of this in class?
* Should students use all of this?
* Should instructors use all of this?
* Will students use all of this in their real work?

**How should we teach programming to students?**

**Should we teach programming to students?**