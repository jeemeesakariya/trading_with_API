# click on the link to get code
# url to get code = https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id=50846363-9409-4238-83cd-216832bd6f51&redirect_uri=https://pro.upstox.com/&state=<Your-Optional-State-Parameter-Here>


# import upstox_client
# from upstox_client.rest import ApiException

# api_instance = upstox_client.LoginApi()
# api_version = '2.0'
# code = '1AnRJu'
# client_id = 'bf62deac-51dd-4fbd-8793-5f5cab4f6a33'
# client_secret = 'u8zf2msppn'
# redirect_uri = 'https://pro.upstox.com/'
# grant_type = 'grant_type_example'

# try:
#     # Get token API
#     api_response = api_instance.token(api_version, code=code, client_id=client_id, client_secret=client_secret,
#                                       redirect_uri=redirect_uri, grant_type=grant_type)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling LoginApi->token: %s\n" % e)


# token= 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NmQxNzkxNDA4Y2IzNDcwZGJjZjliM2QiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzI1MDA0MDUyLCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3MjUwNTUyMDB9._wmO11Sh54-U1_lY-bTxbwtklV8ll7_vG6MNxTsDTpc'



# import upstox_client
# from upstox_client.rest import ApiException

# configuration = upstox_client.Configuration()
# configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NjIyMjA3ZDFjNDhmMTdmZmFlYjFlMWMiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTM1MTI1NzMsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxMzU2NDAwMH0.MKFmtiOQuhG0TnFnkWtDSgLoN2Om1rji3H7WnCG861U'

# api_version = '2.0'

# api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))

# try:
#     # Get User Fund And Margin
#     api_response = api_instance.get_profile(api_version)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling UserApi->get_user_fund_margin: %s\n" % e)



# import upstox_client
# from upstox_client.rest import ApiException

# configuration = upstox_client.Configuration()
# configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NjM2MTVhY2E1Yjg1MDBlNWMwMTc5NjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTQ4MjA1MjQsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxNDg2MDAwMH0.5W33TTSpwk7xLxgbDvi4utURYWQKpy8vqXnNXLjASQ4'

# api_version = '2.0'

# api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))

# try:
#     # Get User Fund And Margin
#     api_response = api_instance.get_user_fund_margin(api_version)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling UserApi->get_user_fund_margin: %s\n" % e)







# import upstox_client
# import pandas as pd
# import json
# import os

# from upstox_client.rest import ApiException

# configuration = upstox_client.Configuration()
# configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NjIyMjA3ZDFjNDhmMTdmZmFlYjFlMWMiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTM1MTI1NzMsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxMzU2NDAwMH0.MKFmtiOQuhG0TnFnkWtDSgLoN2Om1rji3H7WnCG861U'

# api_version = '2.0'

# api_instance = upstox_client.PortfolioApi(upstox_client.ApiClient(configuration))

# try:
#     # while True:
#         api_response = api_instance.get_holdings(api_version)
#         print(api_response)
#         # os.system('cls')

    
# except ApiException as e:
#     print("Exception when calling ChargeApi->get_brokerage: %s\n" % e)


# df=pd.DataFrame([{'average_price': 3534.4,
#            'close_price': 3872.8,
#            'cnc_used_quantity': 0,
#            'collateral_quantity': 0,
#            'collateral_type': 'WC',
#            'collateral_update_quantity': 0,
#            'company_name': 'TATA CONSULTANCY SERV LT',
#            'day_change': 0.0,
#            'day_change_percentage': -0.28,
#            'exchange': 'NSE',
#            'haircut': 0.2,
#            'instrument_token': 'NSE_EQ|INE467B01029',
#            'isin': 'INE467B01029',
#            'last_price': 3862.0,
#            'pnl': 327.6,
#            'product': 'D',
#            'quantity': 1,
#            't1_quantity': 0,
#            'trading_symbol': 'TCS',
#            'tradingsymbol': 'TCS'},
#           {'average_price': 5873.0,
#            'close_price': 7330.79,
#            'cnc_used_quantity': 0,
#            'collateral_quantity': 0,
#            'collateral_type': 'WC',
#            'collateral_update_quantity': 0,
#            'company_name': '2.50%GOLDBONDS2031SR-II',
#            'day_change': 0.0,
#            'day_change_percentage': -1.24,
#            'exchange': 'NSE',
#            'haircut': 0.1,
#            'instrument_token': 'NSE_EQ|IN0020230093',
#            'isin': 'IN0020230093',
#            'last_price': 7240.09,
#            'pnl': 1367.09,
#            'product': 'D',
#            'quantity': 1,
#            't1_quantity': 0,
#            'trading_symbol': 'SGBSEP31II',
#            'tradingsymbol': 'SGBSEP31II'}])
# print(df)





# #Get user positions
# import upstox_client
# from upstox_client.rest import ApiException

# configuration = upstox_client.Configuration()
# configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NjIyMjA3ZDFjNDhmMTdmZmFlYjFlMWMiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTM1MTI1NzMsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxMzU2NDAwMH0.MKFmtiOQuhG0TnFnkWtDSgLoN2Om1rji3H7WnCG861U'
# api_version = '2.0'

# api_instance = upstox_client.PortfolioApi(upstox_client.ApiClient(configuration))

# try:
#     api_response = api_instance.get_positions(api_version)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling ChargeApi->get_brokerage: %s\n" % e)





# Place Order

