
import React, { useState, useEffect } from 'react';
import { Grid, Typography } from '@mui/material';
import './App.css';
import { getWeatherData, queryWeatherData, getDailyWeatherDataSum, queryDailyWeatherDataSum } from './services/api';
import WeatherData from './components/WeatherData';
import WeatherSummary from './components/WeatherSummary';
import DailyWeatherChart from './components/DailyWeatherChart';

import Sidebar from './components/Sidebar'; // New component for sidebar


function App() {
  const [weatherData, setWeatherData] = useState([]);
  const [weatherSummary, setWeatherSummary] = useState([]);
  const [selectedComponent, setSelectedComponent] = useState('weatherData');

  useEffect(() => {
    const fetchData = async () => {
      const data = await getWeatherData();
      setWeatherData(data);
    };

    fetchData();
  }, []);

  const handleQuery = async (params) => {
    const data = await queryWeatherData(params);
    setWeatherSummary(data);
  };

  return (
    <div className="App">
      <h1>Weather Forecast</h1>

      <Grid container spacing={2}>
        <Grid item xs={2}>
          <Sidebar setSelectedComponent={setSelectedComponent} />
        </Grid>
        <Grid item xs={9}>
          {selectedComponent === 'weatherData' && <WeatherData data={[]} />}
          {selectedComponent === 'weatherSummary' && <WeatherSummary data={[]} />}
          {selectedComponent === 'weatherSummaryChart' && <DailyWeatherChart data={[]} />}
        </Grid>
      </Grid>

    </div>
    
  );
}

export default App;