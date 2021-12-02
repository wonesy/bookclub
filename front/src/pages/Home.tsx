import { Button } from '@mui/material'
import { useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../context/auth_context'

export default function Home() {
    const auth = useAuth()

    useEffect(() => {
        console.log(auth.user)
    }, [auth.user])

    return (
        <>
            <Button
                onClick={() => {
                    if (auth.logout) {
                        auth.logout()
                    }
                }}
            >
                Logout
            </Button>
            <Link to={'/login'}>Login</Link>
            <p>Home!</p>
        </>
    )
}
