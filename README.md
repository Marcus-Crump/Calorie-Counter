# Ingredient Calorie Lookup (WIP)

## Overview
Python script that looks up calorie values for a list of ingredients by scraping MyFoodData search results.
Currently returns the calories for **100g** of the first matching result and prints values to stdout.

## Current Functionality
- Build MyFoodData search URLs from ingredient strings
- Fetch and parse HTML using `requests` + `BeautifulSoup`
- Extract kcal value for 100g from the nutrient table
- Process a list of ingredients and print kcal results

## Not Yet Implemented
- Portion/measurement parsing (cups, tbsp, oz, etc.) and calorie scaling
- Reliable item selection (disambiguation instead of “first search result”)
- Robust URL handling (currently brittle)
- Error handling (missing results, network failures, HTML changes)
- GUI (PyQt5 is planned but not used yet)

## Requirements
- Python 3.10+
- requests
- beautifulsoup4

## Run
```bash
pip install requests beautifulsoup4
python main.py
