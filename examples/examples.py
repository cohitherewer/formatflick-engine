import json
from formatflick.formatflick import *
import requests
import pandas as pd
import csv

"""
This example has been created to demonstrate how we can convert a json file into csv file
The first function create_sample_json_file is just a function that will create a random json file
We dont need to worry about that file as it is not related to the actual formatflick code

the second function demonstrate the usage of the formatflick module
"""


def create_sample_json_file():
    # call the api
    value = requests.get("http://universities.hipolabs.com/search?country=United+States")
    print(f"Status Code: {value.status_code}")

    if value.status_code != 200:
        raise Exception("Some problem with the API call. Check the API")

    # create the json file
    with open("sample.json", "w") as file:
        json.dump(value.json(), file, indent=4)


def example_1():
    """
    This function initiates the formatflick and converts into from json file to csv file
    """
    create_sample_json_file()
    # convert from json file to csv file
    # initiate the formatflick
    print("Initiating formatflick")
    core = formatflick(source="sample.json",
                       destination=None,  # change to unset the default file name "result"
                       destination_extension=".csv",  # set if you dont destination is None
                       verbosity=2,  # has no effect till now
                       mode='file'  # by default set to 'file
                       )
    print("Converting...")
    core.convert()
    print("Conversion Done...")


def create_sample_csv():
    url = 'https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv'
    ret = requests.get(url)
    print(f"Status Code: {ret.status_code}")
    with open("sample.csv", "wb") as file:
        file.write(ret.content)


def example_2():
    """
    This function initiates the formatflick and converts from csv to json
    """
    create_sample_csv()
    print("Initiating formatflick")
    core = formatflick(source="sample.csv",
                       destination=None,  # change to unset the default file name "result"
                       destination_extension=".json",  # set if you dont destination is None
                       verbosity=2,  # has no effect till now
                       mode='file'  # by default set to 'file
                       )
    print("Converting...")
    core.convert()
    print("Conversion Done...")


def remove_files():
    import os
    import glob
    for item in [".csv", ".json", "xml"]:
        csv_files = glob.glob(f"*{item}")
        for file in csv_files:
            os.remove(file)
            print(f"Deleted: {file}")


if __name__ == "__main__":
    # example_2()

    remove_files() # occasanly run this function to delete all the junk files
