"""
This Module is responsible for finding the Maximum , Minimum Temperature and Humidity for either the yearly or monthly data
For the monthly data , it loops over each object , comparing it to a preset value of Maximum , Minimum Temperature and Humidity 
The required values are then stored  along with their dates in dictionaries 
For monthly data , returns  2 dictionaries , one for max and one for min temperature and a value for mean humidity 
For yearly data, returns   3 dictionaries , each corresponding to MAximum , Minimum Temperature and Maximum Humidity and their dates 
Contain an internal function to Parse date values and return the day , month and year accordingly 
"""

import datetime
from daily_weather_data import WeatherDataRow


class Compute:
    """
    Class containing Attributes for monthly data.
    Contains a method for computing the monthly data dictionary values .
    Contains a method for computing the yearly data values from the list of dictionaries
    """

    def __init__(self, total_data):
        """
        This Function Contains an Attribute Monthly data which is a list of objects and will be provided by the get_data module on instantiation
        as a parameter .
        """

        self.total_data = total_data

    def compute_data(self):
        """
        Loops over  objects in the total_data  list which is either of 30 to 31 objects or 365 or 366 objects signifying a whole year
        This allows for only one compute function to be used and for the iterable (list) to be looped over as many elements there are in the list

        Returns 2 objects of thhe Weather data row class , one with the maximum temperature and one with the minimum temperature in the total data
        """

        max_temp_month = -100
        min_temp_month = 100
        total_monthly_humi = 0
        humi_count = 0
        max_temp__monthly_obj = None
        min_temp_monthly_obj = None

        for row in self.total_data:

            if row.max_temp is not None:

                if row.max_temp > max_temp_month:
                    max_temp_month = row.max_temp
                    max_temp__monthly_obj = row

            if row.min_temp is not None:

                if row.min_temp < min_temp_month:
                    min_temp_month = row.min_temp
                    min_temp_monthly_obj = row

            if row.mean_humidity is not None:
                if row.mean_humidity != "":
                    row.mean_humidity = int(row.mean_humidity)
                    total_monthly_humi += row.mean_humidity
                    humi_count += 1

        mean_humidity_month = total_monthly_humi / humi_count

        return max_temp__monthly_obj, min_temp_monthly_obj, mean_humidity_month
