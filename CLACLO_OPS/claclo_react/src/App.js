import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ManageAccounts from './components/ManageAccounts';
import ManageSurveys from './components/ManageSurveys';

function App() {
    return (
        <BrowserRouter>
            <div>
                <Switch>
                    <Route path="/manage-accounts" component={ManageAccounts} />
                    <Route path="/manage-surveys" component={ManageSurveys} />
                    <Route path="/" component={Dashboard} />
                </Switch>
            </div>
        </BrowserRouter>
    );
}

export default App;
