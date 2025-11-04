# Smartpix Smartphone Data Analysis & Modelling

This project focuses on **data-driven insights from smartphone specifications** scraped from the Smartpix website.
It covers **data gathering, cleaning, exploratory data analysis (EDA), feature engineering, and predictive modelling** to understand patterns such as price relationships, feature importance, and brand trends.

## Project Overview

The dataset was collected using a custom Python scraper (`smartpix_web_scrap.py`) and analyzed through a Jupyter Notebook (`smartpix_web_scrap copy.ipynb`).

The goal was to:
- Clean and preprocess real-world web-scraped smartphone data.
- Perform in-depth **EDA** to uncover brand and feature trends.
- Build a **predictive model** (e.g., price prediction or feature-based clustering).
- Visualize findings and present key insights.


## Project Workflow

1. **Data Collection**  
   - Data scraped from Smartpix using `smartpix.py`.  
   - The script uses Selenium/BeautifulSoup to extract smartphone specs and prices.  

2. **Data Cleaning**  
   - Removed duplicates, missing values, and inconsistent formats.  
   - Parsed numeric fields (price, storage, battery) into usable types.  

3. **EDA (Exploratory Data Analysis)**  
   - Distribution of phone prices and brands.  
   - Feature relationships (camera, RAM, storage, etc.).  
   - Correlation heatmaps and outlier detection.  

4. **Feature Engineering**  
   - Created derived features such as price-per-spec metrics.  
   - Encoded categorical fields (brand, OS).  
   - Scaled numerical attributes.  

5. **Modelling**  
   - Used different ML models to predict the smartphone price.  
   - Compared baseline and advanced models.
   - also use the stacking regressor, which gives a promising result for mobile price prediction

6. **Visualization & Reporting**  
   - Created plots using Matplotlib/Pandas.  
   - Summarized insights. 
