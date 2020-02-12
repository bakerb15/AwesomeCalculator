# Awesome Calculator

This project is a simple calculator created in Python and [PySimpleGUI](https://pysimplegui.readthedocs.io). 
It relies on the python interpreter to parse and evaluate arithmetic expressions. 
The advantage of using the python interpreter is we don't have to write a parser. 
The project makes use of the model-view-controller (MVC) pattern in an attempt to make the calculator extensible.
There is a Visual Studio 2017 solution for this small project, but any IDE or text editor will do.
If you aren't using Visual Studio you may need to add the project's directory to your python path 
for the MVC classes are imported at the top of main.py.

## What are the advantages of using PySimpleGUI?

Cross-platform and quick! PySimpleGUI is great for prototyping.

## Future Work
1. Implement some type of history. A list of past calculations could be displayed to the user. If the user enters a (h1) then the value of (h1) would be plugged into the calculation.
2. Import SymPy and allow user to make use of SymPy's ability to solve equations.
3. Import Matplotlib and combine with Sympy to allow user to generate plots.
4. Allow user to add comments to calculations. Maybe create seperate box text box.
Store comments with calculations in history. Allow the user to save/load history from
previous session.
5. SimpleGui has a bunch of built in themes. Allow the user to select the theme from a dropdown.

