import yfinance as yf
from datetime import datetime, timedelta


def get_stock_price(ticker):
    ticker = ticker + ".NS"
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')
    if data.empty:
        raise Exception("Invalid ticker symbol")
    return {
        "current_price": data['Close'].iloc[-1]
    }

def get_stock_info(ticker):
    current_price = round(get_stock_price(ticker).get("current_price", 0), 2)

    ticker = ticker + ".NS"
    stock = yf.Ticker(ticker)
    info = stock.info
    if not info:
        raise Exception("Invalid ticker symbol")
    return {
        'ticker': ticker,
        'name': info.get('longName', 'N/A'),
        'current_price': current_price if current_price else 'N/A',
        'sector': info.get('sector', 'N/A'),
        'industry': info.get('industry', 'N/A'),
        'market_cap': info.get('marketCap', 'N/A'),
        'previous_close': info.get('previousClose', 'N/A'),
        'open': info.get('open', 'N/A'),
        'volume': info.get('volume', 'N/A'),
        'average_volume': info.get('averageVolume', 'N/A'),
        'pe_ratio': info.get('trailingPE', 'N/A'),
        'dividend_yield': info.get('dividendYield', 'N/A')
    }

def get_stock_history(ticker, period):
    ticker = ticker + ".NS"
    stock = yf.Ticker(ticker)
    
    if period == '1d':
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)
        interval = '1m'
    elif period == '5d':
        end_date = datetime.now()
        start_date = end_date - timedelta(weeks=1)
        interval = '1h'
    elif period == '1mo':
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        interval = '1h'
    elif period == '6mo':
        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)
        interval = '1d'
    elif period == '1y':
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        interval = '1d'
    elif period == '5y':
        end_date = datetime.now()
        start_date = end_date - timedelta(days=5*365)
        interval = '5d'
    elif period == 'max':
        end_date = datetime.now()
        start_date = end_date - timedelta(days=10*365)
        interval = '1mo'
    else:
        raise Exception("Invalid period")

    hist = stock.history(start=start_date, end=end_date, interval=interval)
    
    if hist.empty:
        raise Exception("Invalid ticker symbol or period")
    
    prices = [{'datetime': str(index), 'price': row['Close']} for index, row in hist.iterrows()]
    return {
        'ticker': ticker,
        'period': period,
        'prices': prices
    }
