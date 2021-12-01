import axios from 'axios'
import { useTokens } from '../../state/hooks/use_tokens'

export function useAxiosClient() {
    const { tokens } = useTokens()

    const client = axios.create({
        baseURL: 'http://localhost:8000',
        timeout: 3000,
        headers: {
            'content-type': 'application/json',
            authorization: tokens?.accessToken ? `Bearer ${tokens.accessToken}` : ''
        }
    })

    return { client }
}
