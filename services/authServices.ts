import type { LoginRequest, LoginResponse } from '@/types/auth';

import api from './api';

export const login = async (request: LoginRequest): Promise<LoginResponse> => {
  return await api.post('/auth/login', request);
};

export const logout = async (): Promise<null> => {
  return await api.post('/auth/logout');
};
