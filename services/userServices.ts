import type { FetchUserInfoResponse } from '@/types/user';

import api from './api';

export const fetchUserInfo = async (): Promise<FetchUserInfoResponse> => {
  return await api.get('/users/me');
};
