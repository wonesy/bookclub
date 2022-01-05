import { useQuery } from 'react-query'
import { useAuthClient } from '../context/auth_context'

type ClubInfoProps = {
    id: number
}

export function useClubInfo({ id }: ClubInfoProps) {
    const client = useAuthClient()

    return useQuery('club_info', async () => await client(`clubs/${id}`, null))
}
