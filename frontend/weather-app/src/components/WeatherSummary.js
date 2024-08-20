import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import DateRangePicker from './DateRangePicker';
import { queryDailyWeatherDataSum } from '../services/api';

const WeatherSummary = ({ data }) => {
    const [dailyWeatherDataSum, setDailyWeatherDataSum] = useState([]);
    const [startDate, setStartDate] = useState(null);
    const [endDate, setEndDate] = useState(null);   
  
  
    useEffect(() => {
      const fetchData = async () => {
        const   
   params = {
          start_date: startDate?.format('YYYY-MM-DD'),
          end_date: endDate?.format('YYYY-MM-DD'),
        };
        const data = await queryDailyWeatherDataSum(params);
        setDailyWeatherDataSum(data);
      };
  
      fetchData();
    }, [startDate, endDate]);
  
    const handleDatesChange = (newStartDate, newEndDate) => {
      setStartDate(newStartDate);
      setEndDate(newEndDate);
    };
  
    const columns = [
      { field: 'date', headerName: 'Date', width: 200 },
      { field: 'average_temperature', headerName: 'Average Temperature', width: 200 },
      { field: 'max_temperature', headerName: 'Max Temperature', width: 200 },
      { field: 'min_temperature', headerName: 'Min Temperature', width: 200 },
    ];
  
  return (
    <div>
      <DateRangePicker onDatesChange={handleDatesChange} />
      <DataGrid getRowId={(row) => row.date} rows={dailyWeatherDataSum} columns={columns} />
    </div>
  );
};

export default WeatherSummary;