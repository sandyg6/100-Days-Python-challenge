def decimalToBinary(ip_val):
    if ip_val >= 1:
        decimalToBinary(ip_val // 2)
  
    print(ip_val % 2, end = '')
 
if __name__ == '__main__':
    ip_val = int(input())
    decimalToBinary(ip_val)
