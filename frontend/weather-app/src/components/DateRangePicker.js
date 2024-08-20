import React, { useState } from 'react';
import { LocalizationProvider, DatePicker } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { Grid, Box, Button } from '@mui/material';

const DateRangePicker = ({ onDatesChange }) => {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const lg = 4, sm = 6, xl = 3, xs = 12;

  const handleStartDateChange = (newDate) => {
    if (newDate != startDate) {
      setStartDate(newDate);
    } 
  };
  const handleEndDateChange = (newDate) => {
    if (newDate != endDate) {
      setEndDate(newDate);
    } 
  };


  const handleSubmit = () => {
    onDatesChange(startDate, endDate);
  };

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      {/* <Stack direction="row" alignItems="center" spacing={2}> */}
        <Box display="flex" justifyContent="space-between"  >
            <fieldset className="dashboardFilter">
            <legend>Filter By:</legend>
                <Grid container spacing={3}>
                    <Grid item lg={lg} sm={sm} xl={xl} xs={xs}>
                        <DatePicker label="Start Date"value={startDate} onChange={handleStartDateChange} format="DD/MM/YYYY"/>
                    </Grid>
                    <Grid item lg={lg} sm={sm} xl={xl} xs={xs}>
                        <DatePicker label="End Date"value={endDate} onChange={handleEndDateChange} format="DD/MM/YYYY"/>
                    </Grid>
                    <Grid item lg={lg} sm={sm} xl={xl} xs={xs}>
                        <Button variant="contained" onClick={handleSubmit}>Apply</Button>
                    </Grid>


                </Grid>
            </fieldset>
        </Box>

      {/* </Stack> */}
    </LocalizationProvider>
  );
};

export default DateRangePicker;