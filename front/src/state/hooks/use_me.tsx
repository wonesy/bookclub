import { useAtom } from 'jotai'
import { useQuery } from 'react-query'
import { useAuthClient } from '../../context/auth_context'
import { Member } from '../member'
import { meAtom } from '../store'

export default function useMe() {
    const client = useAuthClient()
    const [_, setMe] = useAtom(meAtom)

    return useQuery<Member>('me', async () => {
        const { data } = await client('members/me', null)
        setMe({ ...data } as Member)
        return data
    })
}
