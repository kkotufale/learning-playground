# Learning Playground

My collection of introductory Python practice exercises. Each script explores a small problem using console input, arithmetic, or conditional logic.

## Exercises

| Exercise | What it does | Concepts |
| --- | --- | --- |
| [Even or odd](evenoddPrac.py) | Identifies whether an integer is even or odd | Modulo and conditionals |
| [Number comparison](NumbercomparisonPrac.py) | Prints the larger of two integers, or an equality message | Comparisons and branching |
| [Test score](TestscorePrac.py) | Converts an integer score to a letter grade and rejects scores outside 0–100 | Ordered conditions and range checks |
| [Area and perimeter](areaperimeterPrac.py) | Calculates a rectangle's area and perimeter | Console input and arithmetic |
| [Monthly payment](MonthlypaymentPrac.py) | Calculates a fixed-payment loan's monthly payment | Rate conversion and exponentiation |

## Run an exercise

These scripts use Python 3 and require no third-party packages.

Clone the repository, enter its directory, and run a script:

```bash
git clone https://github.com/kkotufale/learning-playground.git
cd learning-playground
python3 evenoddPrac.py
```

Enter a number when prompted. For example, entering `8` prints `Even`.

To run another exercise, replace the filename:

```bash
python3 TestscorePrac.py
```

Entering `85` prints `B`.

On systems where Python 3 is available as `python` rather than `python3`, use `python` in these commands.

## Current scope

These are learning exercises with integer input. Non-numeric input is not handled. The loan calculator expects a positive loan amount, interest rate, and number of years; a zero interest rate or zero-year term causes division by zero. The rectangle exercise does not reject zero or negative dimensions.

## Next learning goals

- Improve input validation and error messages.
- Support decimal input where appropriate.
- Handle zero-interest loans.
- Practice reusable functions and automated tests.

These are planned improvements, rather than features already implemented.

## Related work

My Excel, Python, SQL, and Tableau coursework is collected in [Projects](https://github.com/kkotufale/Projects).
