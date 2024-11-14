'use client';

import type { LoginRequest } from '@/types/auth';
import type { FetchUserInfoResponse } from '@/types/user';

import { useEffect, useState } from 'react';

import LoginForm from '@/components/login/LoginForm';
import { Button } from '@/components/ui/button';
import { login, logout } from '@/services/authServices';
import { fetchUserInfo } from '@/services/userServices';
import { getErrorMessage } from '@/utils/errorHandler';
import { tokenStorage } from '@/utils/tokenStorage';

export default function Home() {
  const [user, setUser] = useState<FetchUserInfoResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isInitializing, setIsInitializing] = useState<boolean>(true);

  const handleLogin = async (userData: LoginRequest) => {
    setIsLoading(true);
    try {
      const response = await login(userData);

      if (response?.accessToken) {
        tokenStorage.setToken(response.accessToken);
        await getUserInfo();
      }
    } catch (error) {
      setError(getErrorMessage(error));
    } finally {
      setIsLoading(false);
    }
  };

  const handleLogout = async () => {
    setIsLoading(true);
    try {
      await logout();
      setUser(null);
      setError(null);
      tokenStorage.removeToken();
    } catch (error) {
      setError(getErrorMessage(error));
    } finally {
      setIsLoading(false);
    }
  };

  const getUserInfo = async () => {
    try {
      const response = await fetchUserInfo();
      setUser(response);
      setError(null);
    } catch (error) {
      tokenStorage.removeToken();
      setUser(null);
      setError(getErrorMessage(error));
    }
  };

  useEffect(() => {
    const initialize = async () => {
      const token = tokenStorage.getToken();
      if (token) {
        await getUserInfo();
      }
      setIsInitializing(false);
    };
    initialize();
  }, []);

  return (
    <main className="flex min-h-screen items-center justify-center">
      <section className="w-full max-w-md px-4">
        {isLoading || isInitializing ? (
          <div className="flex items-center justify-center">
            <div className="h-12 w-12 animate-spin rounded-full border-b-4 border-t-4 border-blue-500"></div>
          </div>
        ) : user ? (
          <div className="space-y-4 text-center">
            <h2 className="text-xl font-semibold">userId: {user.userId}</h2>
            <h2 className="text-xl font-semibold">uuid: {user.uuid}</h2>
            <Button onClick={handleLogout}>로그아웃</Button>
          </div>
        ) : (
          <>
            {error && <p className="text-center text-red-500">{error}</p>}
            <LoginForm onSubmit={handleLogin} />
          </>
        )}
      </section>
    </main>
  );
}
