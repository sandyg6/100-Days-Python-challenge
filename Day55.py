def check_lsb(number):
  lsb = number & 1

  return lsb != 0


number = 10  
if check_lsb(number):
  print("LSB of", number, "is set.")
else:
  print("LSB of", number, "is not set.")
