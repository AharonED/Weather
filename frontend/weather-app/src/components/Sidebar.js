import React from 'react';
import { List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import { Home, BarChart } from '@mui/icons-material';

const Sidebar = ({ setSelectedComponent }) => {
  return (
    <List>
      <ListItem button onClick={() => setSelectedComponent('weatherData')}>
        <ListItemIcon><Home /></ListItemIcon>
        <ListItemText primary="Weather Data" />
      </ListItem>
      <ListItem button onClick={() => setSelectedComponent('weatherSummary')}>
        <ListItemIcon><BarChart /></ListItemIcon>
        <ListItemText primary="Weather Summary" />
      </ListItem>
    </List>
  );
};

export default Sidebar;