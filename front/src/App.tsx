import { ChakraProvider } from '@chakra-ui/react'
import { QueryClient, QueryClientProvider } from 'react-query'
import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import { AuthProvider } from './context/auth_context'
import Home from './pages/Home'
import Login from './pages/Login'

const queryClient = new QueryClient()

function App() {
    return (
        <ChakraProvider>
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
        </ChakraProvider>
    )
}

export default App
