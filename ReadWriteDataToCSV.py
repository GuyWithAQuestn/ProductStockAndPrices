from datetime import date
import csv #imported csvkit

#for copying files
import shutil #imported shutils

#for sorting lists of hard drives
def getKeyPrice(obj):
    return obj.price

def getKeyWebsite(obj):
    return obj.website

def getKeyCapacity(obj):
    return int(obj.capacity)

# ****

def read_in_and_write_out_csv_file(list_of_prices):
    i = 0
    x = 0
    comment = ""

    originalCSVFile = r'/Users/bryan/Downloads/wd.csv'
    # Write the contents of HDDList to a temporary .CSV file
    tempCSVFile = r'TEMP.csv'
    # tempCSVFile = "TEMP.csv"

    # To write read the CSV file
    # CSVfile = open('WD.csv')
    CSVfile = open(originalCSVFile)
    # CSVfile = open('WDPrices.csv')
    csv_f = csv.reader(CSVfile)

    # HDDList will contain all of the csv file with the prices
    HDDList = []
    for row in csv_f:
        HDDList.append(row)

    todaysDate = date.today()
    todaysDateStringbeforestrippingzeroes = todaysDate.strftime('%m/%d/%y')

    # Need to get rid of any leading 0 in the month and day, e.g. 05/01/23 --> 5/1/23
    # Split the date string into day, month, and year components using the forward slash as a delimiter
    day, month, year = todaysDateStringbeforestrippingzeroes.split('/')

    # Strip the leading zero from the day and month components using the lstrip() method
    day = day.lstrip('0')
    month = month.lstrip('0')

    # Reconstruct the date string with the modified day and month components
    todaysDateString = f'{day}/{month}/{year}'

    #strip out left 0 so that the string can be matched.
