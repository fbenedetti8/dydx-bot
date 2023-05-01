from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADES, MANAGE_EXITS
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits


if __name__ == "__main__":
  
  # Connect to client 
  try:
    client = connect_dydx()
  except Exception as e:
    print("Error conectado al cliente ", e)
    exit(1)
    
  # Abort all open positions
  if ABORT_ALL_POSITIONS:
    try:
      print("Cerrando posiciones...")
      close_orders = abort_all_positions(client)
    except Exception as e:
      print("Fallo cerrar posiciones! ", e)
      exit(1)
  
  # Find Cointegrated Pairs
  if FIND_COINTEGRATED:
    # Construct Market prices
    try:
      print("Fetching market prices, puede tardar 3 mins...")
      df_market_prices = construct_market_prices(client)
    except Exception as e:
      print("Fallo en market prices! ", e)
      exit(1)
      
    # Store Cointegrated Pairs  
    try:
      print("Guardando cointegrates Pairs...")
      stores_result = store_cointegration_results(df_market_prices)
      if stores_result != "saved":
        print("Error Guardando Pares!")
        exit(1)
    except Exception as e:
      print("Error Guardando Pares! ", e)
      exit(1)
   
   
  # Correr constantemente 
  while true:
 
    # Place trades for opening positions
    if MANAGE_EXITS:
      try:
        print("Manegando trades existentes...")
        manage_trade_exits(client)
        
      except Exception as e:
        print("Error manegando trades existentes! ", e)
        exit(1)
      
    
    # Place trades for opening positions
    if PLACE_TRADES:
      try:
        print("Encontrando oportunidades de trading...")
        open_positions(client)
        
      except Exception as e:
        print("Error buscando oportunidades de trade! ", e)
        exit(1)