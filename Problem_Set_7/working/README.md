# Working 9 to 5

Whereas [most countries](https://en.wikipedia.org/wiki/Date_and_time_representation_by_country#Time) use a [24-hour clock](https://en.wikipedia.org/wiki/24-hour_clock), the United States tends to use a [12-hour clock](https://en.wikipedia.org/wiki/12-hour_clock). Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

<details><summary>Conversion Table</summary><br/>
<p>Just as “12:00 AM” in 12-hour format would be “00:00” in 24-hour format, so would “12:01 AM” through “12:59 AM” be “00:01” through “00:59”, respectively.</p>

<div>
   <div></div>
   <div>
      <div>
         <table></table>
      </div>
      <div>
         <table>
            <thead>
               <tr>
                  <th data-field="0">
                     <div>
                        <div style="text-align: left">12-Hour</div>
                     </div>
                     <div></div>
                  </th>
                  <th data-field="1">
                     <div>
                        <div style="text-align: left">24-Hour</div>
                     </div>
                     <div></div>
                  </th>
               </tr>
            </thead>
            <tbody>
               <tr data-index="0">
                  <td>12:00 AM</td>
                  <td>00:00</td>
               </tr>
               <tr data-index="1">
                  <td>1:00 AM</td>
                  <td>01:00</td>
               </tr>
               <tr data-index="2">
                  <td>2:00 AM</td>
                  <td>02:00</td>
               </tr>
               <tr data-index="3">
                  <td>3:00 AM</td>
                  <td>03:00</td>
               </tr>
               <tr data-index="4">
                  <td>4:00 AM</td>
                  <td>04:00</td>
               </tr>
               <tr data-index="5">
                  <td>5:00 AM</td>
                  <td>05:00</td>
               </tr>
               <tr data-index="6">
                  <td>6:00 AM</td>
                  <td>06:00</td>
               </tr>
               <tr data-index="7">
                  <td>7:00 AM</td>
                  <td>07:00</td>
               </tr>
               <tr data-index="8">
                  <td>8:00 AM</td>
                  <td>08:00</td>
               </tr>
               <tr data-index="9">
                  <td>9:00 AM</td>
                  <td>09:00</td>
               </tr>
               <tr data-index="10">
                  <td>10:00 AM</td>
                  <td>10:00</td>
               </tr>
               <tr data-index="11">
                  <td>11:00 AM</td>
                  <td>11:00</td>
               </tr>
               <tr data-index="12">
                  <td>12:00 PM</td>
                  <td>12:00</td>
               </tr>
               <tr data-index="13">
                  <td>1:00 PM</td>
                  <td>13:00</td>
               </tr>
               <tr data-index="14">
                  <td>2:00 PM</td>
                  <td>14:00</td>
               </tr>
               <tr data-index="15">
                  <td>3:00 PM</td>
                  <td>15:00</td>
               </tr>
               <tr data-index="16">
                  <td>4:00 PM</td>
                  <td>16:00</td>
               </tr>
               <tr data-index="17">
                  <td>5:00 PM</td>
                  <td>17:00</td>
               </tr>
               <tr data-index="18">
                  <td>6:00 PM</td>
                  <td>18:00</td>
               </tr>
               <tr data-index="19">
                  <td>7:00 PM</td>
                  <td>19:00</td>
               </tr>
               <tr data-index="20">
                  <td>8:00 PM</td>
                  <td>20:00</td>
               </tr>
               <tr data-index="21">
                  <td>9:00 PM</td>
                  <td>21:00</td>
               </tr>
               <tr data-index="22">
                  <td>10:00 PM</td>
                  <td>22:00</td>
               </tr>
               <tr data-index="23">
                  <td>11:00 PM</td>
                  <td>23:00</td>
               </tr>
               <tr data-index="24">
                  <td>12:00 AM</td>
                  <td>00:00</td>
               </tr>
            </tbody>
         </table>
      </div>
      <div></div>
   </div>
   <div></div>
</div>
</details>

In a file called `working.py`, implement a function called `convert` that expects a `str` in any of the 12-hour formats below and returns the corresponding `str` in 24-hour format (i.e., `9:00 to 17:00`). Expect that `AM` and `PM` will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

- `9:00 AM to 5:00 PM`
- `9 AM to 5 PM`
- `9:00 AM to 5 PM`
- `9 AM to 5:00 PM`

Raise a `ValueError` instead if the input to `convert` is not in either of those formats or if either time is invalid (e.g., `12:60 AM`, `13:00 PM`, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., `5:00 PM` to `9:00 AM`).

Structure `working.py` as follows, wherein you’re welcome to modify `main` and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use `re` and/or `sys`.

```
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
```

Either before or after you implement `convert` in `working.py`, additionally implement, in a file called `test_working.py`, **three or more** functions that collectively test your implementation of `convert` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:
