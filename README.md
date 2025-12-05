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


## Original structure
#   Column                            Non-Null Count  Dtype 
---  ------                            --------------  ----- 
 0   Rank                              20 non-null     int64 
 1   Peak                              9 non-null      object
 2   All Time Peak                     6 non-null      object
 3   Actual�gross                      20 non-null     object
 4   Adjusted�gross (in 2022 dollars)  20 non-null     object
 5   Artist                            20 non-null     object
 6   Tour title                        20 non-null     object
 7   Year(s)                           20 non-null     object
 8   Shows                             20 non-null     int64 
 9   Average gross                     20 non-null     object
 10  Ref.                              20 non-null     object

## Final structure
(#   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Actual gross    20 non-null     float64
 1   Adjusted gross  20 non-null     float64
 2   Artist          20 non-null     object 
 3   Tour title      20 non-null     object 
 4   Year(s)         20 non-null     object 
 5   Shows           20 non-null     int64  
 6   Average gross   20 non-null     float64)

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/Oscar-Jiram/data-cleaning-project.git
cd data-cleaning-project
pip install -r requirements.txt
python src/cleaning_script.py data/raw.csv data/cleaned_data.csv
pip install jupyter
jupyter notebook notebooks/cleaning.ipynb