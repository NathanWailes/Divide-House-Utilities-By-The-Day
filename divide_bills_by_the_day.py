"""

"""
from datetime import date
from collections import namedtuple


def print_a_report_given(people_data, bill_data):
    """ Basically for each bill I want a list of the people who were present at some point during that bill, with how
    many days each person was present, the total number of person-days, the amount of bill for each person-day, and the
    amount each person owes. If I list all that it should be very easy to check the work if someone's interested.

    :param people_data:
    :param bill_data:
    :return:
    """
    
    for bill in bill_data:
        total_num_of_person_days_in_bill_period = get_total_num_of_person_days_in_bill_period(people_data, bill)

        bill_amount_per_person_day = bill.amount / total_num_of_person_days_in_bill_period
        
        print("Total person-days: %s\nBill amount per person-day: $%s" % (total_num_of_person_days_in_bill_period,
              round(bill_amount_per_person_day, 4)))

        for person in people_data:
            num_of_days_person_was_present_in_bill_period = get_num_of_days_person_was_present_in_bill_period(bill, person)

            if num_of_days_person_was_present_in_bill_period > 0:
                amount_owed_for_this_bill = num_of_days_person_was_present_in_bill_period * bill_amount_per_person_day

                person.amount_owed += amount_owed_for_this_bill
                
                print("%s (%s days, $%s)" % (person.name, num_of_days_person_was_present_in_bill_period, round(amount_owed_for_this_bill, 2)))

    total_amount_across_all_bills = sum([bill.amount for bill in bill_data])
    print("\nTotal bills/expenses: $%s\nTotal amounts owed by each person for these bills:" % round(total_amount_across_all_bills, 2))

    for person in people_data:
        print("%s: $%s" % (person.name, round(person.amount_owed, 2)))


def get_total_num_of_person_days_in_bill_period(person, bill):
    """

    :return:
    """
    total_person_days_in_bill_period = 0

    print("\n%s - $%s" % (bill.name, bill.amount))

    for person in people_data:
        num_of_days_person_was_present_in_bill_period = get_num_of_days_person_was_present_in_bill_period(bill, person)

        if num_of_days_person_was_present_in_bill_period > 0:
            total_person_days_in_bill_period += num_of_days_person_was_present_in_bill_period

    return total_person_days_in_bill_period


def get_num_of_days_person_was_present_in_bill_period(bill, person):
    """ This figures out how many days a person was present during a particular bill period.

    Code taken from http://stackoverflow.com/a/9044111/4115031

    :param bill_start:
    :param bill_end:
    :param person_start:
    :param person_end:
    :return:
    """
    Range = namedtuple('Range', ['start', 'end'])
    bill_range = Range(start=bill.start, end=bill.end)
    persons_occupancy_range = Range(start=person.start, end=person.end)

    latest_start = max(bill_range.start, persons_occupancy_range.start)
    earliest_end = min(bill_range.end, persons_occupancy_range.end)

    overlap = (earliest_end - latest_start).days + 1

    return overlap if overlap > 0 else 0


class Person:
    def __init__(self, _name, _start, _end, _amount_owed):
        self.name = _name
        self.start = _start
        self.end = _end
        self.amount_owed = _amount_owed


if __name__ == '__main__':
    # Format: Name, Move-in Date, Move-out Date, Total Amnt Owed
    people_data = [["Angelo", date(2012, 12, 1), date(2015, 1, 1), 0],
                     ["Feleg", date(2010, 10, 1), date(2015, 1, 1), 0],
                     ["Jasna", date(2012, 11, 15), date(2015, 1, 1), 0],
                     ["Kara", date(2012, 10, 13), date(2015, 1, 1), 0],
                     ["Luella", date(2011, 8, 1), date(2015, 1, 1), 0],
                     ["Masha", date(2012, 6, 1), date(2015, 1, 1), 0],
                     ["Nathan", date(2010, 10, 1), date(2015, 1, 1), 0],
                     ["Rocky", date(2012, 8, 1), date(2015, 1, 1), 0]]
    people_data = [Person(*[value for value in item]) for item in people_data]

    # Format: Name, Amount, Start Date, End Date
    bill_data = [["Pepco 11/5-12/6", 255.75, date(2012, 11, 5), date(2012, 12, 6)],
                 ["Verizon 11/22-12/22", 39.99, date(2012, 11, 22), date(2012, 12, 22)],
                 ["Washington Gas 11/6-12/10", 159.11, date(2012, 11, 6), date(2012, 12, 10)]]
    Bill = namedtuple('Bill', ['name', 'amount', 'start', 'end'])
    bill_data = [Bill(*[value for value in item]) for item in bill_data]

    print_a_report_given(people_data, bill_data)
