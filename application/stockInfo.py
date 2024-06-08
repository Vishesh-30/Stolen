import yfinance as yf


def get_stock_info(ticker):
    ticker = ticker + ".NS"
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')
    if data.empty:
        raise Exception("Invalid ticker symbol")
    return {
        "current_price": data['Close'].iloc[-1]
    }