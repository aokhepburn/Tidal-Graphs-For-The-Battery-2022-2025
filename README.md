<p align="center">
    <a href=""><img src="https://img.shields.io/pypi/l/ansicolortags.svg" /></a>
    <a href=""><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" /></a>
    <a href=""><img src="https://github.com/aokhepburn/Tidal-Graphs-For-The-Battery-2022-2025" /></a>
    <br>
    <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>

</p>

<h1 align="center"><b>Graphing The Tide As It Is Observed at the Battery (NY, NY) 2022-2025</b></h1>
<h4 align="center">A CLI project to look at both past tidal data and future tidal data for tracking daily tidal changes in New York Harbor.

Currently only using the observations at The Battery but will add functionality for other parts of the harbor.</h4>

<p align="center">
    <img src="" alt="Project Banner" width=60% height=60%/>
</p>

## Table of Contents

- [Introduction](#introduction)
- [Technical Requirements](#technical-requirements)
- [Project Structure](#project-structure)
- [Key Functionalities](#key-functionalities)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The project is supposed to enable an easier, more visual, way for a user to interact with daily tide data as provided by NOAA.

## Technical Requirements

To enable the commands you will need:

- Python 3.8 or later
- NumPy
- SciPy
- MatPlotLib
- Pandas

## Project Directory Hierarchy

Upon successful setup (see **Getting Started**), you should see the following project directory hierarchy.

```
tidal-and-pilot-chart-project-python/
├── data/
│ └── data/NOAA-tides-date-and-time-same.csv
│ └── data/NOAA-tide-predictions-battery-yr2022-2025.csv
├── main.py
├── Pipfile
├── PlotDataMatLab.py
├── README.md
├── TestingFile.py
├── TidalPlottingDashApp.py
└── TidalPlottingInputDateRetrieveData.py

```

- `data/`: Directory containing datasets for tidal information obtained from NOAA.
- `main.py`: Main application file which takes user input and allows application to be run.
- `Pipfile` and `Pipfile.lock`: Files specifying project dependencies when using `pipenv`.
- `README.md`: Project documentation providing an overview, setup instructions, and other details.

## Key Functionalities

The NFL Player Statistics Dashboard offers the following functionalities:

-

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/aokhepburn/Tidal-Graphs-For-The-Battery-2022-2025
```

2. Navigate to the project directory:

```bash
cd Tidal-Graphs-For-The-Battery-2022-2025
```

3. Install the required dependencies using pipenv:

```bash
pipenv install
```

4. Run the application:

```bash
pipenv python main.py
```

5. Within the CLI there are three prompts to allow a range of three dates as data.

## Usage

1. Run the file.
2. Enter the prompted dates
3. Save the chart from matplotlib if so desired.

## Dependencies

The tidal charts rely on the following libraries:

- MatPlotLib
- NumPy
- SciPy