#    todaysDateString = todaysDate.strftime('%m/%d/%y').replace("/0", "/") #Should be good unless we go back before 2010
    todaysDateWeekDay = todaysDate.strftime('%A')

    print("todaysDateString: ")
    print(todaysDateString)
    # find the entry with today's date and update the prices into the array

    for s in HDDList:
        if todaysDateString in s:
            x = i
            print("found it")
            print(i)
            print("Existing Data: ")
            print(HDDList[i])
            #		print ("FakeDataToInsert: ")
            #		print (fakeDataToInsert)
            #		HDDList[i] = fakeDataToInsert
            print(todaysDate)
            print("S=")
            print(s)
            break
        else:
            print(i)
        i += 1

    print("i now =")
    print(i)
    print("X now =")
    print(x)

    date_and_day = []
    j = 0

    date_and_day.append(todaysDateString)
    date_and_day.append(todaysDateWeekDay)

    # Update the HDDList with the new data

    print("date_and_day")
    print(date_and_day)

    print("list_of_prices")
    print(list_of_prices)

    print("i")
    print(i)
    print("HDDList")
    print(HDDList)
    print("HDDList[i]")
    print(HDDList[i])

    #move the date & day in the list that will be put in csv
    date_day_and_prices = []
    for each in date_and_day:
        date_day_and_prices.append(each)

    #move the prices in the list that will be put in csv
    for each in list_of_prices:
        date_day_and_prices.append(each)

    print("date_day_and_prices")
    print(date_day_and_prices)


    # error out here when one of the Best Buy pages asks to do a survey ??????
    HDDList[i] = date_day_and_prices
    print("HDDList: ")
    print(HDDList)


    # writing to csv file
    with open(tempCSVFile, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(HDDList)

    # If all goes well, copy the temp file to the original existig WD file
    shutil.copyfile(tempCSVFile, originalCSVFile)

    return 0

def list_of_prices_sorted_by_website_then_capacity(list_of_HDDs_sorted_by_Website_then_Capacity):

    big_list_of_hdds_prices = []
    big_list_of_hdds_prices_with_website = []


    for each_item in list_of_HDDs_sorted_by_Website_then_Capacity:
        for each in each_item:
            # print(each.website)
            # print(each.capacity)
            big_list_of_hdds_prices.append(each.price)
            big_list_of_hdds_prices_with_website.append(each.website)
            big_list_of_hdds_prices_with_website.append(each.price)



    print("big_list_of_hdds_prices_with_website")
    print(big_list_of_hdds_prices_with_website)

    print("big_list_of_hdds_prices")
    print(big_list_of_hdds_prices)

    return big_list_of_hdds_prices

def sort_unique_websites_alphabetically(unique_list_of_websites):

    #unique_list_of_websites_sorted_alphabetically = unique_list_of_websites.sort(key=getKeyWebsite,reverse=False)
    unique_list_of_websites_sorted_alphabetically = sorted(unique_list_of_websites, reverse=False)
    print("unique_list_of_websites")
    print(unique_list_of_websites)
    print("unique_list_of_websites_sorted_alphabetically")
    print(unique_list_of_websites_sorted_alphabetically)

    return unique_list_of_websites_sorted_alphabetically

def sort_hdds_by_capacity(list_of_hard_drive_items):
    # Sort hard drives by capacity (highest capacity to least capacity)
    sorted_list = []
    list_of_hard_drive_items.sort(key=getKeyCapacity,reverse=True)
    print("Sort by Capacity")
    print(list_of_hard_drive_items)

    for each_instance in list_of_hard_drive_items:
        print(each_instance.capacity)
        print(each_instance.price)
        sorted_list.append(each_instance)

    return sorted_list

def get_unique_website_names(list_of_hard_drive_items):
    unique_list_of_websites = []

    for each_instance in list_of_hard_drive_items:
         # print(each_instance.website)
         # print(each_instance.price)
         if each_instance.website not in unique_list_of_websites:
             unique_list_of_websites.append(each_instance.website)

    # print("unique_list_of_websites")
    # print(unique_list_of_websites)

    return unique_list_of_websites

def group_hdds_by_website(unique_list_of_websites, hdds_sorted_by_capacity):

    list_of_lists_of_hdds_by_website_then_then_capacity = []

    for each_website in unique_list_of_websites:
        list_of_hdds_for_website = []

        for each_instance in hdds_sorted_by_capacity:
            if each_website == each_instance.website:
                list_of_hdds_for_website.append(each_instance)

        list_of_lists_of_hdds_by_website_then_then_capacity.append(list_of_hdds_for_website)


    # list_iteration = 1
    # for each_websites_prices in master_list_of_prices_based_on_website:
    #     print("list_iteration")
    #     print(list_iteration)
    #     list_iteration = list_iteration + 1
    #     print(each_websites_prices)


    return list_of_lists_of_hdds_by_website_then_then_capacity
def sortListOfDevicesForOutput(list_of_hard_drive_items):
    # since each of the URLs were accessed randomly (to help decrease chances of being detected as a bot)
    # Going to group each of the hard drives by their website name
    # create a unique list of website names
    unique_list_of_websites = get_unique_website_names(list_of_hard_drive_items)

    print("unique_list_of_websites")
    print(unique_list_of_websites)

    unique_list_of_websites_sorted_alphabetically = sort_unique_websites_alphabetically(unique_list_of_websites)

    # For each website name, create a list within a list
    #[website nameA [list of drives prices], website nameB [list of drives prices], etc]



    #initially sort all the list by capacity
    hdds_sorted_by_capacity = sort_hdds_by_capacity(list_of_hard_drive_items)

    #then break them up by the website they belong to
    list_of_lists_of_hdds = group_hdds_by_website(unique_list_of_websites_sorted_alphabetically, hdds_sorted_by_capacity)

    print("list_of_lists_of_hdds")
    print(list_of_lists_of_hdds)

    list_of_HDDs_sorted_by_Website_then_Capacity = []

    for each_group in list_of_lists_of_hdds:
        print("each_group")
        print(each_group)

        list_of_HDDs_sorted_by_Website_then_Capacity.append(each_group)

    return list_of_HDDs_sorted_by_Website_then_Capacity



    # master_list_of_prices_based_on_website = []




    # *****