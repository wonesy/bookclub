import * as React from 'react'
import * as auth from '../auth-provider'
import { useAsync } from '../util/hooks/use_async'

type AuthContextProps = {
    user?: string
    login?: (creds: { username: string; password: string }) => void
    children?: React.ReactNode
}

const AuthContext = React.createContext<AuthContextProps | undefined>(undefined)

function AuthProvider(props: AuthContextProps) {
    const { data: user, run, setData, isSuccess, isError, isIdle, isLoading } = useAsync()

    React.useEffect(() => {
        // get user from token in local storage, if present
        // do once per mount
        setData(auth.checkLoggedIn())
    }, [])

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
