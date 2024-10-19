import datetime
import jdatetime


def show_gregorian_age(birth):
    thisyear = datetime.datetime.now().year
    age = thisyear - birth
    print(age)


def show_jalali_age(birth):
    thisyear = jdatetime.datetime.now().year
    age = thisyear - birth
    print(age)


show_jalali_age(1363)
show_gregorian_age(1980)
