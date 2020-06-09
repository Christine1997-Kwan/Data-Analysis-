# Import Library
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat


def day_weather(choice_month, choice_day,
                month, date_month,
                max_temp, min_temp,
                avg_temp, rain):
    """To extract the data set which matches the desire date

    Parameters
    ----------
    input_string : choice_month
        a number of integar within 1 to 12
    input_string : choice_day
        a number of integar within 1 to 28/30/31
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

    Returns
    -------
    output_string : print(string)
        A string which indicate the weather on the desire date
    """
    # Select the desired data set from the corresponding date
    for m_num, d_num, ma_temp, mi_temp, av_temp, pre in zip(month, date_month,
                                                            max_temp, min_temp,
                                                            avg_temp, rain):
        if m_num == choice_month and d_num == choice_day:
            return print('On', choice_month, '/', choice_day, '\n'
                         'The Maximum Temperature =', ma_temp, '°F', '\n'
                         'The Minimum Temperature =', mi_temp, '°F', '\n'
                         'The Average Temperature =', av_temp, '°F', '\n'
                         'Precipitation =', pre, 'L/m^2')


def desire_months(choice_month_start, choice_month_end, month, date_month,
                  date_year, max_temp, min_temp, avg_temp, rain):
    """To extract the data set which matches the desire date

    Parameters
    ----------
    input_string : choice_month_start
        a number of integar within 1 to 12
    input_string : choice_month_end
        a number of integar within 1 to 12, no less than start_range
    input_string : month
        Array of data sets
    input_string : date_month
        Array of data sets
    input_string : date_year
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

    Returns
    -------
    output_string : df1
        A DataFrame consist with all the parameters within the desire range
    """

    # Create empty list
    yd = []
    mo = []
    day = []
    ma = []
    mi = []
    av = []
    pr = []

    # Select the data set which matches the desire distance range
    for m_num, d_num, ma_temp, mi_temp, av_temp, pre, yeard in zip(month,
                                                                   date_month,
                                                                   max_temp,
                                                                   min_temp,
                                                                   avg_temp,
                                                                   rain,
                                                                   date_year):

        # Append all desire data into the empty list
        if m_num >= choice_month_start and m_num <= choice_month_end:
            mo.append(m_num)
            day.append(d_num)
            ma.append(ma_temp)
            mi.append(mi_temp)
            av.append(av_temp)
            pr.append(pre)
            yd.append(yeard)

    # Tranform from list to Series
    mo = pd.Series(mo)
    day = pd.Series(day)
    ma = pd.Series(ma)
    mi = pd.Series(mi)
    av = pd.Series(av)
    pr = pd.Series(pr)
    yd = pd.Series(yd)

    # Reform a new dataframe with new data set
    data_set = {'Month': mo, 'Day': day, 'Day in Year': yd,
                'Maximum Temperature': ma, 'Minimum Temperature': mi,
                'Average Temperature': av, 'Precipitation': pr}
    df1 = pd.DataFrame(data=data_set)

    return df1


def month_weather(choice_month_start, choice_month_end,
                  date_year, max_temp, min_temp, avg_temp, rain):
    """Plot out monthly temperature Vs day number in year plot
       and Precipitation Vs day number in year plot

    Parameters
    ----------
    input_string : choice_month_start
        a number of integar within 1 to 12
    input_string : choice_month_end
        a number of integar within 1 to 12, no less than start_range
    input_string : date_year
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

    Returns
    -------
    output_string : fig1
        A Temperature Vs day number in year plot
    output_string : fig2
        A Precipitation Vs day number in year plot
    """

    # Average temperature Calculation
    average = stat.mean(avg_temp)

    # Title lebal with corresponding months
    month_label1 = str(choice_month_start) + ' to '
    month_label2 = str(choice_month_end) + ' months'
    month_label = month_label1+month_label2

    title_temp_label = '2019' + ' ' + month_label + ' ' + \
                       'San Diego CA Temperature Distribution'
    title_pre_label = '2019' + ' ' + month_label + ' ' + \
                      'San Diego CA Precipitation Distribution'

    # Temperature Vs day number in year plot
    fig1 = plt.figure()  # Produce a figure
    plt.plot(date_year, max_temp, color='red', label='Max Temp')
    plt.plot(date_year, min_temp, color='blue', label='Min Temp')
    plt.axhline(y=average, color='r', label='Monthly Average')
    plt.title(title_temp_label)  # Title
    plt.ylabel('Temperature(°F)')  # X-axis label
    plt.xlabel('Day Number of The Year')  # Y-axis label
    plt.legend(fontsize=8)  # Add legend
    plt.grid()  # Add grid

    # Precipitation Vs day number in year plot
    fig2 = plt.figure()  # Produce a figure
    plt.plot(date_year, rain, color='blue', label='Precipitation')
    plt.title(title_pre_label)  # Title
    plt.ylabel('Precipitation (L/m^2)')  # X-axis label
    plt.xlabel('Day Number of The Year')  # Y-axis label
    plt.legend(fontsize=8)  # Add legend
    plt.grid()  # Add grid

    return fig1, fig2


def year_weather(max_temp, min_temp, avg_temp, rain):
    """Plot out entire year temperature Vs day number in year plot
       and Precipitation Vs day number in year plot

    Parameters
    ----------
    input_string : date_year
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

    Returns
    -------
    output_string : fig1
        A Temperature Vs day number in year plot
    output_string : fig2
        A Precipitation Vs day number in year plot
    """

    # Average temperature Calculation
    average = stat.mean(avg_temp)

    # Temperature Vs day number in year plot
    fig1 = plt.figure()  # Produce a figure
    plt.plot(max_temp, color='red', label='Max Temp')
    plt.plot(min_temp, color='blue', label='Min Temp')
    plt.axhline(y=average, color='r', label='Yearly Average')
    plt.title('2019 San Diego CA Temperature Distribution')  # Title
    plt.ylabel('Temperature(°F)')  # X-axis label
    plt.xlabel('Day Number of The Year')  # Y-axis label
    plt.legend(fontsize=8)  # Add legend
    plt.grid()  # Add grid

    # Precipitation Vs day number in year plot
    fig2 = plt.figure()  # Produce a figure
    plt.plot(rain, color='blue', label='Precipitation')
    plt.title('2019 San Diego CA Precipitation Distribution')  # Title
    plt.ylabel('Precipitation (L/m^2)')  # X-axis label
    plt.xlabel('Day Number of The Year')  # Y-axis label
    plt.legend(fontsize=8)  # Add legend
    plt.grid()  # Add grid

    return fig1, fig2