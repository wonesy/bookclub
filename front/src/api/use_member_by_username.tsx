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

export function useMemberByUsername(username: string) {
    const { client } = useAxiosClient()
    const store = useStore()

    const getMemberRequest = async () => {
        const { data } = await client.get(`/members/${username}`)
        return toMember(data)
    }

    return useQuery('getMemberByUsername', async () => getMemberRequest(), {
        onSuccess: store.addMemberDetails
    })
}
