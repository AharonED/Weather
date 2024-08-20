import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const NavigationBar = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Weather App
        </Typography>
        <Button color="inherit" href="/weather-data">Weather Data</Button>
        <Button color="inherit" href="/weather-summary">Weather Summary</Button>
      </Toolbar>
    </AppBar>
  );
};

export default NavigationBar;