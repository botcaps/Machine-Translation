import os
import requests

# URLs for Multi30K splits (2016 version)
base_url = "https://raw.githubusercontent.com/multi30k/dataset/master/data/task1/raw/"
splits = {
    "train.en": "train.en.gz",
    "train.de": "train.de.gz",
    "train.fr": "train.fr.gz",
    "val.en": "val.en.gz",
    "val.de": "val.de.gz",
    "val.fr": "val.fr.gz",
    "test_2016_flickr.en": "test_2016_flickr.en.gz",
    "test_2016_flickr.de": "test_2016_flickr.de.gz",
    "test_2016_flickr.fr": "test_2016_flickr.fr.gz"
}

def download_file(url, dest):
    print(f"Downloading {url}...")
    r = requests.get(url)
    r.raise_for_status()
    with open(dest, 'wb') as f:
        f.write(r.content)
    print(f"Saved {dest}")

def main():
    folder = "multi30k_data"
    os.makedirs(folder, exist_ok=True)
    for split, filename in splits.items():
        url = f"{base_url}{filename}"
        dest = os.path.join(folder, filename)
        if not os.path.exists(dest):
            download_file(url, dest)
        else:
            print(f"{dest} already exists, skipping.")

if __name__ == "__main__":
    main()