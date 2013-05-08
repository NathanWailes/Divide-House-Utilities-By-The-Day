# Copyright (c) 2012 Nathan Wailes

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author(s): Nathan Wailes

#I have made a YouTube video giving the same explanation I write below:
#http://bit.ly/13O2tkE

#This program was written for Python 2.7.3

#This program divides house utilities by the DAY instead of by the MONTH, and
#then generates a report that lists the amount each person in the house owes
#and how this number was generated, bill-by-bill, so that anyone can check
#any step by hand if they want to.

#I made this program because I was living in a row house where people were
#frequently moving in and out, and they only wanted to pay for the days they
#were living in the house, and the bills spanned different lengths of time,
#and so calculating what everyone owed each month was a real pain.

#How the program works:

#There are two main types of data I use: info about the people living in the
#house, and info about the bills.  I have two arrays to handle these two
#types of data, you can find them pretty easily by looking below.

#The program goes through the bills one-by-one (using a "for" loop) and for each
#bill it then goes through the list of people to count up how many days each
#person was in the house for the period of that bill.  It adds up all those days
#to get the TOTAL PERSON DAYS.  I need to calculate this number before I start
#figuring out how much each person owes.  A simple example: Suppose I was in the
#house for only one day during the period of a bill.  How much should I pay?
#Well, it depends on how many days everyone else was in the house!  That's why
#I need to calculate the total-persond-days.

#Once I have the total-person-days, I then divide the bill by that amount to get
#the bill amount per person-day.  This makes the bill into something like a
#subway fare, where you pay a small amount everytime you use the house one day.

#Once I have the bill-amount-per-person-days, I then loop through the people
#again and multiply the number of days each person was in the house by the
#daily "fare" (bill-per-person-day) to arrive at how much that person owes for
#that bill.

#I print all this info out for this bill, and then I move on to the next bill!

#After doing this for all the bills, I tally up the total amount of the bills
#and print that out, and then print out the total amounts that each person owes,
#and print that out.  This bottom part is what I really need; the stuff above it
#is just to make it easy to check the program's work.

##################This line is exactly 80 characters long#######################

#this figures out how many days a person was present during a particular bill
#period
def bill_period_person_days(bill_start, bill_end, person_start, person_end):

  from datetime import timedelta
  
  #tell the program the variable exists so that the scope is set properly
  bill_period_person_days = timedelta(days=0)

  #it's REALLY helpful to draw examples on a timeline to understand these
  #rules
  #if the bill started after the person arrived before before the person left...
  if (bill_start >= person_start and bill_start <= person_end):
    if (bill_end >= person_end):
      bill_period_person_days = person_end - bill_start
    if (bill_end < person_end):
      bill_period_person_days = bill_end - bill_start
  #if the bill started before the person arrived but ended after the person
  #arrived...
  if (bill_start < person_start and bill_end >= person_start):
    if (bill_end >= person_end):
      bill_period_person_days = person_end - person_start
    if (bill_end < person_end):
      bill_period_person_days = bill_end - person_start
  
  #I'm doing this because if you just subtract dates from each other you end up
  #being one short.  If a person arrived on the 22nd and the bill ends on the
  #22nd, the subtraction will show up as zero but I want them to be charged for
  #that day.
  if bill_period_person_days.days >= 0:
    bill_period_person_days = bill_period_person_days.days + 1
  else:
    bill_period_person_days = 0

  #If the person wasn't in the house for the period of the bill
  if (bill_end < person_start) or (bill_start > person_end):
    bill_period_person_days = 0

  return bill_period_person_days



