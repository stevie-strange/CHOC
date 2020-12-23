from fitparse import FitFile
#from datetime import datetime

# Split point of the 2 linear functions
CURVE_THRESHOLD = 175

# Welcome message
print("CHOC - Individual carbohydrates calculator")

# User Input: Path to FIT file for analysis
file_path = input("Enter the FIT file: ")

# Read FIT file based on user input
fit_file = FitFile(file_path)

# Inform user about start of processing
print("Processing of FIT file started....")

# Reset CHO count
total_cho = 0

# Parse all record messages and extract the power information
for record in fit_file.get_messages("record"):
    
    for data in record:
        
        # Reset power 
        current_power = 0

        if data.name == 'power':
            
            # Extract the current power value
            current_power = data.value
            
            # validate the power information
            if current_power is not None:
                # if the power value is below the threshold value apply the first formula
                if current_power <= CURVE_THRESHOLD:
                    cho = 11.43 * current_power
                    
                    # scaled down from CHO per day to 1 second
                    total_cho = total_cho + (cho/24/60/60)
               
                # Since the power value is above the threshold use the second formula
                else:
                    cho = 12.86 * current_power - 251
                    total_cho = total_cho + (cho/24/60/60)

# Counter for the activity duration
activity_duration = 0

# read the total activity duration
for activity in fit_file.get_messages("activity"):

    for data in activity:
        if data.name == 'total_timer_time':
            activity_duration = activity_duration + data.value
    
# Convert activity to minutes
activity_duration = round(activity_duration / 60)

# Inform user about the results
print("Processing has finished.")
print("Total activity duration (min): ", activity_duration)
print("Total carbohydrates consumed (g): ", round(total_cho))
print("Carboyhdrates consumed per hour (g): ", round(total_cho / activity_duration * 60))