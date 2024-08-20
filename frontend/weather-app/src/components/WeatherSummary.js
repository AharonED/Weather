import React from 'react';

const WeatherSummary = ({ data }) => {
  return (
    <div>
      {data.map((item) => (
        <div key={item.id}>
          <p>Date: {item.date}</p>
          <p>Average Temperature: {item.average_temperature}°C</p>
          <p>Max Temperature: {item.max_temperature}°C</p>
          <p>Min Temperature: {item.min_temperature}°C</p>
        </div>
      ))}
    </div>
  );
};

export default WeatherSummary;