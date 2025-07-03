<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<h1 align="center">MUOS Scraper - libretro-thumbnails Downloader</h1>

  <p align="center">
    <a href="https://github.com/mattsteen14/muos_scraper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
     <a href="https://github.com/mattsteen14/muos_scraper">View Demo</a>
    ·
    <a href="https://github.com/mattsteen14/muos_scraper/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/mattsteen14/muos_scraper/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple Python CLI tool to automatically download box art and preview images for your video game ROMs from the [libretro-thumbnails GitHub repository](https://github.com/libretro-thumbnails/libretro-thumbnails).

The tool matches your ROM filenames exactly — including metadata like years and publishers — and fetches the corresponding images from a pinned commit on GitHub. It automatically resizes box art images to a width of 300 pixels to fit MUOS catalogue standards, populating the box and preview subfolders within the MUOS /info/catalogue folder structure.

This tool is intended as an alternative to [ScreenScraper](https://www.screenscraper.fr)/[Skraper](https://www.skraper.net) & [Scrappy](https://github.com/gabrielfvale/scrappy/releases) for Anbernic RG28XX devices that are not Wi-Fi enabled, and for users who want to use Skraper but can’t install it due to Mac compatibility issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [Python 3](https://www.python.org/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Pillow (PIL)](https://python-pillow.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

These are instructions for setting up the project locally. To get a local copy up and running, follow these simple steps.

### Prerequisites

- Internet connection to download images from GitHub
- Your ROMs organized in a folder (with filenames matching libretro-thumbnails naming conventions)
- Knowledge of your system's MUOS system name and corresponding libretro-thumbnails folder name

Ensure you have the following software installed before proceeding:

- **Python 3.6 or higher**: Check with:

  ```sh
  python3 --version
  ```

- **The Pillow image library**

    Install Pillow using pip:

  ```sh
  pip install pillow
  ```

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/mattsteen14/muos_scraper.git
   ```

2. In the terminal, navigate into the project directory:

   ```sh
   cd muos_scraper
   ```

3. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the script with your ROMs folder, libretro folder name, and output folder:

   ```sh
   python muos_scraper.py --roms-folder '/path/ROMS/N64'
                       --libretro-folder Nintendo_-_Nintendo_64
                       --output-folder '/MUOS/info/catalogue/Nintendo\ N64'
   ```
    -	--roms-folder — Required. Path to the roms folder you'd like images for. In quotes.
    -	--libretro-folder — Required. How the system is called in the github.com/libretro-thumbnails/ URL. See above example. For this you will have to find the system on the [libretro-thumbnails GitHub repository](https://github.com/libretro-thumbnails/libretro-thumbnails). I will work on how this can be set dynamically. Feel free to send a pull request if you know how it can be done.
    -	--output-folder — Required. Path to the /MUOS/info/catalogue/{system name} folder with the box & preview sub folders you would like to populate. In quotes.

    *Hint:* 
    
    *Instead of typing the full paths, just drag & drop the folders into the terminal.*

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Plan project.
- [x] Write code.
- [x] Test on roms folder.
- [x] Version control. Set up on GitHub.
- [x] Push to GitHub.
- [ ] Testing and dubugging.
- [ ] Additional features.
- [ ] Simplify inputs.
- [ ] Create simple GUI interface.

See the [open issues](https://github.com/mattsteen14/muos_scraper/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project.

2. Create your Feature Branch:

   ```sh
   git checkout -b feature/AmazingFeature
   ```

3. Commit your Changes:

   ```sh
   git commit -m "Add some AmazingFeature"
   ```

4. Push to the Branch:

   ```sh
   git push origin feature/AmazingFeature
   ```

5. Open a Pull Request.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Matt Steen-Brookes - [@mattsteen14](https://twitter.com/mattsteen14) - <mattsteen14@me.com>

Project Link: [https://github.com/mattsteen14/muos_scraper](https://github.com/mattsteen14/muos_scraper)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [Mo Ashqar](https://github.com/ashqar) for introducing me to Codecademy in the first place.
- [Othneil Drew](https://github.com/othneildrew) for the README template.
- [Choose an Open Source License](https://choosealicense.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mattsteen14/muos_scraper.svg?style=for-the-badge
[contributors-url]: https://github.com/mattsteen14/muos_scraper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mattsteen14/muos_scraper.svg?style=for-the-badge
[forks-url]: https://github.com/mattsteen14/muos_scraper/network/members
[stars-shield]: https://img.shields.io/github/stars/mattsteen14/muos_scraper.svg?style=for-the-badge
[stars-url]: https://github.com/mattsteen14/muos_scraper/stargazers
[issues-shield]: https://img.shields.io/github/issues/mattsteen14/muos_scraper.svg?style=for-the-badge
[issues-url]: https://github.com/mattsteen14/muos_scraper/issues
[license-shield]: https://img.shields.io/github/license/mattsteen14/muos_scraper.svg?style=for-the-badge
[license-url]: https://github.com/mattsteen14/muos_scraper/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mattsteen14
