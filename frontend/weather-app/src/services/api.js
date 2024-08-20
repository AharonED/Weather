import axios from 'axios';

const baseURL = 'http://localhost:8000/api'; 

const getWeatherData = async () => {
  try {
    const response = await axios.get(`${baseURL}/get_all`);
    return response.data;
  } catch (error) {
    console.error('Error fetching weather data:', error);
    throw error;
  }
};

const queryWeatherData = async (params) => {
  try {
    const response = await axios.get(`${baseURL}/query`, { params });
    return response.data;
  } catch (error) {
    console.error('Error querying weather data:', error);
    throw error;
  }
};


const getDailyWeatherDataSum = async () => {
    try {
      const response = await axios.get(`${baseURL}/get_all_sum`);
      return response.data;
    } catch (error) {
      console.error('Error fetching weather data:', error);
      throw error;
    }
  };
  
  const queryDailyWeatherDataSum = async (params) => {
    try {
      const response = await axios.get(`${baseURL}/query_sum`, { params });
      return response.data;
    } catch (error) {
      console.error('Error querying weather data:', error);
      throw error;
    }
  };

export { getWeatherData, queryWeatherData, getDailyWeatherDataSum, queryDailyWeatherDataSum };