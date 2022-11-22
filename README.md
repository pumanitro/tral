### USEFULL COMMANDS

!! Use Admin privileges everywhere

#### Plotting
1. Uncomment in docker-compose.yml `image: freqtradeorg/freqtrade:develop_plot`
2. Command:
    docker-compose run --rm freqtrade plot-dataframe --strategy GoldenCross1dBTC --export-filename user_data/backtest_results/backtest-result-2022-11-15_20-27-23.json -p BTC/USDT

#### Backtesting
    docker-compose run --rm freqtrade backtesting --config user_data/config.json --strategy GoldenCross1dBTC --timerange 20120101-20221115 -i 1d --pairs BTC/USDT