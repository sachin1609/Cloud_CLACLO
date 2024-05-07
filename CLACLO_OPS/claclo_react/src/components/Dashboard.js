import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    return (
        <div className="container mt-4">
            <h1>ClaClo Ops Dashboard</h1>
            <Link to="/manage-accounts" className="btn btn-primary">Manage Institute Accounts</Link>
            <Link to="/manage-surveys" className="btn btn-secondary mt-2">Manage Surveys</Link>
        </div>
    );
}

export default Dashboard;
