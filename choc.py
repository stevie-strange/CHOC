from fitparse import FitFile
from scipy.signal import savgol_filter
import plotly.graph_objects as go

# Split point of the 2 linear functions
CURVE_THRESHOLD = 175

# Slope & intercept of first linear function
F1_SLOPE = 11.43
F1_INTERCEPT = 0

# Slope & intercept of second linear function
F2_SLOPE = 12.86
F2_INTERCEPT = -251


# function to calculate the CHO consumption
def calculate_cho(slope, intercept, power, cho_list):
    
    # Calculate CHO consumption based on linear function
    cho = slope * power + intercept
                    
    # scaled down from CHO per day to 1 hour
    cho = cho/24

    # Add the calculated value to list
    cho_list.append(round(cho))

    # Scale down to recording intervall of 1s
    cho = cho/60/60
                    
    # Return the cho conspumtion per s
    return cho


############### MAIN PROGRAM STARTS HERE ##############################
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

# List of all CHO values calculated
cho_values = []

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
                    
                    # call function with linear function 1
                    total_cho = total_cho + calculate_cho(F1_SLOPE, F1_INTERCEPT, current_power, cho_values)

                    
                # Since the power value is above the threshold use the second formula
                else:
                    
                    # call function with linear function 2
                    total_cho = total_cho + calculate_cho(F2_SLOPE, F2_INTERCEPT, current_power, cho_values)

                    

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


# Smooth data sets using the Savitzky-Golay filter, windows size 59s
smoothed_data = savgol_filter(cho_values, window_length=59, polyorder=1)

# print diagram
fig = go.Figure(data=go.Scatter(y=smoothed_data, 
                hoverlabel=dict(namelength=0), 
                hovertemplate='Data point<br>Workout time: %{x:,}<br>CHO: %{y:,} g/h'))

fig.update_layout(
    title='CHO consumption',
    xaxis_title='Workout time (s)',
    yaxis_title='CHO (g/h)')

fig.show()