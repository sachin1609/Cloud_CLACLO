//import React from 'react';
//import axios from 'axios';

//const ManageSurveys = () => {
//    const handleSurvey = (type) => {
//        axios.post(`/api/conduct-survey/${type}`).then(res => {
//            alert(`Survey for ${type} conducted successfully!`);
//        });
//    };

//    return (
//        <div className="container mt-4">
//            <h2>Manage Surveys</h2>
//            <button onClick={() => handleSurvey('students')} className="btn btn-primary">
//                Conduct Student Survey
//            </button>
//            <button onClick={() => handleSurvey('staff')} className="btn btn-secondary mt-2">
//                Conduct Staff Survey
//            </button>
//        </div>
//    );
//}

//export default ManageSurveys;

import React, { useState } from 'react';
import axios from 'axios';

const SurveyManager = () => {
    const [surveyTitle, setSurveyTitle] = useState('');
    const [reports, setReports] = useState([]);

    const createSurvey = async () => {
        try {
            await axios.post('http://localhost:8000/surveys/', { title: surveyTitle });
            alert('Survey created successfully!');
        } catch (error) {
            console.error('Failed to create survey', error);
        }
    };

    const fetchReports = async () => {
        try {
            const response = await axios.get('http://localhost:8000/survey-reports/');
            setReports(response.data);
        } catch (error) {
            console.error('Failed to fetch reports', error);
        }
    };

    return (
        <div className="container">
            <h2>Survey Management</h2>
            <div>
                <input type="text" value={surveyTitle} onChange={e => setSurveyTitle(e.target.value)} placeholder="Enter Survey Title" className="form-control" />
                <button onClick={createSurvey} className="btn btn-success">Create Survey</button>
            </div>
            <div>
                <button onClick={fetchReports} className="btn btn-primary">Load Reports</button>
                {reports.map(report => (
                    <div key={report.id} className="alert alert-info">
                        {report.title} - {report.result}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SurveyManager;