# Place a delivery limit order
# import upstox_client
# from upstox_client.rest import ApiException
# configuration = upstox_client.Configuration()
# configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NjIyMjA3ZDFjNDhmMTdmZmFlYjFlMWMiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTM1MTI1NzMsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxMzU2NDAwMH0.MKFmtiOQuhG0TnFnkWtDSgLoN2Om1rji3H7WnCG861U'
# api_instance = upstox_client.OrderApi(upstox_client.ApiClient(configuration))
# body = upstox_client.PlaceOrderRequest(1, 'I', 'DAY', 4000.00, 'string', 'NSE_EQ|INE467B01029', 'LIMIT', 'SELL', 1, 3835.70, False)
# api_version = '2.0'
# count=0
# try:
#     while count<9:
#         count=count+1
#         api_response = api_instance.place_order(body, api_version)
#         print(api_response)
# except ApiException as e:
#     print("Exception when calling OrderApi->place_order: %s\n" % e)



# Get report meta data for futures and options segment

# import upstox_client
# from upstox_client.rest import ApiException

# configuration = upstox_client.Configuration()
# configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NjM2MTVhY2E1Yjg1MDBlNWMwMTc5NjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTQ4MjA1MjQsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxNDg2MDAwMH0.5W33TTSpwk7xLxgbDvi4utURYWQKpy8vqXnNXLjASQ4'

# api_instance = upstox_client.TradeProfitAndLossApi(upstox_client.ApiClient(configuration))
# segment = 'FO'
# financial_year = '2324' # str | Financial year for which data has been requested. Concatenation of last 2 digits of from year and to year Sample:for 2021-2022, financial_year will be 2122
# api_version = '2.0' # str | API Version Header
# from_date = '02-04-2023' # str | Date from which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format (optional)
# to_date = '20-03-2024' # str | Date till which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format (optional)

# try:
#     # Get Trade-wise Profit and Loss Report Data
#     api_response = api_instance.get_trade_wise_profit_and_loss_meta_data(segment, financial_year, api_version, from_date=from_date, to_date=to_date)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling TradeProfitAndLossApi->get_trade_wise_profit_and_loss_data: %s\n" % e)




# Get profit loss report for futures and options segment

# import upstox_client
# from upstox_client.rest import ApiException

# configuration = upstox_client.Configuration()
# configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NjM2MTVhY2E1Yjg1MDBlNWMwMTc5NjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTQ4MjA1MjQsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxNDg2MDAwMH0.5W33TTSpwk7xLxgbDvi4utURYWQKpy8vqXnNXLjASQ4'

# api_instance = upstox_client.TradeProfitAndLossApi(upstox_client.ApiClient(configuration))
# segment = 'FO'
# financial_year = '2324' # str | Financial year for which data has been requested. Concatenation of last 2 digits of from year and to year Sample:for 2021-2022, financial_year will be 2122
# page_number = 1
# page_size = 1
# api_version = '2.0' # str | API Version Header
# from_date = '01-04-2023' # str | Date from which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format (optional)
# to_date = '31-03-2024' # str | Date till which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format (optional)

# try:
#     # Get Trade-wise Profit and Loss Report Data
#     api_response = api_instance.get_trade_wise_profit_and_loss_data(segment, financial_year, page_number, page_size, api_version, from_date=from_date, to_date=to_date)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling TradeProfitAndLossApi->get_trade_wise_profit_and_loss_data: %s\n" % e)



# Get trade charges for futures and options segment

# import upstox_client
# from upstox_client.rest import ApiException

# configuration = upstox_client.Configuration()
# configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2WEJWWkUiLCJqdGkiOiI2NjM2MTVhY2E1Yjg1MDBlNWMwMTc5NjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTQ4MjA1MjQsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxNDg2MDAwMH0.5W33TTSpwk7xLxgbDvi4utURYWQKpy8vqXnNXLjASQ4'
# api_instance = upstox_client.TradeProfitAndLossApi(upstox_client.ApiClient(configuration))
# segment = 'FO'
# financial_year = '2324' # str | Financial year for which data has been requested. Concatenation of last 2 digits of from year and to year Sample:for 2021-2022, financial_year will be 2122
# api_version = '2.0' # str | API Version Header
# from_date = '02-04-2023' # str | Date from which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format (optional)
# to_date = '20-03-2024' # str | Date till which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format (optional)

# try:
#     # Get Trade-wise Profit and Loss Report Data
#     api_response = api_instance.get_profit_and_loss_charges(segment, financial_year, api_version, from_date=from_date, to_date=to_date)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling TradeProfitAndLossApi->get_trade_wise_profit_and_loss_data: %s\n" % e)



# Get intraday candle data with a 30-minute interval

# import upstox_client
# from upstox_client.rest import ApiException

# api_version = '2.0'

# api_instance = upstox_client.HistoryApi()
# instrument_key = 'NSE_EQ|INE669E01016'
# interval = '30minute'
# try:

#     api_response = api_instance.get_intra_day_candle_data(instrument_key,interval,api_version)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling HistoryApi->get_historical_candle_data: %s\n" % e)




# Get data with a 30-minute interval

import upstox_client
from upstox_client.rest import ApiException

api_version = '2.0'

api_instance = upstox_client.HistoryApi()
instrument_key = 'NSE_EQ|INE669E01016'
interval = '30minute'
to_date = '2024-05-03'
from_date = '2024-05-02'
try:
    api_response = api_instance.get_historical_candle_data1(instrument_key, interval, to_date,from_date, api_version)
    print(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->get_historical_candle_data: %s\n" % e)







