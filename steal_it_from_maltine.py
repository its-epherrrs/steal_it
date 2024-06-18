import requests
from bs4 import BeautifulSoup
import os

# Define the base URL
base_url = 'http://maltinerecords.cs8.biz/release.html'

# Create a session
session = requests.Session()

# Fetch the content of the main page
response = session.get(base_url)
response.raise_for_status()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all release links within the div with id 'content'
content_div = soup.find('div', id='content')
release_links = content_div.find_all('a', href=True)

# Directory to save the downloads
download_dir = './downloads'
os.makedirs(download_dir, exist_ok=True)

# Function to download a file from a URL
def download_file(url, download_path):
    response = session.get(url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)

# Process each release link
for link in release_links:
    try:
        relative_link = link['href']
        release_url = f'http://maltinerecords.cs8.biz/{relative_link}'
        release_page_response = session.get(release_url)
        release_page_response.raise_for_status()
        release_soup = BeautifulSoup(release_page_response.content, 'html.parser')
        
        # Find the download link in the div with class 'right' that ends with '.zip'
        right_div = release_soup.find('div', class_='right')
        if right_div:
            download_link = right_div.find('a', href=lambda href: href and href.endswith('.zip'))
            if download_link:
                download_url = download_link['href']
                if not download_url.startswith('http'):
                    download_url = f'http://maltinerecords.cs8.biz/{download_url}'
                filename = os.path.join(download_dir, os.path.basename(download_url))
                print(f'Downloading {download_url} to {filename}')
                download_file(download_url, filename)
            else:
                print(f'No .zip download link found on page: {release_url}')
        else:
            print(f'No right div found on page: {release_url}')
    except requests.exceptions.HTTPError as e:
        print(f'HTTP error for URL {release_url}: {e}')
    except Exception as e:
        print(f'An error occurred for URL {release_url}: {e}')
