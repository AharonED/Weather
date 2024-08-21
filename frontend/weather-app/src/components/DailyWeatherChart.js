import React, { useEffect, useState } from 'react';
import DateRangePicker from './DateRangePicker';
import { queryDailyWeatherDataSum } from '../services/api';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';   


const DailyWeatherChart = ({ data }) => {
    const [dailyWeatherDataSum, setDailyWeatherDataSum] = useState([]);
    const [chartData, setChartData] = useState([]);
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

        const chartDatamap = data.map((item) => ({
            date: item.date,
            Avg: item.average_temperature,
            Min: item.min_temperature,
            Max: item.max_temperature,
          }));
          setChartData(chartDatamap)

      };
  
      fetchData();
    }, [startDate, endDate]);
  
    const handleDatesChange = (newStartDate, newEndDate) => {
      setStartDate(newStartDate);
      setEndDate(newEndDate);
    };
  
    // const columns = [
    //   { field: 'date', headerName: 'Date', width: 200 },
    //   { field: 'average_temperature', headerName: 'Average Temperature', width: 200 },
    //   { field: 'max_temperature', headerName: 'Max Temperature', width: 200 },
    //   { field: 'min_temperature', headerName: 'Min Temperature', width: 200 },
    // ];
  
  return (
    <div>
      <DateRangePicker onDatesChange={handleDatesChange} />
      {/* <DataGrid getRowId={(row) => row.date} rows={dailyWeatherDataSum} columns={columns} /> */}
      <LineChart width={600} height={300} data={chartData}>
      <Line type="monotone" dataKey="Avg" stroke="#63c768" strokeWidth={2} />
      <Line type="monotone" dataKey="Min" stroke="#384af2" strokeWidth={2} />
      <Line type="monotone" dataKey="Max" stroke="#f74040" strokeWidth={2} />
      <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
      </LineChart>

    </div>
  );
};

export default DailyWeatherChart;