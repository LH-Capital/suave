from alpha_vantage.timeseries import TimeSeries
from typing import List
from suave.retrievers.mixins import RetrieverMixin as mixin


class TimeSeriesRetriever(mixin):

    def __init__(self, alpha_api_key: str,
                 tickers: List[str],
                 starting_date: str):
        self.av = TimeSeries(key=alpha_api_key)
        self.tickers = [ticker.upper() for ticker in tickers]
        self.starting_date = starting_date

    @mixin.marshal_date
    @mixin.marshal_equity
    def get_all_intraday(self):
        data = {}
        for ticker in self.tickers:
            output, meta = self.av.get_intraday(ticker, outputsize='all')
            data[ticker] = output
        return data

    @mixin.marshal_date
    @mixin.marshal_equity
    def get_all_daily(self):
        data = {}
        for ticker in self.tickers:
            output, meta = self.av.get_daily(ticker, outputsize='all')
            data[ticker] = output
        return data

    @mixin.marshal_equity
    def get_current_quote(self):
        data = {}
        for ticker in self.tickers:
            output, meta = self.av.get_quote_endpoint(ticker)
            data[ticker] = output
        return data
