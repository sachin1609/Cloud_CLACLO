//import React, { useState, useEffect } from 'react';
//import axios from 'axios';

//const ManageAccounts = () => {
//    const [accounts, setAccounts] = useState([]);

//    useEffect(() => {
//        axios.get('/api/accounts').then(res => setAccounts(res.data));
//    }, []);

//    const toggleAccountStatus = (id) => {
//        axios.post(`/api/toggle-account/${id}`).then(() => {
//            setAccounts(accounts.map(account => {
//                if (account.id === id) {
//                    account.isActive = !account.isActive;
//                }
//                return account;
//            }));
//        });
//    };

//    return (
//        <div className="container mt-4">
//            <h2>Manage Institute Accounts</h2>
//            {accounts.map(account => (
//                <div key={account.id}>
//                    <h5>{account.name}</h5>
//                    <button onClick={() => toggleAccountStatus(account.id)} className="btn btn-info">
//                        {account.isActive ? 'Deactivate' : 'Activate'}
//                    </button>
//                </div>
//            ))}
//        </div>
//    );
//}

//export default ManageAccounts;

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const UniversityList = () => {
    const [universities, setUniversities] = useState([]);

    useEffect(() => {
        fetchUniversities();
    }, []);

    const fetchUniversities = async () => {
        try {
            const response = await axios.get('http://localhost:8000/universities/');
            setUniversities(response.data);
        } catch (error) {
            console.error('Failed to fetch universities', error);
        }
    };

    const toggleUniversityActive = async (id, isActive) => {
        const endpoint = `http://localhost:8000/universities/${id}/${isActive ? 'deactivate' : 'activate'}`;
        try {
            await axios.patch(endpoint);
            fetchUniversities();  // Refresh list after updating
        } catch (error) {
            console.error('Failed to toggle active state', error);
        }
    };

    return (
        <div className="container">
            <h2>University Management</h2>
            {universities.map(uni => (
                <div key={uni.id} className="card mb-3">
                    <div className="card-body">
                        <h5 className="card-title">{uni.name}</h5>
                        <p className="card-text">Status: {uni.is_active ? 'Active' : 'Inactive'}</p>
                        <button className="btn btn-primary" onClick={() => toggleUniversityActive(uni.id, uni.is_active)}>
                            {uni.is_active ? 'Deactivate' : 'Activate'}
                        </button>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default UniversityList;
