import { useAuth } from '../auth/AuthProvider'

export default function Login() {
    const auth = useAuth()
    return (
        <div>
            <button onClick={() => auth?.login('wonesy', 'fakepassword')}>Login</button>
        </div>
    )
}
