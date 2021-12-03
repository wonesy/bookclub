import { Box, Button, Container, Grid, Paper, Toolbar } from '@mui/material'
import { useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../context/auth_context'

export default function Home() {
    const auth = useAuth()

    useEffect(() => {
        console.log(auth.user)
    }, [auth.user])

    return (
        <Box
            component="main"
            sx={{
                backgroundColor: (theme: any) =>
                    theme.palette.mode === 'light'
                        ? theme.palette.grey[100]
                        : theme.palette.grey[900],
                flexGrow: 1,
                height: '100vh',
                overflow: 'auto'
            }}
        >
            <Toolbar />
            <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
                <Grid container spacing={3}>
                    {/* Chart */}
                    <Grid item xs={12} md={8} lg={9}>
                        <Paper
                            sx={{
                                p: 2,
                                display: 'flex',
                                flexDirection: 'column',
                                height: 240
                            }}
                        >
                            {/* <Chart /> */}
                            Chart
                        </Paper>
                    </Grid>
                    {/* Recent Deposits */}
                    <Grid item xs={12} md={4} lg={3}>
                        <Paper
                            sx={{
                                p: 2,
                                display: 'flex',
                                flexDirection: 'column',
                                height: 240
                            }}
                        >
                            {/* <Deposits /> */}
                            Deposits
                        </Paper>
                    </Grid>
                    {/* Recent Orders */}
                    <Grid item xs={12}>
                        <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                            {/* <Orders /> */}
                            Orders
                        </Paper>
                    </Grid>
                </Grid>
            </Container>
        </Box>
    )
}
