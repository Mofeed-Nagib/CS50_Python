# Seasons of Love

<blockquote>
   <p>Five hundred twenty-five thousand, six hundred minutes<br>
      Five hundred twenty-five thousand moments so dear<br>
      Five hundred twenty-five thousand, six hundred minutes<br>
      How do you measure, measure a year?
   </p>
   <p>— “<a href="https://en.wikipedia.org/wiki/Seasons_of_Love">Seasons of Love</a>,” <a href="https://en.wikipedia.org/wiki/Rent_(musical)"><em>Rent</em></a></p>
</blockquote>

Assuming there are 365 days in a year, there are `365 x 24 x 60 = 525,600` minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour). But how many minutes are there in two or more years? Well, it depends on how many of those are [leap years](https://en.wikipedia.org/wiki/Leap_year) with 366 days, per the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar), as some of them could have `1 x 24 x 60 = 1,440` additional minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since! There is an [algorithm](https://en.wikipedia.org/wiki/Leap_year#Algorithm) for such, but let’s not reinvent that wheel. Let’s use a library instead. Fortunately, Python comes with a `datetime` module that has a class called `date` that can help, per [docs.python.org/3/library/datetime.html#date-objects](https://docs.python.org/3/library/datetime.html#date-objects).

In a file called `seasons.py`, implement a program that prompts the user for their date of birth in `YYYY-MM-DD` format and then <strike>sings</strike> prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from _Rent_, without any `and` between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use `datetime.date.today` to get today’s date, per [docs.python.org/3/library/datetime.html#datetime.date.today](https://docs.python.org/3/library/datetime.html#datetime.date.today).

Structure your program per the below, not only with a `main` function but also with one or more other functions as well:

```
from datetime import date


def main():
    ...


...


if __name__ == "__main__":
    main()
```

You’re welcome to import other (built-in) libraries, or any that are specified in the below hints. Exit via `sys.exit` if the user does not input a date in `YYYY-MM-DD` format. Ensure that your program will not raise any exceptions.

Either before or after you implement `seasons.py`, additionally implement, in a file called `test_seasons.py`, **one or more** functions that test your implementation of any functions besides `main` in `seasons.py` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_seasons.py
```
