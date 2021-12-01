import jwt_decode from 'jwt-decode'
import { useCallback, useEffect } from 'react'
import { useTokens } from '../../state/hooks/use_tokens'
import { useStore } from '../../state/store'
import { useAxiosClient } from './use_axios_client'

export function useAuth() {
    const store = useStore()
    const { tokens } = useTokens()
    const { client } = useAxiosClient()

    useEffect(
        useCallback(() => {
            if (tokens?.accessToken !== undefined) {
                const decodedToken: Record<string, string> = jwt_decode(tokens.accessToken)
                const username = decodedToken['sub']

                console.log(username)
                const { data } = client.get(`/members/${username}`)
            }
        }, [tokens, client])
    )
}
