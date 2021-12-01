import { QueryClient, QueryClientProvider } from 'react-query'
import { Routes, Route } from 'react-router-dom'
import { AuthProvider } from './auth/AuthProvider'
import Layout from './components/Layout'
import Home from './pages/Home'
import Login from './pages/Login'

const queryClient = new QueryClient()

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <AuthProvider>
                <Routes>
                    <Route path="/" element={<Layout />}>
                        <Route index element={<Home />} />
                        <Route path="login" element={<Login />} />
                    </Route>
                </Routes>
            </AuthProvider>
        </QueryClientProvider>
    )
}

export default App