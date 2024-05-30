from freqtrade.strategy import IStrategy
from pandas import DataFrame
from freqtrade.persistence import Trade
import pandas as pd


class MartingaleBullRunStrategy(IStrategy):
    INTERFACE_VERSION = 3

    # Leverage settings
    LEVERAGE = 5

    # Optimal stoploss to satisfy configuration schema
    stoploss = -0.99  # Effectively disables stop loss by setting it to -99%

    # Minimal ROI designed for the strategy.
    minimal_roi = {
        "0": 0.2  # Exit after 20% profit
    }

    # Optimal timeframe for the strategy
    timeframe = '1d'

    # Define constants
    DROP_FROM_ATH = 10  # Percentage drop from ATH to trigger entry

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """ Adds ATH indicator to the given DataFrame """

        # Calculate the maximum close price over the past 3 years (3 * 365 * 24)
        dataframe['max_close'] = dataframe['close'].rolling(window=3 * 365 * 24, min_periods=1).max()

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """ Define the entry signal """

        # Calculate the percentage drop from the highest close price in the dataframe
        dataframe['percent_drop'] = (dataframe['max_close'] - dataframe['close']) / dataframe['max_close'] * 100

        # Entry signal when market drops by DROP_FROM_ATH percent from ATH
        dataframe.loc[
            (dataframe['percent_drop'] >= self.DROP_FROM_ATH),
            'enter_long'
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """ Define the exit signal """

        # Exit signal when market increases by 20% from the entry point
        dataframe.loc[
            (dataframe['close'] > dataframe['close'].shift(1) * 1.2),
            'exit_long'
        ] = 1

        return dataframe

    def should_enter(self, pair: str, dataframe: DataFrame) -> bool:
        """
        Override this method to prevent multiple entries
        """
        # Check if there are any open trades for the given pair
        open_trades = self.get_open_trades()
        if open_trades.empty:
            return True

        return False
