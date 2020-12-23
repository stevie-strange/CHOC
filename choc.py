from fitparse import FitFile
#from datetime import datetime

# Split point of the 2 linear functions
CURVE_THRESHOLD = 175

fit_file = FitFile('BikeFile3.fit')

total_cho = 0

for record in fit_file.get_messages("record"):
    
    for data in record:
        
        current_power = 0

        if data.name == 'power':
            #print(f"{data.name}, {data.value}, {data.units}")
            current_power = data.value
            #print(current_power)

            if current_power is not None:
                if current_power <= CURVE_THRESHOLD:
                    cho = 11.43 * current_power
                    
                    # scaled down from CHO per day to 1 second
                    total_cho = total_cho + (cho/24/60/60)
                else:
                    cho = 12.86 * current_power - 251
                    total_cho = total_cho + (cho/24/60/60)

print("Total carbos: ", total_cho)

        #if data.name == 'timestamp':
            #print(f"{data.name}, {data.value}, {data.units}")
         #   current_timestamp = data.value
          #  print(current_timestamp)
            #print(type(current_timestamp))

