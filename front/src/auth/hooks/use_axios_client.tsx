import axios from 'axios'
import { useCallback, useEffect } from 'react'
export function useAxiosClient() {
    const tokens = auth?.tokens

    const client = axios.create({
        baseURL: 'http://localhost:8000',
        timeout: 1000
    })

    useEffect(
        useCallback(() => {
            if (auth?.tokens !== undefined) {
                client.defaults.headers.common[
                    'Authorization'
                ] = `Bearer ${auth.tokens.accessToken}`
            }
        }, [auth?.tokens])
    )

    return { client }
}
