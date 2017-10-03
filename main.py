from netCDF4 import Dataset

if __name__ == '__main__':
    SDF_0 = Dataset(
        '/ouce-home/data/satellite/meteosat/seviri/15-min/native/sdf/nc'
        '/JUNE2012/SDF_v2/SDF_v2.201206221800.nc')

    year_lower = 2012
    year_upper = 2012
    month_lower = 6
    month_upper = 6
    day_lower = 1
    day_upper = 30
    hour_lower = 0
    hour_upper = 23
    minute_lower = 0
    minute_upper = 45

    time_params = np.array([year_lower, year_upper, month_lower,
                            month_upper, day_lower, day_upper,
                            hour_lower, hour_upper, minute_lower,
                            minute_upper])




