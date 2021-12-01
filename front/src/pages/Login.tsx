import { useLogin } from '../auth/hooks/use_login'

export default function Login() {
    const login = useLogin()

    return (
        <div>
            <button onClick={async () => await login('wonesy', 'fakepassword')}>Login</button>
        </div>
    )
}
