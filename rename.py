#!/usr/bin/env python


#
# Estos son todos los datos de agosto de la estacion UNAH...
# te mande una foto por WhatsApp..
# o sea que ocupo tener 5 carpetas, que se llamaran UNAH2012 hasta UNAH 2016;
# una por cada semana GPS.
#
# Y adentro de cada semana debo tener los archivos de medicion de esa semana;
# por ejemplo para la semana UNAH2012 tendre 4 archivos de la primera semana de agosto:
# UNAH2130.AS; UNAH2140.AS, UNAH2150.AS, UNAH2160.AS. Y asi, sucesivamente para to do el mes
#
#


import os
from datetime import datetime


STARTING_GPS_WEEK_DATE = "19800106"

# STARTING_DATE = "20180729"
# STARTING_GPS_DATE = 210
# STARTING_GPS_WEEK = 2012


def get_new_name(old_name):

    # old_name = "unah20180910_000000.AS"

    mydate_str = old_name[:12]
    mydate_str = mydate_str[-8:]

    mydate = datetime.strptime(mydate_str, '%Y%m%d')
    # print mydate
    starting_gps_week_date = datetime.strptime(STARTING_GPS_WEEK_DATE, '%Y%m%d')
    diff_to_gps_week = mydate - starting_gps_week_date
    # print diff.days

    # Logic to calculate day of the year
    first_day_of_the_year = datetime.strptime(str(mydate.year) + "0101", '%Y%m%d')
    diff_to_first_day_of_the_year = mydate - first_day_of_the_year
    day_of_the_year = 1 + diff_to_first_day_of_the_year.days

    # Add leading zeros
    if day_of_the_year < 10:
        day_of_the_year = "00" + str(day_of_the_year)
    elif day_of_the_year < 100:
        day_of_the_year = "0" + str(day_of_the_year)
    else:
        day_of_the_year = str(day_of_the_year)

    # Logic to calculate gps week
    gps_week = diff_to_gps_week.days/7
    # print gps_week

    # Get the prefix
    prefix = old_name[:4]
    prefix = prefix.upper()
    # print prefix

    # Get the file extension
    k = old_name.rfind(".") + 1
    file_extension = old_name[k:]
    # print file_extension

    new_name = prefix + str(gps_week) + "/" + prefix + day_of_the_year + "0." + file_extension
    # print new_name

    return new_name, gps_week, prefix


def get_months():
    months = []
    for x in os.listdir('.'):
        # Get all the folders starting with 201 (2018, 2019, etc.)
        if x.startswith("201") and os.path.isdir(x):
            months.append(x)

    return months


def main():

    print ""

    # old_name = "unah20170724_000000.AS"
    # new_name, gps_week, prefix = get_new_name(old_name)
    #
    # print new_name
    #
    # print "gps week: " + str(gps_week)

    # Get all the months (folders) to process
    months = get_months()

    # Go over each month
    for month in months:
        # Retrieve files and iterate over each file
        for root, dirs, files in os.walk("./" + month + "/"):
            for filename in files:
                old_name = filename
                # Generate new name based on date and gps week (new folder)
                new_name, gps_week, prefix = get_new_name(old_name)
                print filename + "   renamed to   " + new_name

                # Check if gps week folder exist
                folder_exist = os.path.exists("./" + month + "/" + prefix + str(gps_week))
                # Create new folder if not found
                if folder_exist is not True:
                    os.mkdir("./" + month + "/" + prefix + str(gps_week))
                # Actual renaming
                os.rename("./" + month + "/" + old_name, "./" + month + "/" + new_name)

    print ""
    print "Done..!!"
    print ""


if __name__ == '__main__':
    main()
