# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy
from typing import Dict, List
from functools import reduce
from pandas import DataFrame
# --------------------------------

import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import numpy # noqa
from typing import Any, Dict
from freqtrade.strategy import (BooleanParameter, CategoricalParameter, DecimalParameter,
                                IStrategy, IntParameter)

# Candle names:
candleNames = [
    "CDL2CROWS",
    "CDL3BLACKCROWS",
    "CDL3INSIDE",
    "CDL3LINESTRIKE",
    "CDL3OUTSIDE",
    "CDL3STARSINSOUTH",
    "CDL3WHITESOLDIERS",
    "CDLABANDONEDBABY",
    "CDLADVANCEBLOCK",
    "CDLBELTHOLD",
    "CDLBREAKAWAY",
    "CDLCLOSINGMARUBOZU",
    "CDLCONCEALBABYSWALL",
    "CDLCOUNTERATTACK",
    "CDLDARKCLOUDCOVER",
    "CDLDOJI",
    "CDLDOJISTAR",
    "CDLDRAGONFLYDOJI",
    "CDLENGULFING",
    "CDLEVENINGDOJISTAR",
    "CDLEVENINGSTAR",
    "CDLGAPSIDESIDEWHITE",
    "CDLGRAVESTONEDOJI",
    "CDLHAMMER",
    "CDLHANGINGMAN",
    "CDLHARAMI",
    "CDLHARAMICROSS",
    "CDLHIGHWAVE",
    "CDLHIKKAKE",
    "CDLHIKKAKEMOD",
    "CDLHOMINGPIGEON",
    "CDLIDENTICAL3CROWS",
    "CDLINNECK",
    "CDLINVERTEDHAMMER",
    "CDLKICKING",
    "CDLKICKINGBYLENGTH",
    "CDLLADDERBOTTOM",
    "CDLLONGLEGGEDDOJI",
    "CDLLONGLINE",
    "CDLMARUBOZU",
    "CDLMATCHINGLOW",
    "CDLMATHOLD",
    "CDLMORNINGDOJISTAR",
    "CDLMORNINGSTAR",
    "CDLONNECK",
    "CDLPIERCING",
    "CDLRICKSHAWMAN",
    "CDLRISEFALL3METHODS",
    "CDLSEPARATINGLINES",
    "CDLSHOOTINGSTAR",
    "CDLSHORTLINE",
    "CDLSPINNINGTOP",
    "CDLSTALLEDPATTERN",
    "CDLSTICKSANDWICH",
    "CDLTAKURI",
    "CDLTASUKIGAP",
    "CDLTHRUSTING",
    "CDLTRISTAR",
    "CDLUNIQUE3RIVER",
    "CDLUPSIDEGAP2CROWS",
    "CDLXSIDEGAP3METHODS"
]

