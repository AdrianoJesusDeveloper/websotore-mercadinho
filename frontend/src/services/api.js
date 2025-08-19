import axios from 'axios';

const API = 'http://1217.0.0.1:8000/api/v1';

export const register = (data) => axios .post('${API}/accounts/register/', data);