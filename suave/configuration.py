from dataclasses import dataclass
from typing import List


@dataclass
class Configuration(object):

    alpha_api_key: str
    starting_date: str
    starting_balance: float
