<h1>CHOC - Individual carbohydrates calculator

<h2>Abstract

The purpose of this project is to estimate the effective consumption of carbohydrates during a cycling activity. 
  The calculation is based on the individual results of the indirect calorimetry of a spirometry.
  Based on the indirect calorimetry a simple model is created that uses linear functions to approximate the carbohydrates consumption.
  
  The results can be used to determine the right nutrition for refueling after a workout or for competitions, e.g. how much carbohydrates are consumed holding a specific wattage.
  

<h2>Prerequisites
  
  * Indirect calorimetry based on a spirometry.
  * Python libraries fitparse, scipy, plotly.
  * Cycling workouts with power data (FIT format).
 

<h2>General approach

The starting point is the indirect calorimetry as shown in the picture below.

![Initial indirect calorimetry](/images/Kalo_2018_cut.jpg)

Based on this result, the consumption curve for the carbohydrates (in black) can be split into 2 distinct parts.
The first part starts at the intersection point with the x-axis and continues up to the intercept of the CHO and the fat oxidation curves.

After this point, the second part of the CHO curve starts that shows a steeper angle than the first part. The second part ends with the ultimate end of the spirometry test.

For each of these 2 parts an individual linear function f(x) = m\*x+b can be defined as an approximation of the CHO consumption.

<h3>Parameters

* Intercept of CHO & FAT = ( 2200 g/day / 175 Watts)
* Intersection with x-axis = origin (0/0) since the recording was started earlier than the actual test.
* Top end of the 2nd linear function = (6000 g/day / 490 Watts)

Based on these data points the following 2 linear functions can be derived:

1. f(x) = 12,57 \* x for x <= 175 Watts
2. f(x) = 12,06 \* x + 91 for x > 175 Watts

The diagram below visualizes the determination of these key parameters.

*Notice: Due to the lack of the detailed data, the parameters were estimated based on the available diagram.*


<h2>Usage


