import axios from 'axios'
import { useMutation } from 'react-query'
import { useTokens } from '../../state/hooks/use_tokens'

export function useLogin() {
    const { setTokens } = useTokens()

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
            onSuccess: tokenResponse => {
                setTokens({
                    accessToken: tokenResponse['access_token'],
                    refreshToken: tokenResponse['refresh_token']
                })
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

    return login
}
