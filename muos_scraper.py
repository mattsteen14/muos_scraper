import argparse
import os
import requests
from urllib.parse import quote
from PIL import Image
from io import BytesIO

GITHUB_COMMIT = "00498a7f6db86bc45146b835ba1aeed58a1a1fe5"

def list_rom_files(folder):
    extensions = ('.zip', '.7z', '.nes', '.sfc', '.smc', '.gba', '.gbc', '.gb', '.n64', '.z64', '.v64', '.bin', '.iso', '.chd', '.rom', '.mgw', '.nds', '.vb', '.p8', '.32x', '.sms', '.md', '.ngc', '.wsc', '.ws', '.dsk', '.tap', '.z80')
    return [
        os.path.join(dp, f)
        for dp, _, files in os.walk(folder)
        for f in files
        if f.lower().endswith(extensions) and not f.startswith("._")
    ]

def resize_and_save_image(response_content, output_path, width=300):
    try:
        img = Image.open(BytesIO(response_content))
        w_percent = width / float(img.size[0])
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((width, h_size), Image.LANCZOS)
        img.save(output_path)
        print(f"✔ Resized + saved box: {output_path}")
    except Exception as e:
        print(f"✖ Error resizing image: {e}")

def download_libretro_thumbnail(libretro_folder, art_type, rom_name, output_path):
    filename = f"{rom_name}.png"
    encoded_filename = quote(filename, safe="")  # full encoding
    url = f"https://raw.githubusercontent.com/libretro-thumbnails/{libretro_folder}/{GITHUB_COMMIT}/{art_type}/{encoded_filename}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            if art_type == "Named_Boxarts":
                resize_and_save_image(response.content, output_path, width=300)
            else:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                print(f"✔ Saved full-size preview: {output_path}")
            return True
        else:
            print(f"✖ Not found: {filename} in {art_type} (status {response.status_code})")
            return False
    except Exception as e:
        print(f"✖ Error downloading {filename}: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MUOS Scraper CLI (libretro-thumbnails full name match)")
    parser.add_argument('--roms-folder', required=True, help='Path to ROMs folder')
    parser.add_argument('--libretro-folder', required=True, help='libretro-thumbnails GitHub folder (e.g. Amstrad_-_CPC)')
    parser.add_argument('--output-folder', required=True, help='Full MUOS output path including system name (e.g. .../catalogue/Amstrad CPC)')
    args = parser.parse_args()

    roms = list_rom_files(args.roms_folder)
    print(f"\n🎮 Found {len(roms)} ROM(s)\n")

    box_dir = os.path.join(args.output_folder, "box")
    preview_dir = os.path.join(args.output_folder, "preview")
    os.makedirs(box_dir, exist_ok=True)
    os.makedirs(preview_dir, exist_ok=True)

    for rom_path in roms:
        rom_name = os.path.splitext(os.path.basename(rom_path))[0]
        print(f"→ Processing: {rom_name}")

        box_path = os.path.join(box_dir, f"{rom_name}.png")
        preview_path = os.path.join(preview_dir, f"{rom_name}.png")

        download_libretro_thumbnail(args.libretro_folder, "Named_Boxarts", rom_name, box_path)
        download_libretro_thumbnail(args.libretro_folder, "Named_Snaps", rom_name, preview_path)