def main():

  import time
  from datetime import date

  #Format:         Name,     Move-in Date,       Move-out Date,  Total Amnt Owed
  people_data = [
                 ["Angelo", date(2012, 12, 1), date(2015, 1, 1), 0],
                 ["Feleg", date(2010, 10, 1), date(2015, 1, 1), 0],
                 ["Jasna", date(2012, 11, 15), date(2015, 1, 1), 0],
                 ["Kara", date(2012, 10, 13), date(2015, 1, 1), 0],
                 ["Luella", date(2011, 8, 1), date(2015, 1, 1), 0],
                 ["Masha", date(2012, 6, 1), date(2015, 1, 1), 0],
                 ["Nathan", date(2010, 10, 1), date(2015, 1, 1), 0],
                 ["Rocky", date(2012, 8, 1), date(2015, 1, 1), 0]               
                ]
  #I'm making these position variables so that it'll be easier to read when I
  #refer to them in the future
  ppl_name_pos = 0
  ppl_move_in_pos = 1
  ppl_move_out_pos = 2
  ppl_total_amount_owed_pos = 3

  #Format :          Name,            Amount,   Start Date,   End Date
  bill_data = [
               ["Pepco 11/5-12/6", 255.75, date(2012, 11, 5), \
                date(2012, 12, 6)],
               ["Verizon 11/22-12/22", 39.99, date(2012, 11, 22), \
                date(2012, 12, 22)],
               ["Washington Gas 11/6-12/10", 159.11, date(2012, 11, 6), \
                date(2012, 12, 10)]
              ]
  #I'm making these position variables so that it'll be easier to read when I
  #refer to them in the future
  bill_name_pos = 0
  bill_amount_pos = 1
  bill_start_pos = 2
  bill_end_pos = 3
  
  for b in range(len(bill_data)):
    #basically for each bill I want a list of the people who were present at
    #some point during that bill, w/ how many days each person was present,
    #the total number of person-days, the amount of bill for each person-day,
    #and the amount each person owes.  If I list all that it should be very easy
    #to check the work if someone's interested.
    
    #Come up with a nickname for these things so they're easier to talk about
    bill_name = bill_data[b][bill_name_pos]
    bill_amount = bill_data[b][bill_amount_pos]
    bill_start = bill_data[b][bill_start_pos]
    bill_end = bill_data[b][bill_end_pos]

    #initializing this; I'll use it to keep track of all the person-days
    total_person_days = 0

    print "\n" + bill_name + " - $" + str(bill_amount)

    #this for-loop is to calculate the total person-days
    for p in range(len(people_data)):
      p_name = people_data[p][ppl_name_pos]
      p_move_in_date = people_data[p][ppl_move_in_pos]
      p_move_out_date = people_data[p][ppl_move_out_pos]
      p_person_days = bill_period_person_days(bill_start, bill_end, \
                                              p_move_in_date, p_move_out_date)

      if p_person_days > 0:
        total_person_days += p_person_days

    bill_amount_per_person_day = bill_amount / total_person_days
    
    print "Total person-days: " + str(total_person_days) + "\n" + \
          "Bill amount per person-day: $" + \
          str(round(bill_amount_per_person_day, 4))

    #this for-loop is to calculate what each person owes for that bill
    for p in range(len(people_data)):
      p_name = people_data[p][ppl_name_pos]
      p_move_in_date = people_data[p][ppl_move_in_pos]
      p_move_out_date = people_data[p][ppl_move_out_pos]
      p_person_days = bill_period_person_days(bill_start, bill_end, \
                                              p_move_in_date, p_move_out_date)
      p_amount_owed = 0 #amount owed for just this bill

      if p_person_days > 0:
        p_amount_owed = p_person_days * bill_amount_per_person_day

        #this lets me keep track of what everyone owes for ALL bills        
        people_data[p][ppl_total_amount_owed_pos] += p_amount_owed
        
        print p_name + " (" + str(p_person_days) + " days, $" + \
              str(round(p_amount_owed, 2)) + ")"

  total_bills = 0
  for b in range(len(bill_data)):
    total_bills += bill_data[b][bill_amount_pos]
    
  print "\nTotal bills/expenses: $" + str(round(total_bills, 2)) + "\n" + \
        "Total amounts owed by each person for these bills:"
  for p in range(len(people_data)):
    p_name = people_data[p][ppl_name_pos]
    p_total_amount_owed = people_data[p][ppl_total_amount_owed_pos]

    print p_name + ": $" + str(round(p_total_amount_owed, 2))



    
# Prevents main() from running if this python file is loaded as a library.
if __name__ == '__main__':
  main()
