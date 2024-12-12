import sys
from ThaiCIDHelper  import *
from DataThaiCID    import *

# สร้าง Instance Class ThaiCIDHelper
reader = ThaiCIDHelper(APDU_SELECT,APDU_THAI_CARD)

# Connect SMC
response = reader.connectReader(0)
print(f'Reader: Connected [{reader.cardReaderIndex}]... [{response[0]}]') # .component.reader

# response value >> 0 = Reader as Connection , Connected Status ??
if response[1] == True:
    # Read Data
    reader.readData()
else:
    print(f'Error: {reader.lastError}')
    sys.exit()    

sys.exit()