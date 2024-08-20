import React, { useState, useEffect } from 'react';
import './App.css';
import WeatherData from './components/WeatherData';
import WeatherSummary from './components/WeatherSummary';
import { getWeatherData, queryWeatherData, getDailyWeatherDataSum, queryDailyWeatherDataSum } from './services/api';

function App() {
  const [weatherData, setWeatherData] = useState([]);
  const [weatherSummary, setWeatherSummary] = useState([]);

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
      <h1>Weather Data</h1>
      <WeatherData data={weatherData} />
      <WeatherSummary data={weatherSummary} />
      {/* Add UI elements for querying data */}
    </div>
  );
}

export default App;