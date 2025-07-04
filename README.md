# 🎮 MUOS Scraper

[![Contributors](https://img.shields.io/github/contributors/mattsteen14/muos_scraper.svg?style=for-the-badge)](https://github.com/mattsteen14/muos_scraper/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/mattsteen14/muos_scraper.svg?style=for-the-badge)](https://github.com/mattsteen14/muos_scraper/network/members)
[![Stargazers](https://img.shields.io/github/stars/mattsteen14/muos_scraper.svg?style=for-the-badge)](https://github.com/mattsteen14/muos_scraper/stargazers)
[![Issues](https://img.shields.io/github/issues/mattsteen14/muos_scraper.svg?style=for-the-badge)](https://github.com/mattsteen14/muos_scraper/issues)
[![MIT License](https://img.shields.io/github/license/mattsteen14/muos_scraper.svg?style=for-the-badge)](https://github.com/mattsteen14/muos_scraper/blob/main/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/mattsteen14)

---

[**Explore the docs »**](https://github.com/mattsteen14/muos_scraper)
[View Demo](https://github.com/mattsteen14/muos_scraper) ·
[Report Bug](https://github.com/mattsteen14/muos_scraper/issues/new?labels=bug&template=bug-report---.md) ·
[Request Feature](https://github.com/mattsteen14/muos_scraper/issues/new?labels=enhancement&template=feature-request---.md)

<details>
  <summary><strong>📚 Table of Contents</strong></summary>

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

</details>

---

## 🚀 About The Project

This is a simple Python CLI tool to automatically download box art and preview images for your video game ROMs from the [libretro-thumbnails GitHub repository](https://github.com/libretro-thumbnails/libretro-thumbnails).

The tool matches your ROM filenames exactly — including metadata like years and publishers — and fetches the corresponding images from a pinned commit on GitHub. It automatically resizes box art images to a width of 300 pixels to fit MUOS catalogue standards, populating the box and preview subfolders within the MUOS /info/catalogue folder structure.

This tool is intended as an alternative to [ScreenScraper](https://www.screenscraper.fr)/[Skraper](https://www.skraper.net) & [Scrappy](https://github.com/gabrielfvale/scrappy/releases) for Anbernic RG28XX devices that are not Wi-Fi enabled, and for users who want to use Skraper but can’t install it due to Mac compatibility issues.

### 📦 Features

- 🧠 Matches ROM filenames exactly — including metadata like year and publisher
- 🔄 Automatically resizes box art to 300px wide for MUOS
- 📁 Outputs to MUOS `/info/catalogue/{system}/box` and `/preview` subfolders
- ⚡ Uses dynamic commit fetching from GitHub (no hardcoded versions)
- ✅ Great for RG28XX and other MUOS-based devices

⬆️ [Back to top](#retroarch-scraper)

---

### 🛠 Built With

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-%3E=2.25.1-green)](https://requests.readthedocs.io/en/latest/)
[![Pillow](https://img.shields.io/badge/Pillow-%3E=8.0.0-yellowgreen)](https://python-pillow.org/)

⬆️ [Back to top](#retroarch-scraper)

---

## 🧰 Getting Started

These instructions will help you set up the project locally.

### ✅ Prerequisites

- An internet connection (to download artwork from GitHub)
- ROMs organized in folders (with filenames that match libretro-thumbnails)
- Knowledge of your system’s MUOS name and libretro-thumbnails folder name

Make sure Python and Pillow are installed:

```bash
python3 --version
pip install pillow
```

---

### 🖥 Installation

1. Clone the repository:

```bash
git clone https://github.com/mattsteen14/muos_scraper.git
```

2. Navigate into the project folder:

```bash
cd muos_scraper
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script with your ROMs folder, libretro folder name, and output folder:

```sh
python muos_scraper.py --roms-folder '/path/ROMS/N64'
--libretro-folder Nintendo_-_Nintendo_64
--output-folder '/MUOS/info/catalogue/Nintendo\ N64'
```

- --roms-folder — Required. Path to the roms folder you'd like images for. In quotes.
- --libretro-folder — Required. How the system is called in the github.com/libretro-thumbnails/ URL. See above example. For this you will have to find the system on the [libretro-thumbnails GitHub repository](https://github.com/libretro-thumbnails/libretro-thumbnails). I will work on how this can be set dynamically. Feel free to send a pull request if you know how it can be done.
- --output-folder — Required. Path to the /MUOS/info/catalogue/{system name} folder with the box & preview sub folders you would like to populate. In quotes.
- *Hint: Instead of typing the full paths, just drag & drop the folders into the terminal.*

⬆️ [Back to top](#retroarch-scraper)

---

## 📅 Roadmap

- [x] Plan project.
- [x] Write code.
- [x] Test on roms folder.
- [x] Version control. Set up on GitHub.
- [x] Push to GitHub.
- [ ] Testing and debugging.
- [ ] Additional features.
- [ ] Simplify inputs.
- [ ] Create simple GUI interface.

👉 See [Issues](https://github.com/mattsteen14/muos_scraper/issues) for open features and bugs.

⬆️ [Back to top](#retroarch-scraper)

---

## 🤝 Contributing

Contributions are what make open source amazing. If you'd like to help:

1. Fork the repository

2. Create your branch:  

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes:  

```bash
git commit -m "Add some feature"
```

4. Push to GitHub:  

```bash
git push origin feature/YourFeature
```

5. Open a pull request

Or open an issue with the **enhancement** label.

⬆️ [Back to top](#retroarch-scraper)

---

## 📝 License

Distributed under the MIT License.  
See [`LICENSE`](https://github.com/mattsteen14/muos_scraper/blob/main/LICENSE) for more information.

⬆️ [Back to top](#retroarch-scraper)

---

## 📬 Contact

Matt Steen-Brookes  
📧 [mattsteen14@me.com](mailto:mattsteen14@me.com)  
🐦 [@mattsteen14](https://twitter.com/mattsteen14)  
🔗 [GitHub Repo](https://github.com/mattsteen14/muos_scraper)

⬆️ [Back to top](#retroarch-scraper)

---

## 🙏 Acknowledgments

- [Mo Ashqar](https://github.com/ashqar) for introducing me to Codecademy
- [Othneil Drew](https://github.com/othneildrew) for the README template
- [Choose an Open Source License](https://choosealicense.com)

⬆️ [Back to top](#retroarch-scraper)