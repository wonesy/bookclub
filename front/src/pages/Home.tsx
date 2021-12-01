import { useMembers } from '../api/use_members'

export default function Home() {
    const members = useMembers()

    return (
        <>
            <p>Home!</p>
        </>
    )
}
