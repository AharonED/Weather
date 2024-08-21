import React from 'react';
import { List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import { Home, BarChart, Functions } from '@mui/icons-material';

const Sidebar = ({ setSelectedComponent }) => {
  return (
    <List>
      <ListItem button onClick={() => setSelectedComponent('weatherData')}>
        <ListItemIcon><Home /></ListItemIcon>
        <ListItemText primary="All Data" />
      </ListItem>
      <ListItem button onClick={() => setSelectedComponent('weatherSummary')}>
        <ListItemIcon><Functions /></ListItemIcon>
        <ListItemText primary="Summary" />
      </ListItem>
      <ListItem button onClick={() => setSelectedComponent('weatherSummaryChart')}>
        <ListItemIcon><BarChart /></ListItemIcon>
        <ListItemText primary="Trend" />
      </ListItem>
    </List>
  );
};

export default Sidebar;