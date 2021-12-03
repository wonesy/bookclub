import { useQuery } from 'react-query'
import { useAuthClient } from '../../context/auth_context'

export default function useMe() {
    const client = useAuthClient()

    return useQuery('me', async () => await client('members/me', null))
}
