try:
  c=int(input())
  d=int(input())
except KeyboardInterrupt as e:
  print('KeyboardInterrupt',e)
except EOF as e:
  print('EOF',e)
except ValueError as e:
  print('value error',e)
  
  
  
  
