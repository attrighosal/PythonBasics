from datetime import datetime

## Datetime to Epoch
current = datetime.now() 
# epoch = current.timestamp()
# print(f"Epoch : {epoch}")

## Epoch to Datetime
# dt = datetime.fromtimestamp(float(epoch)).strftime('%c')
# print(f"Datetime : {dt}")

## Different formats 
# print(current.strftime('%Y-%m-%d %H:%M:%S')) 

# Example 1
s = current.strftime("%A %m %-Y")
print('\nExample 1:', s)
 
# Example 2
s = current.strftime("%a %-m %y")
print('\nExample 2:', s)
 
# Example 3
s = current.strftime("%-I %p %S")
print('\nExample 3:', s)
 
# Example 4
s = current.strftime("%H:%M:%S")
print('\nExample 4:', s)