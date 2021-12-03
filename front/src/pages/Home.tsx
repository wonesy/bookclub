import { Box, Container, Grid, Paper, Toolbar } from '@mui/material'
import { useEffect } from 'react'
import { useAuth } from '../context/auth_context'
import useMe from '../state/hooks/use_me'

export default function Home() {
    const auth = useAuth()

    const { data } = useMe()

    useEffect(() => {
        console.log(auth.user)
    }, [auth.user])

    useEffect(() => {
        console.log(data)
    }, [data])

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
