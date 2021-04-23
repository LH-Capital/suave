from typing import Dict
from suave.assets import Equity, EquitySchema


class RetrieverMixin(object):

    @classmethod
    def marshal_date(cls, func):
        def _marshal_date(self, *args, **kwargs):
            output = func(self, *args, **kwargs)
            modified_output = {}
            print(output)
            for ticker in output:
                modified_output[ticker] = RetrieverMixin._marshal_date(
                    output[ticker], self.starting_date)
            return modified_output
        return _marshal_date

    @classmethod
    def marshal_equity(cls, func):
        def _marshal_equity(self, *args, **kwargs):
            output = func(self, *args, **kwargs)
            modified_output = {}
            for ticker in output:
                modified_output[ticker] = RetrieverMixin._marshal_equity(
                    output, ticker)
            return modified_output
        return _marshal_equity

    @staticmethod
    def _marshal_date(output: Dict, starting_date: str):
        out_of_range = []
        min_date = min(output.keys())
        for date in output.keys():
            if (starting_date or min_date) > date:
                out_of_range.append(date)
        for date in out_of_range:
            del output[date]
        return output

    @staticmethod
    def _marshal_equity(output: Dict, ticker: str):
        equity_output = []
        schema = EquitySchema()
        for date, v in output.items():
            v = schema.load(v)
            v['date'] = date
            v['ticker'] = ticker
            equity_output.append(Equity.create(**v))
        return sorted(equity_output, key=lambda item: item.date)
