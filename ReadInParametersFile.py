import os

def open_and_read_file():

    # Often times the script is not executed from where the file's actually exist, and therefore can't find the files, even if
    # they seem to be in the same directory. Therefore, use the absolute path
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'ScrapeParameters.txt')

    # Going to bypass the inputs, and get inputs from the file instead
    FileParametersReadIn = open(filename, "r")
    collected_data_as_string = FileParametersReadIn.readlines()
    FileParametersReadIn.close()
    print("Here's what I read in: ", collected_data_as_string)

    # each_line = collected_data_as_string

    # list_of_urls = collected_data_as_string[0].split("\n")

    # dates_and_times_to_search = str(collected_data_as_list[0])
    # dates_and_times_to_search_list = dates_and_times_to_search.split("|")
    #
    # location_service_provider = str(collected_data_as_list[1])
    # location_service_provider_list = location_service_provider.split("|")
    #
    # email_address = str(collected_data_as_list[2])
    # email_password = str(collected_data_as_list[3])

    #    which_bundled_preferences = str(collected_data_as_list[1]).strip('\n')
    # had to add in the above .strip('\n') as a newline character was coming along with the last variable there and messing things up

    return collected_data_as_string


def mainBody():
    dates_and_times_to_search_list, location_service_provider_list, email_address, email_password = open_and_read_file()
    return dates_and_times_to_search_list, location_service_provider_list, email_address, email_password
