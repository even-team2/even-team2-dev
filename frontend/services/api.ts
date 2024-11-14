import axios from 'axios';

import { toCamelCase, toSnakeCase } from '@/utils/caseConverter';
import { tokenStorage } from '@/utils/tokenStorage';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(
  (config) => {
    const token = tokenStorage.getToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    if (config.data && typeof config.data === 'object') {
      config.data = toSnakeCase(config.data);
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

api.interceptors.response.use(
  (response) => {
    const { data } = response;
    if (data?.success) {
      return data?.data ? toCamelCase(data?.data) : true;
    } else {
      // TODO: 공통 에러 상태 코드 추가 처리
      return Promise.reject(new Error(data?.message || 'Unknown error occurred'));
    }
  },
  (error) => {
    if (!error.response) {
      return Promise.reject(new Error('Network error occurred'));
    }

    const status = error.response.status;
    const errorMessage = error.response.data?.message || 'An error occurred';

    if (status === 401) {
      // TODO: 토큰 갱신
      return Promise.reject(new Error('Unauthorized'));
    } else if (status === 403) {
      return Promise.reject(new Error('Forbidden'));
    } else if (status === 404) {
      return Promise.reject(new Error('Not Found'));
    } else if (status >= 500) {
      return Promise.reject(new Error('Server error occurred'));
    } else {
      return Promise.reject(new Error(errorMessage));
    }
  },
);

export default api;
