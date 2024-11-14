'use client';

import type { LoginFormUserDataType } from '@/app/page';

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';

import { Button } from '@/components/ui/button';
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form';
import { Input } from '@/components/ui/input';


const formSchema = z.object({
  userId: z.string().min(1, {
    message: '1자 이상 입력해 주세요.',
  }),
  userPassword: z.string().min(1, {
    message: '1자 이상 입력해 주세요.',
  }),
});

type LoginFormProps = {
  onLoginSuccess: (userData: LoginFormUserDataType) => void;
};

export default function LoginForm({ onLoginSuccess }: LoginFormProps) {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      userId: '',
      userPassword: '',
    },
  });

  const onSubmit = (data: z.infer<typeof formSchema>) => {
    console.log('폼 데이터:', data);
    onLoginSuccess(data);
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="userId"
          render={({ field }) => (
            <FormItem>
              <FormLabel>아이디</FormLabel>
              <FormControl>
                <Input placeholder="아이디" {...field} autoComplete="username" />
              </FormControl>
              <FormDescription>아이디를 입력해 주세요.</FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="userPassword"
          render={({ field }) => (
            <FormItem>
              <FormLabel>비밀번호</FormLabel>
              <FormControl>
                <Input type="password" placeholder="••••••••" {...field} autoComplete="current-password" />
              </FormControl>
              <FormDescription>비밀번호를 입력해 주세요.</FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit">로그인</Button>
      </form>
    </Form>
  );
}
