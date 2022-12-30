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

class Strategy002V4(IStrategy):
    """
    Strategy 002
    author@: Gerald Lonlas
    github@: https://github.com/freqtrade/freqtrade-strategies
    How to use it?
    > python3 ./freqtrade/main.py -s Strategy002
    """

    CDL2CROWS_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3BLACKCROWS_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3INSIDE_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3LINESTRIKE_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3OUTSIDE_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3STARSINSOUTH_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDL3WHITESOLDIERS_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLABANDONEDBABY_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLADVANCEBLOCK_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLBELTHOLD_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLBREAKAWAY_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLCLOSINGMARUBOZU_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLCONCEALBABYSWALL_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLCOUNTERATTACK_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLDARKCLOUDCOVER_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLDOJI_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLDOJISTAR_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLDRAGONFLYDOJI_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLENGULFING_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLEVENINGDOJISTAR_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLEVENINGSTAR_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLGAPSIDESIDEWHITE_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLGRAVESTONEDOJI_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHAMMER_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHANGINGMAN_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHARAMI_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHARAMICROSS_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHIGHWAVE_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHIKKAKE_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHIKKAKEMOD_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLHOMINGPIGEON_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLIDENTICAL3CROWS_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLINNECK_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLINVERTEDHAMMER_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLKICKING_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLKICKINGBYLENGTH_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLLADDERBOTTOM_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLLONGLEGGEDDOJI_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLLONGLINE_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMARUBOZU_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMATCHINGLOW_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMATHOLD_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMORNINGDOJISTAR_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLMORNINGSTAR_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLONNECK_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLPIERCING_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLRICKSHAWMAN_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLRISEFALL3METHODS_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSEPARATINGLINES_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSHOOTINGSTAR_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSHORTLINE_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSPINNINGTOP_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSTALLEDPATTERN_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLSTICKSANDWICH_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLTAKURI_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLTASUKIGAP_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLTHRUSTING_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLTRISTAR_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLUNIQUE3RIVER_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLUPSIDEGAP2CROWS_BUY = CategoricalParameter([0, 100], default=100, space="buy")
    CDLXSIDEGAP3METHODS_BUY = CategoricalParameter([0, 100], default=100, space="buy")

    CDL2CROWS_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDL3BLACKCROWS_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDL3INSIDE_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDL3LINESTRIKE_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDL3OUTSIDE_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDL3STARSINSOUTH_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDL3WHITESOLDIERS_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLABANDONEDBABY_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLADVANCEBLOCK_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLBELTHOLD_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLBREAKAWAY_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLCLOSINGMARUBOZU_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLCONCEALBABYSWALL_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLCOUNTERATTACK_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLDARKCLOUDCOVER_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLDOJI_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLDOJISTAR_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLDRAGONFLYDOJI_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLENGULFING_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLEVENINGDOJISTAR_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLEVENINGSTAR_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLGAPSIDESIDEWHITE_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLGRAVESTONEDOJI_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLHAMMER_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLHANGINGMAN_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLHARAMI_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLHARAMICROSS_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLHIGHWAVE_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLHIKKAKE_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLHIKKAKEMOD_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLHOMINGPIGEON_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLIDENTICAL3CROWS_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLINNECK_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLINVERTEDHAMMER_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLKICKING_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLKICKINGBYLENGTH_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLLADDERBOTTOM_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLLONGLEGGEDDOJI_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLLONGLINE_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLMARUBOZU_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLMATCHINGLOW_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLMATHOLD_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLMORNINGDOJISTAR_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLMORNINGSTAR_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLONNECK_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLPIERCING_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLRICKSHAWMAN_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLRISEFALL3METHODS_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLSEPARATINGLINES_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLSHOOTINGSTAR_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLSHORTLINE_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLSPINNINGTOP_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLSTALLEDPATTERN_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLSTICKSANDWICH_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLTAKURI_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLTASUKIGAP_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLTHRUSTING_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLTRISTAR_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLUNIQUE3RIVER_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLUPSIDEGAP2CROWS_SELL = CategoricalParameter([0, 100], default=100, space="sell")
    CDLXSIDEGAP3METHODS_SELL = CategoricalParameter([0, 100], default=100, space="sell")

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
    sell_rsi = IntParameter(low=1, high=100, default=30, space='sell', optimize=True, load=True)

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

        conditions.append(dataframe['CDL2CROWS'] == self.CDL2CROWS_BUY.value)
        conditions.append(dataframe['CDL3BLACKCROWS'] == self.CDL3BLACKCROWS_BUY.value)
        conditions.append(dataframe['CDL3INSIDE'] == self.CDL3INSIDE_BUY.value)
        conditions.append(dataframe['CDL3LINESTRIKE'] == self.CDL3LINESTRIKE_BUY.value)
        conditions.append(dataframe['CDL3OUTSIDE'] == self.CDL3OUTSIDE_BUY.value)
        conditions.append(dataframe['CDL3STARSINSOUTH'] == self.CDL3STARSINSOUTH_BUY.value)
        conditions.append(dataframe['CDL3WHITESOLDIERS'] == self.CDL3WHITESOLDIERS_BUY.value)
        conditions.append(dataframe['CDLABANDONEDBABY'] == self.CDLABANDONEDBABY_BUY.value)
        conditions.append(dataframe['CDLADVANCEBLOCK'] == self.CDLADVANCEBLOCK_BUY.value)
        conditions.append(dataframe['CDLBELTHOLD'] == self.CDLBELTHOLD_BUY.value)
        conditions.append(dataframe['CDLBREAKAWAY'] == self.CDLBREAKAWAY_BUY.value)
        conditions.append(dataframe['CDLCLOSINGMARUBOZU'] == self.CDLCLOSINGMARUBOZU_BUY.value)
        conditions.append(dataframe['CDLCONCEALBABYSWALL'] == self.CDLCONCEALBABYSWALL_BUY.value)
        conditions.append(dataframe['CDLCOUNTERATTACK'] == self.CDLCOUNTERATTACK_BUY.value)
        conditions.append(dataframe['CDLDARKCLOUDCOVER'] == self.CDLDARKCLOUDCOVER_BUY.value)
        conditions.append(dataframe['CDLDOJI'] == self.CDLDOJI_BUY.value)
        conditions.append(dataframe['CDLDOJISTAR'] == self.CDLDOJISTAR_BUY.value)
        conditions.append(dataframe['CDLDRAGONFLYDOJI'] == self.CDLDRAGONFLYDOJI_BUY.value)
        conditions.append(dataframe['CDLENGULFING'] == self.CDLENGULFING_BUY.value)
        conditions.append(dataframe['CDLEVENINGDOJISTAR'] == self.CDLEVENINGDOJISTAR_BUY.value)
        conditions.append(dataframe['CDLEVENINGSTAR'] == self.CDLEVENINGSTAR_BUY.value)
        conditions.append(dataframe['CDLGAPSIDESIDEWHITE'] == self.CDLGAPSIDESIDEWHITE_BUY.value)
        conditions.append(dataframe['CDLGRAVESTONEDOJI'] == self.CDLGRAVESTONEDOJI_BUY.value)
        conditions.append(dataframe['CDLHAMMER'] == self.CDLHAMMER_BUY.value)
        conditions.append(dataframe['CDLHANGINGMAN'] == self.CDLHANGINGMAN_BUY.value)
        conditions.append(dataframe['CDLHARAMI'] == self.CDLHARAMI_BUY.value)
        conditions.append(dataframe['CDLHARAMICROSS'] == self.CDLHARAMICROSS_BUY.value)
        conditions.append(dataframe['CDLHIGHWAVE'] == self.CDLHIGHWAVE_BUY.value)
        conditions.append(dataframe['CDLHIKKAKE'] == self.CDLHIKKAKE_BUY.value)
        conditions.append(dataframe['CDLHIKKAKEMOD'] == self.CDLHIKKAKEMOD_BUY.value)
        conditions.append(dataframe['CDLHOMINGPIGEON'] == self.CDLHOMINGPIGEON_BUY.value)
        conditions.append(dataframe['CDLIDENTICAL3CROWS'] == self.CDLIDENTICAL3CROWS_BUY.value)
        conditions.append(dataframe['CDLINNECK'] == self.CDLINNECK_BUY.value)
        conditions.append(dataframe['CDLINVERTEDHAMMER'] == self.CDLINVERTEDHAMMER_BUY.value)
        conditions.append(dataframe['CDLKICKING'] == self.CDLKICKING_BUY.value)
        conditions.append(dataframe['CDLKICKINGBYLENGTH'] == self.CDLKICKINGBYLENGTH_BUY.value)
        conditions.append(dataframe['CDLLADDERBOTTOM'] == self.CDLLADDERBOTTOM_BUY.value)
        conditions.append(dataframe['CDLLONGLEGGEDDOJI'] == self.CDLLONGLEGGEDDOJI_BUY.value)
        conditions.append(dataframe['CDLLONGLINE'] == self.CDLLONGLINE_BUY.value)
        conditions.append(dataframe['CDLMARUBOZU'] == self.CDLMARUBOZU_BUY.value)
        conditions.append(dataframe['CDLMATCHINGLOW'] == self.CDLMATCHINGLOW_BUY.value)
        conditions.append(dataframe['CDLMATHOLD'] == self.CDLMATHOLD_BUY.value)
        conditions.append(dataframe['CDLMORNINGDOJISTAR'] == self.CDLMORNINGDOJISTAR_BUY.value)
        conditions.append(dataframe['CDLMORNINGSTAR'] == self.CDLMORNINGSTAR_BUY.value)
        conditions.append(dataframe['CDLONNECK'] == self.CDLONNECK_BUY.value)
        conditions.append(dataframe['CDLPIERCING'] == self.CDLPIERCING_BUY.value)
        conditions.append(dataframe['CDLRICKSHAWMAN'] == self.CDLRICKSHAWMAN_BUY.value)
        conditions.append(dataframe['CDLRISEFALL3METHODS'] == self.CDLRISEFALL3METHODS_BUY.value)
        conditions.append(dataframe['CDLSEPARATINGLINES'] == self.CDLSEPARATINGLINES_BUY.value)
        conditions.append(dataframe['CDLSHOOTINGSTAR'] == self.CDLSHOOTINGSTAR_BUY.value)
        conditions.append(dataframe['CDLSHORTLINE'] == self.CDLSHORTLINE_BUY.value)
        conditions.append(dataframe['CDLSPINNINGTOP'] == self.CDLSPINNINGTOP_BUY.value)
        conditions.append(dataframe['CDLSTALLEDPATTERN'] == self.CDLSTALLEDPATTERN_BUY.value)
        conditions.append(dataframe['CDLSTICKSANDWICH'] == self.CDLSTICKSANDWICH_BUY.value)
        conditions.append(dataframe['CDLTAKURI'] == self.CDLTAKURI_BUY.value)
        conditions.append(dataframe['CDLTASUKIGAP'] == self.CDLTASUKIGAP_BUY.value)
        conditions.append(dataframe['CDLTHRUSTING'] == self.CDLTHRUSTING_BUY.value)
        conditions.append(dataframe['CDLTRISTAR'] == self.CDLTRISTAR_BUY.value)
        conditions.append(dataframe['CDLUNIQUE3RIVER'] == self.CDLUNIQUE3RIVER_BUY.value)
        conditions.append(dataframe['CDLUPSIDEGAP2CROWS'] == self.CDLUPSIDEGAP2CROWS_BUY.value)
        conditions.append(dataframe['CDLXSIDEGAP3METHODS'] == self.CDLXSIDEGAP3METHODS_BUY.value)

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
        conditions = []

        conditions.append(dataframe['CDL2CROWS'] == self.CDL2CROWS_SELL.value)
        conditions.append(dataframe['CDL3BLACKCROWS'] == self.CDL3BLACKCROWS_SELL.value)
        conditions.append(dataframe['CDL3INSIDE'] == self.CDL3INSIDE_SELL.value)
        conditions.append(dataframe['CDL3LINESTRIKE'] == self.CDL3LINESTRIKE_SELL.value)
        conditions.append(dataframe['CDL3OUTSIDE'] == self.CDL3OUTSIDE_SELL.value)
        conditions.append(dataframe['CDL3STARSINSOUTH'] == self.CDL3STARSINSOUTH_SELL.value)
        conditions.append(dataframe['CDL3WHITESOLDIERS'] == self.CDL3WHITESOLDIERS_SELL.value)
        conditions.append(dataframe['CDLABANDONEDBABY'] == self.CDLABANDONEDBABY_SELL.value)
        conditions.append(dataframe['CDLADVANCEBLOCK'] == self.CDLADVANCEBLOCK_SELL.value)
        conditions.append(dataframe['CDLBELTHOLD'] == self.CDLBELTHOLD_SELL.value)
        conditions.append(dataframe['CDLBREAKAWAY'] == self.CDLBREAKAWAY_SELL.value)
        conditions.append(dataframe['CDLCLOSINGMARUBOZU'] == self.CDLCLOSINGMARUBOZU_SELL.value)
        conditions.append(dataframe['CDLCONCEALBABYSWALL'] == self.CDLCONCEALBABYSWALL_SELL.value)
        conditions.append(dataframe['CDLCOUNTERATTACK'] == self.CDLCOUNTERATTACK_SELL.value)
        conditions.append(dataframe['CDLDARKCLOUDCOVER'] == self.CDLDARKCLOUDCOVER_SELL.value)
        conditions.append(dataframe['CDLDOJI'] == self.CDLDOJI_SELL.value)
        conditions.append(dataframe['CDLDOJISTAR'] == self.CDLDOJISTAR_SELL.value)
        conditions.append(dataframe['CDLDRAGONFLYDOJI'] == self.CDLDRAGONFLYDOJI_SELL.value)
        conditions.append(dataframe['CDLENGULFING'] == self.CDLENGULFING_SELL.value)
        conditions.append(dataframe['CDLEVENINGDOJISTAR'] == self.CDLEVENINGDOJISTAR_SELL.value)
        conditions.append(dataframe['CDLEVENINGSTAR'] == self.CDLEVENINGSTAR_SELL.value)
        conditions.append(dataframe['CDLGAPSIDESIDEWHITE'] == self.CDLGAPSIDESIDEWHITE_SELL.value)
        conditions.append(dataframe['CDLGRAVESTONEDOJI'] == self.CDLGRAVESTONEDOJI_SELL.value)
        conditions.append(dataframe['CDLHAMMER'] == self.CDLHAMMER_SELL.value)
        conditions.append(dataframe['CDLHANGINGMAN'] == self.CDLHANGINGMAN_SELL.value)
        conditions.append(dataframe['CDLHARAMI'] == self.CDLHARAMI_SELL.value)
        conditions.append(dataframe['CDLHARAMICROSS'] == self.CDLHARAMICROSS_SELL.value)
        conditions.append(dataframe['CDLHIGHWAVE'] == self.CDLHIGHWAVE_SELL.value)
        conditions.append(dataframe['CDLHIKKAKE'] == self.CDLHIKKAKE_SELL.value)
        conditions.append(dataframe['CDLHIKKAKEMOD'] == self.CDLHIKKAKEMOD_SELL.value)
        conditions.append(dataframe['CDLHOMINGPIGEON'] == self.CDLHOMINGPIGEON_SELL.value)
        conditions.append(dataframe['CDLIDENTICAL3CROWS'] == self.CDLIDENTICAL3CROWS_SELL.value)
        conditions.append(dataframe['CDLINNECK'] == self.CDLINNECK_SELL.value)
        conditions.append(dataframe['CDLINVERTEDHAMMER'] == self.CDLINVERTEDHAMMER_SELL.value)
        conditions.append(dataframe['CDLKICKING'] == self.CDLKICKING_SELL.value)
        conditions.append(dataframe['CDLKICKINGBYLENGTH'] == self.CDLKICKINGBYLENGTH_SELL.value)
        conditions.append(dataframe['CDLLADDERBOTTOM'] == self.CDLLADDERBOTTOM_SELL.value)
        conditions.append(dataframe['CDLLONGLEGGEDDOJI'] == self.CDLLONGLEGGEDDOJI_SELL.value)
        conditions.append(dataframe['CDLLONGLINE'] == self.CDLLONGLINE_SELL.value)
        conditions.append(dataframe['CDLMARUBOZU'] == self.CDLMARUBOZU_SELL.value)
        conditions.append(dataframe['CDLMATCHINGLOW'] == self.CDLMATCHINGLOW_SELL.value)
        conditions.append(dataframe['CDLMATHOLD'] == self.CDLMATHOLD_SELL.value)
        conditions.append(dataframe['CDLMORNINGDOJISTAR'] == self.CDLMORNINGDOJISTAR_SELL.value)
        conditions.append(dataframe['CDLMORNINGSTAR'] == self.CDLMORNINGSTAR_SELL.value)
        conditions.append(dataframe['CDLONNECK'] == self.CDLONNECK_SELL.value)
        conditions.append(dataframe['CDLPIERCING'] == self.CDLPIERCING_SELL.value)
        conditions.append(dataframe['CDLRICKSHAWMAN'] == self.CDLRICKSHAWMAN_SELL.value)
        conditions.append(dataframe['CDLRISEFALL3METHODS'] == self.CDLRISEFALL3METHODS_SELL.value)
        conditions.append(dataframe['CDLSEPARATINGLINES'] == self.CDLSEPARATINGLINES_SELL.value)
        conditions.append(dataframe['CDLSHOOTINGSTAR'] == self.CDLSHOOTINGSTAR_SELL.value)
        conditions.append(dataframe['CDLSHORTLINE'] == self.CDLSHORTLINE_SELL.value)
        conditions.append(dataframe['CDLSPINNINGTOP'] == self.CDLSPINNINGTOP_SELL.value)
        conditions.append(dataframe['CDLSTALLEDPATTERN'] == self.CDLSTALLEDPATTERN_SELL.value)
        conditions.append(dataframe['CDLSTICKSANDWICH'] == self.CDLSTICKSANDWICH_SELL.value)
        conditions.append(dataframe['CDLTAKURI'] == self.CDLTAKURI_SELL.value)
        conditions.append(dataframe['CDLTASUKIGAP'] == self.CDLTASUKIGAP_SELL.value)
        conditions.append(dataframe['CDLTHRUSTING'] == self.CDLTHRUSTING_SELL.value)
        conditions.append(dataframe['CDLTRISTAR'] == self.CDLTRISTAR_SELL.value)
        conditions.append(dataframe['CDLUNIQUE3RIVER'] == self.CDLUNIQUE3RIVER_SELL.value)
        conditions.append(dataframe['CDLUPSIDEGAP2CROWS'] == self.CDLUPSIDEGAP2CROWS_SELL.value)
        conditions.append(dataframe['CDLXSIDEGAP3METHODS'] == self.CDLXSIDEGAP3METHODS_SELL.value)

        if conditions:
            dataframe.loc[
                (
                    (qtpylib.crossed_above(dataframe['rsi'], self.sell_rsi.value)) &
                    dataframe['volume'] > 0 &
                    reduce(lambda x, y: x | y, conditions)
                ),
                'exit_long'] = 1

        return dataframe
