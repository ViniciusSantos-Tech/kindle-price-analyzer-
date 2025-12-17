<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFFF,100:000000&height=200&section=header&text=Amazon%20Price%20Monitoring&fontSize=45&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Selenium-4.0+-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/Web%20Scraping-FF6B35?style=for-the-badge&logo=web-scraper&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

<h2 align="center">📊 Intelligent Amazon Price Monitoring</h2>
A learning project in web automation using Selenium


# 📝 Project Description

## This project is a web application built with **Streamlit** that uses **Selenium** to perform data scraping (web scraping) on Amazon Brazil. The goal is to search for a product specified by the user and extract prices from the first results, providing a quick statistical analysis and the option to download the data.

The tool is useful for quickly monitoring price variations and identifying the best deals for a specific item on Amazon.

## 🎯 Why Did I Build This Project?
As a developer in learning, I wanted to:
- Apply Selenium in a real-world project
- Understand web scraping challenges
- Create something useful that could evolve into a price monitoring tool


# Technologies

## ✅ Automation & Web Scraping
- Selenium WebDriver 4.15+: Advanced automation of the Chrome browser
- Advanced CSS Selectors: Robust location of dynamic elements
- XPath Expressions: Alternative selection for complex elements
- WebDriverWait + Expected Conditions: Smart waiting for dynamic loading
- ActionChains: Simulation of realistic user interactions


## ✅ Web Development & Interface
- Streamlit 1.28+: Framework for building web applications in Python
- Session State: State management between user interactions
- Streamlit Components: Buttons, inputs, metrics, and interactive containers
- Custom CSS: Interface styling via HTML markdown


## ✅ Data Processing & Analysis
- Pandas 2.1.4+: Structured data manipulation and analysis
- DataFrames: Tabular structuring of collected products
- Vectorized Operations: Efficient statistical calculations
- Data Cleaning: Cleaning and transforming strings into numeric values


### 1. Home Screen
Here, the user enters the search term (e.g., "Toy") and starts the search.

![Initial Interface Screenshot](assets/foto1.png)

### 2. Results and Analysis
Display of the 5 products found, the statistical summary, and the CSV download button.

![Results and Metrics Screenshot](assets/foto2.png)


## ⚙️ Technologies Used
* **Python 3.x**
* **Streamlit**: Framework for rapid web interface development
* **Selenium**: Used for browser automation (Chrome) and data collection from Amazon pages
* **datetime** and **time**: For time handling and dynamic file name generation


## ⚠️ If the code stops working, it is likely because Amazon has changed its CSS classes (a-price-whole, a-size-base-plus.a-color-base.a-text-normal). ⚠️


### 🧑‍💻 Author  
Developed by Vinicius Santos – Tech
