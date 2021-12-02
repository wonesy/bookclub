import { useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../context/auth_context'

export default function Home() {
    const auth = useAuth()

    useEffect(() => {
        console.log(auth.user)
    })

    return (
        <>
            <Link to={'/login'}>Login</Link>
            <p>Home!</p>
        </>
    )
}
