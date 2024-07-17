import pandas as pd
import urllib
import os
import requests
from tqdm import tqdm
from datetime import datetime
import time


def download(url, chunk_size, output_file):

    with requests.get(url, stream=True) as res:
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

    start_date = "2024-04-01"
    end_date = "2024-04-02"
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
        print(f"Writing from {url} to {os.path.join(output_dir, output_file)}")
        download(
            url=url,
            chunk_size=1024 * 8,
            output_file=os.path.join(output_dir, output_file),
        )
        print("Download complete")
        print("\n")
        time.sleep(30)
