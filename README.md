### USEFULL COMMANDS

!! Use Admin privileges everywhere

#### Plotting
1. Uncomment in docker-compose.yml `image: freqtradeorg/freqtrade:develop_plot`
2. Dataframe:
```
   docker-compose run --rm freqtrade plot-dataframe --strategy GoldenCross1dBTC --export-filename user_data/backtest_results/backtest-result-2022-11-15_20-27-23.json -p BTC/USDT
```
3. Profits:
```
docker-compose run --rm freqtrade plot-profit --strategy GoldenCross1dBTC --export-filename user_data/backtest_results/backtest-result-2022-11-22_18-37-58.json -p BTC/USDT --timeframe 1d
```

#### Backtesting
    docker-compose run --rm freqtrade backtesting --config user_data/config.json --strategy GoldenCross1dBTC --timerange 20120101-20221115 -i 1d --pairs BTC/USDT
