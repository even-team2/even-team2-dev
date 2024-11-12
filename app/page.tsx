'use client';

import { useState } from 'react';

import LoginForm from '@/components/login/LoginForm';
import { Button } from '@/components/ui/button';
import axiosInstance from '@/lib/axios';

export type LoginFormUserDataType = { userId: string; userPassword: string };

export default function Home() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState<{ userId: string } | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleLogin = async (userData: LoginFormUserDataType) => {
    // TODO: 실제 엔드포인트로 변경
    const response = await axiosInstance.post('/api/login', {
      userId: userData.userId,
      userPassword: userData.userPassword,
    });

    if (response.status === 200 && response.data) {
      setUser({ userId: response.data.userId });
      setIsLoggedIn(true);
      setError(null);
    }
  };

  const handleLogout = () => {
    setUser(null);
    setIsLoggedIn(false);
    setError(null);
  };

  return (
    <main className="flex min-h-screen items-center justify-center">
      <section className="w-full max-w-md px-4">
        {isLoggedIn && user ? (
          <div className="space-y-4 text-center">
            <h2 className="text-xl font-semibold">아이디: {user.userId}</h2>
            <Button onClick={handleLogout}>로그아웃</Button>
          </div>
        ) : (
          <>
            {error && <p className="text-center text-red-500">{error}</p>}
            <LoginForm onLoginSuccess={handleLogin} />
          </>
        )}
      </section>
    </main>
  );
}
