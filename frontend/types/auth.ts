export interface LoginRequest {
  userId: string;
  userPassword: string;
}

export interface LoginResponse {
  accessToken: string;
}
