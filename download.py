import urllib
import logging
import os
import time
import argparse
import requests
import pandas as pd
from tqdm import tqdm
from datetime import datetime


def download(url, chunk_size, output_file):

    with requests.get(url, stream=True, headers={"User-Agent": "Mozilla/5.0"}) as res:
        res.raise_for_status()
        file_size = int(res.headers.get("Content-Length", 0))

        with open(output_file, "wb") as outfile:
            progress = tqdm(
                total=file_size, unit="B", unit_scale=True, desc="Downloading"
            )  # Initialize tqdm
            for chunk in res.iter_content(chunk_size):
                outfile.write(chunk)
                progress.update(len(chunk))  # Update progress bar for each chunk
            progress.close()  # Close


if __name__ == "__main__":

    sleep = 30

    # Set up logging
    fmt = "%(asctime)s [%(levelname)s] [%(filename)s:%(funcName)s] - %(message)s"
    datefmt = "%Y-%m-%dT%H:%M:%SZ"
    logging.basicConfig(
        format=fmt, datefmt=datefmt, level=os.environ.get("LOGLEVEL", "INFO")
    )

    # Set up argument parser for command line
    parser = argparse.ArgumentParser(
        prog="SSEN smart meter downloader",
        description="This utitlity downloads LV feeder usage date from SSEN smart meter database.",
        epilog="Contact h.olakkengil@sheffield.ac.uk for help.",
    )
    parser.add_argument("-s", "--start_date")
    parser.add_argument("-e", "--end_date")

    args = parser.parse_args()

    start_date = args.start_date
    end_date = args.end_date
    format = "%Y-%m-%d"

    start_date = datetime.strptime(start_date, format)
    end_date = datetime.strptime(end_date, format)

    dates = pd.date_range(start=start_date, end=end_date, freq="d")

    output_dir = os.path.join(os.getenv("HOME"), "Downloads/ssen_download")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_url = "https://ssen-smart-meter-prod.portaljs.com/LV_FEEDER_USAGE/"

    for date in dates:
        output_file = str(date.strftime(format) + ".csv")
        url = base_url + output_file
        logging.info(f"Writing from {url} to {os.path.join(output_dir, output_file)}")
        download(
            url=url,
            chunk_size=1024 * 8,
            output_file=os.path.join(output_dir, output_file),
        )
        logging.info("Download complete")
        logging.info("Sleeping for {sleep} seconds")
        print("\n")
        time.sleep(sleep)
