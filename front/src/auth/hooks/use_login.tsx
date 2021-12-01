import axios from 'axios'
import { useMutation } from 'react-query'
import { LOCAL_STORAGE_TOKEN_KEY } from '..'

export function useLogin() {
    const loginRequest = async (username: string, password: string): Promise<any> => {
        const { data } = await axios.post('http://localhost:8000/auth/login', {
            username,
            password
        })
        return data
    }

    const loginMutation = useMutation(
        async ({ username, password }: { username: string; password: string }) =>
            loginRequest(username, password),
        {
            onSuccess: data => {
                console.log(data)
                window.localStorage.setItem(LOCAL_STORAGE_TOKEN_KEY, JSON.stringify(data))
            },
            onError: (err: any) => {
                if (err.response) {
                    console.error(err.response.data)
                }
            }
        }
    )

    const login = async (username: string, password: string) =>
        loginMutation.mutateAsync({ username, password })

    return { login }
}
