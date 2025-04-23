select * from stocks_data.stocks_data;

-- to understand how each stocks behave over time
SELECT symbol, Date(timestamp) as day, AVG(close) as avg_close
FROM stocks_data.stocks_data
GROUP BY symbol, day
ORDER BY day;


-- to know how much a stock price fluctuates
SELECT distinct symbol, timestamp, (high - low) as price_range
FROM stocks_data.stocks_data
ORDER BY symbol, timestamp;


-- to know how actively a stock is traded
SELECT symbol, AVG(volume) as avg_volume
FROM stocks_data.stocks_data
Group by symbol;


-- to compare between stocks
SELECT symbol, AVG(close) as avg_close
FROM stocks_data.stocks_data
Group By symbol;


-- to simulate gains/losses
SELECT *, ROUND((close - open)/open * 100, 2) as percent_return
FROM stocks_data.stocks_data;


-- to detect unusual behaviour : big price moves with low volume
SELECT 
  symbol,
  timestamp,
  open,
  close,
  volume,
  ROUND(ABS(close - open), 2) AS price_move,
  ROUND((ABS(close - open) / volume) * 1000000, 4) AS move_per_million_volume
FROM stocks_data.stocks_data
WHERE volume > 0
ORDER BY move_per_million_volume DESC;


-- Group by hour of day to detect patterns
SELECT symbol, HOUR(timestamp) as hour_of_day,
ROUND(AVG(volume)) AS avg_volume,
ROUND(AVG(ABS(close-open)),4) AS avg_price_move
FROM stocks_data.stocks_data
GROUP BY symbol, hour_of_day
ORDER BY symbol, hour_of_day;


-- Market Open vs Close Comparison
WITH ranked_prices AS (
  SELECT
    symbol,
    DATE(timestamp) AS trading_day,
    timestamp,
    open,
    close,
    ROW_NUMBER() OVER (PARTITION BY symbol, DATE(timestamp) ORDER BY timestamp ASC) AS rn_open,
    ROW_NUMBER() OVER (PARTITION BY symbol, DATE(timestamp) ORDER BY timestamp DESC) AS rn_close
  FROM stocks_data.stocks_data
),

daily_open_close AS (
  SELECT
    symbol,
    trading_day,
    MAX(CASE WHEN rn_open = 1 THEN open END) AS market_open,
    MAX(CASE WHEN rn_close = 1 THEN close END) AS market_close
  FROM ranked_prices
  GROUP BY symbol, trading_day
)

SELECT
  symbol,
  trading_day,
  market_open,
  market_close,
  ROUND(((market_close - market_open) / market_open) * 100, 2) AS daily_return_pct
FROM daily_open_close
ORDER BY trading_day, symbol;






