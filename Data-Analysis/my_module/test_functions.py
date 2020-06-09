# Import Library
import weather_anaylsis
import pandas as pd

# Import Excel File
df = pd.read_excel('SD_year_temp.xlsx')

# Define data variables
month = df['Month']
date_month = df['Date of month']
date_year = df['Date of Year']
max_temp = df['Maximum Temperature']
min_temp = df['Minimum Temperature']
avg_temp = df['Average Temperature']
rain = df['Precipitation']


def test_day_weather():
    """Test if the day_weather function is extracting the correct data set

    Parameters
    ----------
    input_string : month
        Array of data sets
    input_string : date_month
        Array of data sets
    input_string : max_temp
        Array of data sets
    input_string : min_temp
        Array of data sets
    input_string : min_temp
        Array of data sets
    input_string : avg_temp
        Array of data sets
    input_string : rain
        Array of data sets

    """
    # Define values for the first set of parameters
    choice_month1 = 9
    choice_day1 = 12
    ma_temp1 = 79
    mi_temp1 = 51
    av_temp1 = 65
    pre1 = 0.13

    # Define values for the second set of parameters
    choice_month2 = 2
    choice_day2 = 10
    ma_temp2 = 34
    mi_temp2 = 5
    av_temp2 = 19.5
    pre2 = 0.1   # 0.24

    # Define the output for assert comparsion
    output1 = print('On', choice_month1, '/', choice_day1, '\n'
                    'The Maximum Temperature =', ma_temp1, '°F', '\n'
                    'The Minimum Temperature =', mi_temp1, '°F', '\n'
                    'The Average Temperature =', av_temp1, '°F', '\n'
                    'Precipitation =', pre1, 'L/m^2')

    output2 = print('On', choice_month2, '/', choice_day2, '\n'
                    'The Maximum Temperature =', ma_temp2, '°F', '\n'
                    'The Minimum Temperature =', mi_temp2, '°F', '\n'
                    'The Average Temperature =', av_temp2, '°F', '\n'
                    'Precipitation =', pre2, 'L/m^2')

    assert weather_anaylsis.day_weather(choice_month1, choice_day1, month,
                                        date_month, max_temp, min_temp,
                                        avg_temp, rain) == output1
    assert weather_anaylsis.day_weather(choice_month2, choice_day2, month,
                                        date_month, max_temp, min_temp,
                                        avg_temp, rain) == output2


def test_desire_months():
    """Test if the desire_months function is extracting the correct data set

    Parameters
    ----------
    input_string : month
        Array of data sets
    input_string : date_month
        Array of data sets
    input_string : max_temp
        Array of data sets
    input_string : min_temp
        Array of data sets
    input_string : min_temp
        Array of data sets
    input_string : avg_temp
        Array of data sets
    input_string : rain
        Array of data sets

    """
    # Define values on parameters
    choice_month_start1 = 2
    choice_month_end1 = 10
    choice_month_start2 = 2
    choice_month_end2 = 2

    # Define the output for assert comparsion
    output1 = 1911
    output2 = 196
    df1 = weather_anaylsis.desire_months(choice_month_start1,
                                         choice_month_end1,
                                         month, date_month, date_year,
                                         max_temp, min_temp, avg_temp,
                                         rain)
    df2 = weather_anaylsis.desire_months(choice_month_start2,
                                         choice_month_end2,
                                         month, date_month, date_year,
                                         max_temp, min_temp, avg_temp,
                                         rain)

    assert df1.size == output1
    assert df2.size == output2