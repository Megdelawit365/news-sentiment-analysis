# Predicting Price Moves with News Sentiment  

This project investigates the relationship between financial news headlines and stock price movements using a combination of Natural Language Processing (NLP) and quantitative financial analysis. The goal is to determine whether sentiment extracted from news data can help explain or predict market behavior when combined with technical indicators such as SMA, EMA, RSI, MACD, returns and volatility.  

---

## Project Structure  

```bash
├── .vscode/                  
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml     
├── .gitignore
├── requirements.txt          
├── README.md                 
│
├── data/
│   └── raw/                  
│
├── notebooks/                
│   ├── eda.ipynb
│   ├── stock_analysis.ipynb
│
├── src/                      
│   └── __init__.py
│
├── tests/                    
│   └── __init__.py
│
└── scripts/                  
    └── __init__.py
```

---

## Setup Instructions  

### 1. Clone the repository  
```bash
git clone https://github.com/Megdelawit365/news-sentiment-analysis
```

### 2. Create a virtual environment  
```bash
python -m venv venv
```

### 2. Activate virtual environment  
Windows:  
```bash
venv\Scripts\activate
```

MAC/Linux:  
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Project Overview  
### Task 1: Exploratory Data Analysis (EDA) on Financial News
- Performed descriptive statistics on headlines to find distribution of headline lengths, article frequency per publisher and to identify most active news sources  
- Performend time series analysis to detect spikes in news volumes
- Extracted frequent keywords and phrases from headlines
- Ranked publishers by article count and detected dominant domains in publisher emails

### Task 2: Stock Market Analysis with Technical Indicators
- Handled missing values and ensured proper time indexing
- Computed technical indicators (SMA, EMA, RSI, MACD) using TA-Lib
- Additionally computed Daily returns and volatility

###  Task 3: Correlation between news sentiment and stock movement  
- Used NLTK VADER to apply sentiment analysis on news headlines  
- Calulated Daily Stock Returns
- Computed the average daily sentiment score for each stock
- Calculated the Pearson correlation coefficient between average daily sentiment scores and daily stock returns 


## Technologies Used
- Python – core programming language
- Pandas, NumPy – data manipulation
- Matplotlib – visualization
- ta – technical indicators
- NLTK / TextBlob – NLP sentiment tools (for later tasks)
- Git & GitHub – version control
- GitHub Actions – CI pipeline