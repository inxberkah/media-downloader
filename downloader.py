import requests
import os
import random
import string
import urllib.parse
#Author Berkah@code:~

def download_media(url, save_folder, media_type):
    try:
        response = requests.get(url)
        response.raise_for_status()

        parsed_url = urllib.parse.urlparse(url)
        file_name = os.path.basename(parsed_url.path)

        random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        file_extension = os.path.splitext(file_name)[1]
        if not file_extension:
            file_extension = '.jpg' if media_type == 'image' else '.mp4'

        save_path = os.path.join(save_folder, f'{random_filename}{file_extension}')

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"{media_type.capitalize()} berhasil diunduh dan disimpan di {save_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengunduh {url}: {str(e)}")

def download_media_from_file(file_path, save_folder, media_type):
    with open(file_path, 'r') as file:
        media_urls = file.read().splitlines()

    for url in media_urls:
        download_media(url, save_folder, media_type)

def create_new_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def main():
    print("Pilih opsi:")
    print("1. Unduh gambar")
    print("2. Unduh video")
    option = input("Masukkan pilihan (1/2): ")

    file_path = input("Path file: ")
    save_folder = input("Folder to save: ")

    create_new_folder(save_folder)

    if option == '1':
        download_media_from_file(file_path, save_folder, 'image')
    elif option == '2':
        download_media_from_file(file_path, save_folder, 'video')
    else:
        print("Opsi yang dimasukkan tidak valid.")

if __name__ == "__main__":
    main()
