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
This phase focuses on understanding the structure and behavior of financial news data.  

#### Descriptive Statistics
- Distribution of headline lengths
- Article frequency per publisher
- Identification of most active news sources

#### Time Analysis
- Publication trends over time
- Detection of spikes in news volume
- Time-of-day analysis of news releases

#### Text Analysis (Topic Exploration)
- Extraction of frequent keywords and phrases
- Identification of recurring financial themes

#### Publisher Analysis
- Ranking publishers by article count
- Detecting dominant domains in publisher emails 

### Task 2: Stock Market Analysis with Technical Indicators

This phase focuses on analyzing historical stock price data using financial indicators.

#### Data Preparation
- Loaded historical stock datasets (AAPL, AMZN, GOOG, META, NVDA)
- Standardized structure across all assets
- Handled missing values and ensured proper time indexing

#### Moving Averages (SMA & EMA)
- SMA (20-day) for trend smoothing
- EMA (20-day) for faster trend response
- Used to identify trend direction and crossovers

#### Relative Strength Index (RSI)
- Measures momentum strength
- Identifies overbought (>70) and oversold (<30) conditions

#### MACD (Moving Average Convergence Divergence)
- Captures momentum shifts
- Used to identify trend reversals through MACD/signal crossovers

#### Daily Returns
- Percentage change in closing price
- Used to evaluate short-term performance

#### Volatility (20-day rolling std)
- Measures risk and price instability
- Highlights periods of high market uncertainty


## Technologies Used
- Python – core programming language
- Pandas, NumPy – data manipulation
- Matplotlib – visualization
- ta – technical indicators
- NLTK / TextBlob – NLP sentiment tools (for later tasks)
- Git & GitHub – version control
- GitHub Actions – CI pipeline