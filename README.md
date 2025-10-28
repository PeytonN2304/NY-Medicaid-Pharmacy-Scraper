# NY Medicaid Pharmacy Scraper
**All data extracted from https://member.emedny.org/pharmacy/search-locations**

Python web scraper to extract pharmacy providers in New York State that accept Medicaid.

---

## Table of contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)

---

## Overview

This repository contains a Python-based web scraper designed to collect contact and location information for pharmacies in New York State that accept Medicaid. The project focuses on programmatic extraction, cleaning, and export of provider data suitable for analysis or import into downstream systems.

---

## Features

- Targeted scraping for New York State pharmacy provider lists
- Data normalization and basic validation (addresses, phone numbers)
- Export to CSV 
- Error handling 

---

## Requirements

- Python 3.9+ (3.10+ recommended)
- pip

Common Python libraries:
- selenium (Web driver)

---

## Installation

1. Clone the repository:

   git clone https://github.com/PeytonN2304/NY-Medicaid-Pharmacy-Scraper.git

    

---

## Usage
1. cd NY-Medicaid-Pharmacy-Scraper
2. Change Url in configuration section of the code 
3. Quick run:
    python main.py


---

## Output

Default outputs:
- CSV: rows of provider data (suitable for spreadsheets or ingestion)

Typical output fields:
- county
- name
- category
- address
- city,state
- phone


---
## Acknowledgements

- Built for collecting structured data on pharmacies in New York State that accept Medicaid.
- Thank you to data providers and maintainers of public provider directories.


