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


STARTING_DATE = "20180729"
STARTING_GPS_DATE = 210
STARTING_GPS_WEEK = 2012


def get_new_name(old_name):
    # old_name = "unah20180910_000000.AS"
    old_name = old_name[:-10]
    old_name = old_name[-8:]

    mydate = datetime.strptime(old_name, '%Y%m%d')
    # print mydate
    starting_date = datetime.strptime(STARTING_DATE, '%Y%m%d')
    diff = mydate - starting_date
    # print diff.days

    # Logic to calculate gps date
    gps_date = STARTING_GPS_DATE + diff.days
    # print gps_date

    # Logic to calculate gps week
    gps_week = 1982 + gps_date/7
    # print gps_week

    new_name = "UNAH" + str(gps_week) + "/UNAH" + str(gps_date) + "0.AS"
    # print new_name

    return new_name, gps_week


def get_months():
    months = []
    for x in os.listdir('.'):
        # Get all the folders starting with 201 (2018, 2019, etc.)
        if x.startswith("201") and os.path.isdir(x):
            months.append(x)

    return months


def main():

    print ""
    # Get all the months (folders) to process
    months = get_months()

    # Go over each month
    for month in months:
        # Retrieve files and iterate over each file
        for root, dirs, files in os.walk("./" + month + "/"):
            for filename in files:
                old_name = filename
                # Generate new name based on date and gps week (new folder)
                new_name, gps_week = get_new_name(old_name)
                print filename + "   renamed to   " + new_name

                # Check if gps week folder exist
                folder_exist = os.path.exists("./" + month + "/UNAH" + str(gps_week))
                # Create new folder if not found
                if folder_exist is not True:
                    os.mkdir("./" + month + "/UNAH" + str(gps_week))
                # Actual renaming
                os.rename("./" + month + "/" + old_name, "./" + month + "/" + new_name)

    print ""
    print "Done..!!"
    print ""


if __name__ == '__main__':
    main()
