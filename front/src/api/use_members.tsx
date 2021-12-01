import { useQuery } from 'react-query'
import { Member } from '../state/member'
import { useStore } from '../state/store'
import { apiClient } from './api_client'

const toMember = (data: Record<string, any>): Member => {
    return {
        username: data['username'],
        firstName: data['first_name'],
        lastName: data['last_name']
    } as Member
}

export function useMembers() {
    const store = useStore()

    const getMembersRequest = async () => {
        const data = await apiClient('/members')
        return (data || []).map(toMember)
    }

    return useQuery('getMembers', async () => getMembersRequest(), {
        onSuccess: store.addMemberDetails
    })
}
