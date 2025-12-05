# Data Cleaning Project

**Objective:** Clean and prepare a messy dataset for statistical analysis and visualization.  
**Technologies:** Python, pandas, numpy, Jupyter Notebook.

## Structure
- `data/raw.csv` — original/raw dataset (or download link)
- `data/cleaned_data.csv` — cleaned dataset output
- `notebooks/cleaning.ipynb` — step-by-step Jupyter notebook
- `src/cleaning_script.py` — reusable script to automate the cleaning process

## Process (Summary)
1. Initial inspection (info, head, describe)
2. Cleaning column names and removing non-ASCII characters
3. Cleaning numeric values using regex (removing symbols)
4. Dropping columns with >30% missing values
5. Manual corrections where needed
6. Export to CSV ready for analysis

## Results
- Original rows/columns: 20 / 11
- Final rows/columns: 20 / 7
- Columns cleaned: Renamed, non-ASCII characters removed
- Numeric columns converted to float
- Columns with >30% missing values removed

## Key Learnings / Skills Demonstrated
- Data inspection and understanding of dataset quality
- Column name standardization and handling special characters
- Regex for numeric data cleaning
- Handling missing values effectively
- Exporting clean data for analysis
- Writing reusable Python scripts for data cleaning

## Potential Applications
- Preparing raw financial or sales data for statistical analysis
- Standardizing datasets for dashboards in Python or Power BI
- Foundational step for predictive analytics or reporting pipelines


## Original structure (selected columns)

| Column                        | Non-Null Count | Dtype  |
|-------------------------------|----------------|-------|
| Rank                          | 20             | int64 |
| Peak                          | 9              | object|
| All Time Peak                 | 6              | object|
| Actual gross                  | 20             | object|
| Adjusted gross (in 2022 $)   | 20             | object|
| Artist                        | 20             | object|
| Tour title                    | 20             | object|
| Year(s)                       | 20             | object|
| Shows                         | 20             | int64 |
| Average gross                 | 20             | object|
| Ref.                          | 20             | object|

## Final structure

| Column         | Non-Null Count | Dtype   |
|----------------|----------------|--------|
| Actual gross   | 20             | float64|
| Adjusted gross | 20             | float64|
| Artist         | 20             | object |
| Tour title     | 20             | object |
| Year(s)        | 20             | object |
| Shows          | 20             | int64  |
| Average gross  | 20             | float64|

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/Oscar-Jiram/data-cleaning-project.git
cd data-cleaning-project
pip install -r requirements.txt
python src/cleaning_script.py data/raw.csv data/cleaned_data.csv
pip install jupyter
jupyter notebook notebooks/cleaning.ipynb