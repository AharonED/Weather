import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import DateRangePicker from './DateRangePicker';
import { getWeatherData, queryWeatherData, getDailyWeatherDataSum, queryDailyWeatherDataSum } from '../services/api';

const WeatherData = () => {
  const [weatherData, setWeatherData] = useState([]);
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);   


  useEffect(() => {
    const fetchData = async () => {
      const   
 params = {
        start_date: startDate?.format('YYYY-MM-DD'),
        end_date: endDate?.format('YYYY-MM-DD'),
      };
      const data = await queryWeatherData(params);
      setWeatherData(data);
    };

    fetchData();
  }, [startDate, endDate]);

  const handleDatesChange = (newStartDate, newEndDate) => {
    setStartDate(newStartDate);
    setEndDate(newEndDate);
  };

  const columns = [
    { field: 'date_time', headerName: 'Date', width: 200 },
    { field: 'temperature', headerName: 'Temperature (°C)', width: 200 },
    { field: 'relative_humidity', headerName: 'Relative Humidity (%)', width: 200 },
    { field: 'wind_speed', headerName: 'Wind Speed (km/h)', width: 200 },
  ];

  return (
    <div>
      <DateRangePicker onDatesChange={handleDatesChange} />
      <DataGrid getRowId={(row) => row.date_time} rows={weatherData} columns={columns} />
    </div>
  );
};

export default WeatherData;
