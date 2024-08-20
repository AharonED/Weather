import React from 'react';

const WeatherData = ({ data }) => {
  return (
    <div>
      {data.map((item) => (
        <div key={item.id}>
          <p>Date: {item.date_time}</p>
          <p>Temperature: {item.temperature}°C</p>
          <p>Relative Humidity: {item.relative_humidity}%</p>
          <p>Wind Speed: {item.wind_speed}km/h</p>
        </div>
      ))}
    </div>
  );
};

export default WeatherData;