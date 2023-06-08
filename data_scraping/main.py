from .helperFunc.helpers import process_string_list, create_file_if_not_exists
from .playwright_scraper import activate_playwright_and_scrape

if __name__ == '__main__':

    # neighbourhoods = burnaby_part1
    # if none, scrapes the entire city
    neighbourhoods = None

    city = 'vancouver'
    province = 'bc'
    DoNotShowBrowser = True

    startingPageNumber = 1
    endingPageNumber = 2

    csv_path = f'./{city}_real_estate_data.csv'

    # for dev purposes, scrape only one listing
    testSingleListing = False
    showLogs = True

    """
    PREPARE INPUTS
    """
    # lower case and replace spaces with '-'
    neighbourhoods = process_string_list(neighbourhoods) if neighbourhoods != None else None

    create_file_if_not_exists(csv_path)

    # Call the function with the specified parameters
    activate_playwright_and_scrape(
        city=city, 
        province=province, 
        neighbourhoods=neighbourhoods, 
        csv_path=csv_path, 
        starting_page_number=startingPageNumber, 
        ending_page_number=endingPageNumber, 
        test_single_listing=testSingleListing, 
        show_logs=showLogs, 
        do_not_show_browser=DoNotShowBrowser
    )