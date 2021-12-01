import { useAxiosClient } from '../auth/hooks/use_axios_client'
import { useMembers } from '../state/hooks/use_member'

export default function Home() {
    const x = useMembers()

    return (
        <>
            <p>Home!</p>
        </>
    )
}
