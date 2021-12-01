import { useAuth } from '../context/auth_context'

export default function Login() {
    const auth = useAuth()

    console.log(auth.user)

    return (
        <div>
            <button
                onClick={async () =>
                    await auth.login!({ username: 'wonesy', password: 'fakepassword' })
                }
            >
                Login
            </button>
        </div>
    )
}
