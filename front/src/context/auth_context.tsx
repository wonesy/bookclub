import * as React from 'react'
import { apiClient } from '../api/api_client'
import * as auth from '../auth-provider'
import { Member } from '../state/member'
import { useAsync } from '../util/hooks/use_async'
import { toMember } from '../util/treats'

async function initAppData() {
    const token = await auth.getToken()

    if (token) {
        const data = apiClient('members/me', undefined, token)
        console.log(data)
        return data
    }

    return null
}

type AuthContextProps = {
    user?: string
    login?: (creds: { username: string; password: string }) => void
    children?: React.ReactNode
}

const AuthContext = React.createContext<AuthContextProps | undefined>(undefined)

function AuthProvider(props: AuthContextProps) {
    const { data: user, run, setData, isSuccess, isError, isIdle, isLoading } = useAsync()

    React.useEffect(() => {
        const initAppPromise = initAppData()
        run(initAppPromise, toMember)
    }, [user])

    const login = React.useCallback(
        (creds: { username: string; password: string }) => {
            auth.login(creds).then(user => setData(user))
        },
        [setData]
    )

    const value = React.useMemo(() => ({ user, login }), [login, user])

    // if loading... spinner

    // if error... full page error

    // if success...
    return <AuthContext.Provider value={value}>{props.children}</AuthContext.Provider>
}

function useAuth() {
    const context = React.useContext(AuthContext)
    if (context === undefined) {
        throw new Error(`useAuth must be used within a AuthProvider`)
    }
    return context
}

// function useClient() {
//     const accessToken = auth.getToken()
//     return React.useCallback(
//         async (endpoint, data) => apiClient(endpoint, data, await accessToken),
//         [accessToken]
//     )
// }

export { AuthProvider, useAuth }
