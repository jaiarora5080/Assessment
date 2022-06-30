import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import CreateWorkflow from './Components/CreateWorkflow'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route exact path='/' element={<App />} />
        <Route path='/create' element={<CreateWorkflow />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
