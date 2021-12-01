import { useQuery } from 'react-query'
import { useAxiosClient } from '../auth/hooks/use_axios_client'
import { Member } from '../state/member'
import { useStore } from '../state/store'

const toMember = (data: Record<string, any>): Member => {
    return {
        username: data['username'],
        firstName: data['first_name'],
        lastName: data['last_name']
    } as Member
}

export function useMembers() {
    const { client } = useAxiosClient()
    const store = useStore()

    const getMembersRequest = async () => {
        const { data } = await client.get('/members')
        return (data || []).map(toMember)
    }

    return useQuery('getMembers', async () => getMembersRequest(), {
        onSuccess: store.addMemberDetails
    })
}