class Strategy002V3(IStrategy):
    """
    Strategy 002
    author@: Gerald Lonlas
    github@: https://github.com/freqtrade/freqtrade-strategies
    How to use it?
    > python3 ./freqtrade/main.py -s Strategy002
    """

    CDL2CROWS = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3BLACKCROWS = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3INSIDE = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3LINESTRIKE = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3OUTSIDE = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3STARSINSOUTH = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3WHITESOLDIERS = CategoricalParameter([0, 100], default=100, space="buy")
    CDLABANDONEDBABY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLADVANCEBLOCK = CategoricalParameter([0, 100], default=100, space="buy")
    CDLBELTHOLD = CategoricalParameter([0, 100], default=100, space="buy")
    CDLBREAKAWAY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLCLOSINGMARUBOZU = CategoricalParameter([0, 100], default=100, space="buy")
    CDLCONCEALBABYSWALL = CategoricalParameter([0, 100], default=100, space="buy")
    CDLCOUNTERATTACK = CategoricalParameter([0, 100], default=100, space="buy")
    CDLDARKCLOUDCOVER = CategoricalParameter([0, 100], default=100, space="buy")
    CDLDOJI = CategoricalParameter([0, 100], default=100, space="buy")
    CDLDOJISTAR = CategoricalParameter([0, 100], default=100, space="buy")
    CDLDRAGONFLYDOJI = CategoricalParameter([0, 100], default=100, space="buy")
    CDLENGULFING = CategoricalParameter([0, 100], default=100, space="buy")
    CDLEVENINGDOJISTAR = CategoricalParameter([0, 100], default=100, space="buy")
    CDLEVENINGSTAR = CategoricalParameter([0, 100], default=100, space="buy")
    CDLGAPSIDESIDEWHITE = CategoricalParameter([0, 100], default=100, space="buy")
    CDLGRAVESTONEDOJI = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHAMMER = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHANGINGMAN = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHARAMI = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHARAMICROSS = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHIGHWAVE = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHIKKAKE = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHIKKAKEMOD = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHOMINGPIGEON = CategoricalParameter([0, 100], default=100, space="buy")
    CDLIDENTICAL3CROWS = CategoricalParameter([0, 100], default=100, space="buy")
    CDLINNECK = CategoricalParameter([0, 100], default=100, space="buy")
    CDLINVERTEDHAMMER = CategoricalParameter([0, 100], default=100, space="buy")
    CDLKICKING = CategoricalParameter([0, 100], default=100, space="buy")
    CDLKICKINGBYLENGTH = CategoricalParameter([0, 100], default=100, space="buy")
    CDLLADDERBOTTOM = CategoricalParameter([0, 100], default=100, space="buy")
    CDLLONGLEGGEDDOJI = CategoricalParameter([0, 100], default=100, space="buy")
    CDLLONGLINE = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMARUBOZU = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMATCHINGLOW = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMATHOLD = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMORNINGDOJISTAR = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMORNINGSTAR = CategoricalParameter([0, 100], default=100, space="buy")
    CDLONNECK = CategoricalParameter([0, 100], default=100, space="buy")
    CDLPIERCING = CategoricalParameter([0, 100], default=100, space="buy")
    CDLRICKSHAWMAN = CategoricalParameter([0, 100], default=100, space="buy")
    CDLRISEFALL3METHODS = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSEPARATINGLINES = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSHOOTINGSTAR = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSHORTLINE = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSPINNINGTOP = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSTALLEDPATTERN = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSTICKSANDWICH = CategoricalParameter([0, 100], default=100, space="buy")
    CDLTAKURI = CategoricalParameter([0, 100], default=100, space="buy")
    CDLTASUKIGAP = CategoricalParameter([0, 100], default=100, space="buy")
    CDLTHRUSTING = CategoricalParameter([0, 100], default=100, space="buy")
    CDLTRISTAR = CategoricalParameter([0, 100], default=100, space="buy")
    CDLUNIQUE3RIVER = CategoricalParameter([0, 100], default=100, space="buy")
    CDLUPSIDEGAP2CROWS = CategoricalParameter([0, 100], default=100, space="buy")
    CDLXSIDEGAP3METHODS = CategoricalParameter([0, 100], default=100, space="buy")

    INTERFACE_VERSION: int = 3
    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi"
    minimal_roi = {
        "60":  0.01,
        "30":  0.03,
        "20":  0.04,
        "0":  0.05
    }

    # Optimal stoploss designed for the strategy
    # This attribute will be overridden if the config file contains "stoploss"
    stoploss = -0.10

    # Optimal timeframe for the strategy
    timeframe = '5m'

    # trailing stoploss
    trailing_stop = False
    trailing_stop_positive = 0.01
    trailing_stop_positive_offset = 0.02

    # run "populate_indicators" only for new candle
    process_only_new_candles = False

    # Experimental settings (configuration will overide these if set)
    use_exit_signal = True
    exit_profit_only = True
    ignore_roi_if_entry_signal = False

    buy_rsi = IntParameter(low=1, high=100, default=30, space='buy', optimize=True, load=True)

    # Optional order type mapping
    order_types = {
        'entry': 'limit',
        'exit': 'limit',
        'stoploss': 'market',
        'stoploss_on_exchange': False
    }

    def informative_pairs(self):
        """
        Define additional, informative pair/interval combinations to be cached from the exchange.
        These pair/interval combinations are non-tradeable, unless they are part
        of the whitelist as well.
        For more information, please consult the documentation
        :return: List of tuples in the format (pair, interval)
            Sample: return [("ETH/USDT", "5m"),
                            ("BTC/USDT", "15m"),
                            ]
        """
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Adds several different TA indicators to the given DataFrame
        Performance Note: For the best performance be frugal on the number of indicators
        you are using. Let uncomment only the indicator you are using in your strategies
        or your hyperopt configuration, otherwise you will waste your memory and CPU usage.
        """

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe)

        # All candles: values [0, 100]
#         for candleName in candleNames:
#              dataframe[candleName] = ta[candleName](dataframe)

        dataframe['CDL2CROWS'] = ta.CDL2CROWS(dataframe)
        dataframe['CDL3BLACKCROWS'] = ta.CDL3BLACKCROWS(dataframe)
        dataframe['CDL3INSIDE'] = ta.CDL3INSIDE(dataframe)
        dataframe['CDL3LINESTRIKE'] = ta.CDL3LINESTRIKE(dataframe)
        dataframe['CDL3OUTSIDE'] = ta.CDL3OUTSIDE(dataframe)
        dataframe['CDL3STARSINSOUTH'] = ta.CDL3STARSINSOUTH(dataframe)
        dataframe['CDL3WHITESOLDIERS'] = ta.CDL3WHITESOLDIERS(dataframe)
        dataframe['CDLABANDONEDBABY'] = ta.CDLABANDONEDBABY(dataframe)
        dataframe['CDLADVANCEBLOCK'] = ta.CDLADVANCEBLOCK(dataframe)
        dataframe['CDLBELTHOLD'] = ta.CDLBELTHOLD(dataframe)
        dataframe['CDLBREAKAWAY'] = ta.CDLBREAKAWAY(dataframe)
        dataframe['CDLCLOSINGMARUBOZU'] = ta.CDLCLOSINGMARUBOZU(dataframe)
        dataframe['CDLCONCEALBABYSWALL'] = ta.CDLCONCEALBABYSWALL(dataframe)
        dataframe['CDLCOUNTERATTACK'] = ta.CDLCOUNTERATTACK(dataframe)
        dataframe['CDLDARKCLOUDCOVER'] = ta.CDLDARKCLOUDCOVER(dataframe)
        dataframe['CDLDOJI'] = ta.CDLDOJI(dataframe)
        dataframe['CDLDOJISTAR'] = ta.CDLDOJISTAR(dataframe)
        dataframe['CDLDRAGONFLYDOJI'] = ta.CDLDRAGONFLYDOJI(dataframe)
        dataframe['CDLENGULFING'] = ta.CDLENGULFING(dataframe)
        dataframe['CDLEVENINGDOJISTAR'] = ta.CDLEVENINGDOJISTAR(dataframe)
        dataframe['CDLEVENINGSTAR'] = ta.CDLEVENINGSTAR(dataframe)
        dataframe['CDLGAPSIDESIDEWHITE'] = ta.CDLGAPSIDESIDEWHITE(dataframe)
        dataframe['CDLGRAVESTONEDOJI'] = ta.CDLGRAVESTONEDOJI(dataframe)
        dataframe['CDLHAMMER'] = ta.CDLHAMMER(dataframe)
        dataframe['CDLHANGINGMAN'] = ta.CDLHANGINGMAN(dataframe)
        dataframe['CDLHARAMI'] = ta.CDLHARAMI(dataframe)
        dataframe['CDLHARAMICROSS'] = ta.CDLHARAMICROSS(dataframe)
        dataframe['CDLHIGHWAVE'] = ta.CDLHIGHWAVE(dataframe)
        dataframe['CDLHIKKAKE'] = ta.CDLHIKKAKE(dataframe)
        dataframe['CDLHIKKAKEMOD'] = ta.CDLHIKKAKEMOD(dataframe)
        dataframe['CDLHOMINGPIGEON'] = ta.CDLHOMINGPIGEON(dataframe)
        dataframe['CDLIDENTICAL3CROWS'] = ta.CDLIDENTICAL3CROWS(dataframe)
        dataframe['CDLINNECK'] = ta.CDLINNECK(dataframe)
        dataframe['CDLINVERTEDHAMMER'] = ta.CDLINVERTEDHAMMER(dataframe)
        dataframe['CDLKICKING'] = ta.CDLKICKING(dataframe)
        dataframe['CDLKICKINGBYLENGTH'] = ta.CDLKICKINGBYLENGTH(dataframe)
        dataframe['CDLLADDERBOTTOM'] = ta.CDLLADDERBOTTOM(dataframe)
        dataframe['CDLLONGLEGGEDDOJI'] = ta.CDLLONGLEGGEDDOJI(dataframe)
        dataframe['CDLLONGLINE'] = ta.CDLLONGLINE(dataframe)
        dataframe['CDLMARUBOZU'] = ta.CDLMARUBOZU(dataframe)
        dataframe['CDLMATCHINGLOW'] = ta.CDLMATCHINGLOW(dataframe)
        dataframe['CDLMATHOLD'] = ta.CDLMATHOLD(dataframe)
        dataframe['CDLMORNINGDOJISTAR'] = ta.CDLMORNINGDOJISTAR(dataframe)
        dataframe['CDLMORNINGSTAR'] = ta.CDLMORNINGSTAR(dataframe)
        dataframe['CDLONNECK'] = ta.CDLONNECK(dataframe)
        dataframe['CDLPIERCING'] = ta.CDLPIERCING(dataframe)
        dataframe['CDLRICKSHAWMAN'] = ta.CDLRICKSHAWMAN(dataframe)
        dataframe['CDLRISEFALL3METHODS'] = ta.CDLRISEFALL3METHODS(dataframe)
        dataframe['CDLSEPARATINGLINES'] = ta.CDLSEPARATINGLINES(dataframe)
        dataframe['CDLSHOOTINGSTAR'] = ta.CDLSHOOTINGSTAR(dataframe)
        dataframe['CDLSHORTLINE'] = ta.CDLSHORTLINE(dataframe)
        dataframe['CDLSPINNINGTOP'] = ta.CDLSPINNINGTOP(dataframe)
        dataframe['CDLSTALLEDPATTERN'] = ta.CDLSTALLEDPATTERN(dataframe)
        dataframe['CDLSTICKSANDWICH'] = ta.CDLSTICKSANDWICH(dataframe)
        dataframe['CDLTAKURI'] = ta.CDLTAKURI(dataframe)
        dataframe['CDLTASUKIGAP'] = ta.CDLTASUKIGAP(dataframe)
        dataframe['CDLTHRUSTING'] = ta.CDLTHRUSTING(dataframe)
        dataframe['CDLTRISTAR'] = ta.CDLTRISTAR(dataframe)
        dataframe['CDLUNIQUE3RIVER'] = ta.CDLUNIQUE3RIVER(dataframe)
        dataframe['CDLUPSIDEGAP2CROWS'] = ta.CDLUPSIDEGAP2CROWS(dataframe)
        dataframe['CDLXSIDEGAP3METHODS'] = ta.CDLXSIDEGAP3METHODS(dataframe)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        """
        conditions = []

        # Check that volume is not 0

        """ for candleName in candleNames:
            conditions.append(dataframe[candleName] == self[candleName].value) """

        conditions.append(dataframe['CDL2CROWS'] == self.CDL2CROWS.value)
        conditions.append(dataframe['CDL3BLACKCROWS'] == self.CDL3BLACKCROWS.value)
        conditions.append(dataframe['CDL3INSIDE'] == self.CDL3INSIDE.value)
        conditions.append(dataframe['CDL3LINESTRIKE'] == self.CDL3LINESTRIKE.value)
        conditions.append(dataframe['CDL3OUTSIDE'] == self.CDL3OUTSIDE.value)
        conditions.append(dataframe['CDL3STARSINSOUTH'] == self.CDL3STARSINSOUTH.value)
        conditions.append(dataframe['CDL3WHITESOLDIERS'] == self.CDL3WHITESOLDIERS.value)
        conditions.append(dataframe['CDLABANDONEDBABY'] == self.CDLABANDONEDBABY.value)
        conditions.append(dataframe['CDLADVANCEBLOCK'] == self.CDLADVANCEBLOCK.value)
        conditions.append(dataframe['CDLBELTHOLD'] == self.CDLBELTHOLD.value)
        conditions.append(dataframe['CDLBREAKAWAY'] == self.CDLBREAKAWAY.value)
        conditions.append(dataframe['CDLCLOSINGMARUBOZU'] == self.CDLCLOSINGMARUBOZU.value)
        conditions.append(dataframe['CDLCONCEALBABYSWALL'] == self.CDLCONCEALBABYSWALL.value)
        conditions.append(dataframe['CDLCOUNTERATTACK'] == self.CDLCOUNTERATTACK.value)
        conditions.append(dataframe['CDLDARKCLOUDCOVER'] == self.CDLDARKCLOUDCOVER.value)
        conditions.append(dataframe['CDLDOJI'] == self.CDLDOJI.value)
        conditions.append(dataframe['CDLDOJISTAR'] == self.CDLDOJISTAR.value)
        conditions.append(dataframe['CDLDRAGONFLYDOJI'] == self.CDLDRAGONFLYDOJI.value)
        conditions.append(dataframe['CDLENGULFING'] == self.CDLENGULFING.value)
        conditions.append(dataframe['CDLEVENINGDOJISTAR'] == self.CDLEVENINGDOJISTAR.value)
        conditions.append(dataframe['CDLEVENINGSTAR'] == self.CDLEVENINGSTAR.value)
        conditions.append(dataframe['CDLGAPSIDESIDEWHITE'] == self.CDLGAPSIDESIDEWHITE.value)
        conditions.append(dataframe['CDLGRAVESTONEDOJI'] == self.CDLGRAVESTONEDOJI.value)
        conditions.append(dataframe['CDLHAMMER'] == self.CDLHAMMER.value)
        conditions.append(dataframe['CDLHANGINGMAN'] == self.CDLHANGINGMAN.value)
        conditions.append(dataframe['CDLHARAMI'] == self.CDLHARAMI.value)
        conditions.append(dataframe['CDLHARAMICROSS'] == self.CDLHARAMICROSS.value)
        conditions.append(dataframe['CDLHIGHWAVE'] == self.CDLHIGHWAVE.value)
        conditions.append(dataframe['CDLHIKKAKE'] == self.CDLHIKKAKE.value)
        conditions.append(dataframe['CDLHIKKAKEMOD'] == self.CDLHIKKAKEMOD.value)
        conditions.append(dataframe['CDLHOMINGPIGEON'] == self.CDLHOMINGPIGEON.value)
        conditions.append(dataframe['CDLIDENTICAL3CROWS'] == self.CDLIDENTICAL3CROWS.value)
        conditions.append(dataframe['CDLINNECK'] == self.CDLINNECK.value)
        conditions.append(dataframe['CDLINVERTEDHAMMER'] == self.CDLINVERTEDHAMMER.value)
        conditions.append(dataframe['CDLKICKING'] == self.CDLKICKING.value)
        conditions.append(dataframe['CDLKICKINGBYLENGTH'] == self.CDLKICKINGBYLENGTH.value)
        conditions.append(dataframe['CDLLADDERBOTTOM'] == self.CDLLADDERBOTTOM.value)
        conditions.append(dataframe['CDLLONGLEGGEDDOJI'] == self.CDLLONGLEGGEDDOJI.value)
        conditions.append(dataframe['CDLLONGLINE'] == self.CDLLONGLINE.value)
        conditions.append(dataframe['CDLMARUBOZU'] == self.CDLMARUBOZU.value)
        conditions.append(dataframe['CDLMATCHINGLOW'] == self.CDLMATCHINGLOW.value)
        conditions.append(dataframe['CDLMATHOLD'] == self.CDLMATHOLD.value)
        conditions.append(dataframe['CDLMORNINGDOJISTAR'] == self.CDLMORNINGDOJISTAR.value)
        conditions.append(dataframe['CDLMORNINGSTAR'] == self.CDLMORNINGSTAR.value)
        conditions.append(dataframe['CDLONNECK'] == self.CDLONNECK.value)
        conditions.append(dataframe['CDLPIERCING'] == self.CDLPIERCING.value)
        conditions.append(dataframe['CDLRICKSHAWMAN'] == self.CDLRICKSHAWMAN.value)
        conditions.append(dataframe['CDLRISEFALL3METHODS'] == self.CDLRISEFALL3METHODS.value)
        conditions.append(dataframe['CDLSEPARATINGLINES'] == self.CDLSEPARATINGLINES.value)
        conditions.append(dataframe['CDLSHOOTINGSTAR'] == self.CDLSHOOTINGSTAR.value)
        conditions.append(dataframe['CDLSHORTLINE'] == self.CDLSHORTLINE.value)
        conditions.append(dataframe['CDLSPINNINGTOP'] == self.CDLSPINNINGTOP.value)
        conditions.append(dataframe['CDLSTALLEDPATTERN'] == self.CDLSTALLEDPATTERN.value)
        conditions.append(dataframe['CDLSTICKSANDWICH'] == self.CDLSTICKSANDWICH.value)
        conditions.append(dataframe['CDLTAKURI'] == self.CDLTAKURI.value)
        conditions.append(dataframe['CDLTASUKIGAP'] == self.CDLTASUKIGAP.value)
        conditions.append(dataframe['CDLTHRUSTING'] == self.CDLTHRUSTING.value)
        conditions.append(dataframe['CDLTRISTAR'] == self.CDLTRISTAR.value)
        conditions.append(dataframe['CDLUNIQUE3RIVER'] == self.CDLUNIQUE3RIVER.value)
        conditions.append(dataframe['CDLUPSIDEGAP2CROWS'] == self.CDLUPSIDEGAP2CROWS.value)
        conditions.append(dataframe['CDLXSIDEGAP3METHODS'] == self.CDLXSIDEGAP3METHODS.value)

        if conditions:
            dataframe.loc[
                (
                    (qtpylib.crossed_above(dataframe['rsi'], self.buy_rsi.value)) &
                    dataframe['volume'] > 0 &
                    reduce(lambda x, y: x | y, conditions)
                ),
                'enter_long'] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        """

        return dataframe
