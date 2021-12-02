import { createTheme, CssBaseline, ThemeProvider } from '@mui/material'
import { QueryClient, QueryClientProvider } from 'react-query'
import BookClubRoutes from './BookClubRoutes'

import { AuthProvider } from './context/auth_context'

const queryClient = new QueryClient()
const theme = createTheme()

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <ThemeProvider theme={theme}>
                <AuthProvider>
                    <CssBaseline />
                    <BookClubRoutes />
                </AuthProvider>
            </ThemeProvider>
        </QueryClientProvider>
    )
}

export default App
