#coding: utf-8

import pandas as pd
import requests
import time
from datetime import datetime
import calendar
import re
import argparse

options = argparse.ArgumentParser()
options.add_argument('--file', type=argparse.FileType('r'), required=True)


def read_csv(file):
    df = pd.read_csv(file)
    return df


def time_convert(time):
    splited_time = re.split("[// :: ]",time)
    formatted_time = "-".join(splited_time[0:3]) + ' ' + ":".join(splited_time[3:6]) + ' ' + splited_time[6]
    utc = datetime.strptime(formatted_time, "%m-%d-%Y %I:%M:%S %p")
    return calendar.timegm(utc.timetuple())
    

def get_price(unix_time):
    api_url = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=JPY&ts=" \
              + str(unix_time) \
              + "&markets=Coincheck"
    r = requests.get(api_url)
    json = r.json()
    return json['BTC']['JPY']


def save_file(df):
    csv_name = "bittrex_result" + str(datetime.now().strftime("%Y%m%d%H%M%S")) + ".csv"
    df.to_csv(csv_name, index=False)
    

def main(opt):
    df = read_csv(opt.file)
    df["Opened(UNIX)"] = df["Opened"].apply(time_convert)
    df["BTC_Price(JPY)"] = df["Opened(UNIX)"].apply(get_price)
    df["Price(JPY)"] = (df["BTC_Price(JPY)"] * df["Price"]).round(2)
    save_file(df)
    exit(0)
    

if __name__ == '__main__':
    main(options.parse_args())
