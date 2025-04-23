# Data Preparation

All stock files stored in BigQuery were merged using python script to form unified stocks data (stocks_data.csv) for comprehensive analysis.


# SQL Techniques used

1. **Aggregation & Grouping**
2. **Date & Time Handling**
3. **Window Functions**
4. **Common Table Expressions**
5. **Conditional Aggregation**
6. **Mathematical Calculations**
7. **Anomaly Detection**
   

# Key Insights Highlight

(The analysis is currently based on a single day; extending this over multiple days can reveal longer-term trends and momentum)

## Average Closing Price Per Stock

   - GOOGL had the highest average close price on April 17, 2025, indicating its premium market valuation.
   - AAPL and MSFT showed similar average price levels, suggesting correlated market behavior or investor sentiment.
   - NVDA recorded the lowest average price, which may be attributed to a lower trading denomination or recent stock split.


## Intraday Price Range (Volatility)
   Measure how much each stock fluctuates minute-by-minute during the trading day using the difference between the high and low price.

   ![image](https://github.com/user-attachments/assets/c96fa897-f2b2-4bdf-b33d-986c9545624b)

  - GOOGL shows a sharp spike in price range, likely around market open or major event — indicating a highly volatile moment.
  - Other stocks like MSFT and NVDA also had elevated price ranges, but GOOGL's volatility stands out prominently.
  - Outside of those spikes, price ranges are generally below 1, suggesting relatively calm trading periods.


## Average Trading Volume Per Stock

- NVDA dominates with the highest average volume, indicating extremely high trading activity — this could be due to strong investor interest, speculative behavior, or recent news/events.
- AAPL comes next, showing consistent interest from retail and institutional investors alike.
- MSFT and GOOGL, while active, see lower average intraday volume compared to NVDA and AAPL.


## Simulate Intraday Gains/Losses
Calculate percentage return per timestamp to understand short-term price movements and identify potential gains or losses on a per-minute basis.

![image](https://github.com/user-attachments/assets/aadbdc81-d873-4399-bc2d-d764a9bcf6a2)

- All four stocks exhibit volatility with sharp but short-lived movements.
- GOOGL shows a noticeable spike indicating a major movement at a specific minute — possibly news or high-volume trade.
- AAPL, MSFT, and NVDA show more subtle fluctuations around the 0% line, with occasional dips and rises.

## Detect Unusual Price Moves with Low Volume

Identify moments where a stock had a big price movement relative to its volume, which may indicate unusual trading activity or inefficiencies.

- At 2025-04-17 17:10:00, GOOGL jumped $6.36 on a very low volume (1,495), creating a high price move-to-volume ratio.
- This event might indicate a sharp but low-participation trade, possibly:
    - After-market volatility
    - Algorithmic spike
    - Delayed order processing
 
## Detect Patterns
![image](https://github.com/user-attachments/assets/9c5f6cad-2396-44c2-b42d-5b058cf07bdb)

- NVDA sees significantly higher trading volume across all hours — especially at 12 PM and 3 PM.
- All stocks spike in volume around 3 PM to 4 PM (market close), and a smaller spike at 12 PM (midday rebound).
- Volume drastically drops after 4 PM, suggesting most trading happens during standard market hours.

![image](https://github.com/user-attachments/assets/37103573-6519-4cb2-9eaa-4b306ae0ae57)

- GOOGL shows the most volatile price moves around 12 PM, especially compared to others.
- Price movement shrinks after 4 PM, matching reduced liquidity.
- Post-market activity (after 4 PM) still shows some minor movement for all stocks, but volume is minimal.

## Market Open vs Close Comparison
Compare each stock’s opening and closing price on the trading day to assess daily return performance.

![image](https://github.com/user-attachments/assets/ac9d81fe-caa1-4561-9078-0d630f65c696)

- NVDA was the only stock that closed higher than it opened, showing positive intraday sentiment.
- GOOGL had the largest negative return, closing nearly 1% down from its open.
- All other stocks saw slight losses, indicating a bearish or flat market sentiment on April 17.

  


   
