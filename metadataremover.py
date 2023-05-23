import os
from PIL import Image


logo = r"""
                 _            _                                              
                | |          | |                                             
  _ __ ___   ___| |_ __ _  __| | __ _ _ __ ___ _ __ ___   _____   _____ _ __ 
 | '_ ` _ \ / _ \ __/ _` |/ _` |/ _` | '__/ _ \ '_ ` _ \ / _ \ \ / / _ \ '__|
 | | | | | |  __/ || (_| | (_| | (_| | | |  __/ | | | | | (_) \ V /  __/ |   
 |_| |_| |_|\___|\__\__,_|\__,_|\__,_|_|  \___|_| |_| |_|\___/ \_/ \___|_|   by @h3art_exe/ Lamer Qiz
"""

def remove_exif(image_path):
    image = Image.open(image_path)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save(image_path)

def main():
    print(logo)
    for filename in os.listdir('.'):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('png'):
            print(f"Removing metadata from {filename}...")
            remove_exif(filename)
    print("Done!")

if __name__ == "__main__":
    main()

