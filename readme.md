#### General information

Author: Nathan Wailes

Targeted Python version: 3.5.2

I have made a YouTube video giving the same explanation I've written out below:
http://bit.ly/13O2tkE

#### What this program does

This program divides house utilities by the DAY instead of by the MONTH, and
then generates a report that lists the amount each person in the house owes
and how this number was generated, bill-by-bill, so that anyone can check
any step by hand if they want to.

I made this program because I was living in a row house where people were
frequently moving in and out, and they only wanted to pay for the days they
were living in the house, and the bills spanned different lengths of time,
and so calculating what everyone owed each month was a real pain.

#### How the program works:

There are two main types of data I use: info about the people living in the
house, and info about the bills.  I have two arrays to handle these two
types of data, you can find them pretty easily by looking below.

The program goes through the bills one-by-one (using a "for" loop) and for each
bill it then goes through the list of people to count up how many days each
person was in the house for the period of that bill.  It adds up all those days
to get the TOTAL PERSON DAYS.  I need to calculate this number before I start
figuring out how much each person owes.  A simple example: Suppose I was in the
house for only one day during the period of a bill.  How much should I pay?
Well, it depends on how many days everyone else was in the house!  That's why
I need to calculate the total-persond-days.

Once I have the total-person-days, I then divide the bill by that amount to get
the bill amount per person-day.  This makes the bill into something like a
subway fare, where you pay a small amount everytime you use the house one day.

Once I have the bill-amount-per-person-days, I then loop through the people
again and multiply the number of days each person was in the house by the
daily "fare" (bill-per-person-day) to arrive at how much that person owes for
that bill.

I print all this info out for this bill, and then I move on to the next bill!

After doing this for all the bills, I tally up the total amount of the bills
and print that out, and then print out the total amounts that each person owes,
and print that out.  This bottom part is what I really need; the stuff above it
is just to make it easy to check the program's work.
