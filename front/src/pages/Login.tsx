import { LockOutlined } from '@mui/icons-material'
import { Avatar, Button, Container, Grid, TextField, Typography } from '@mui/material'
import { Box } from '@mui/system'
import React from 'react'
import { useNavigate } from 'react-router'
import { useAuth } from '../context/auth_context'

export default function Login() {
    const navigate = useNavigate()
    const auth = useAuth()
    const [error, setError] = React.useState<string>()

    React.useEffect(
        React.useCallback(() => {
            if (auth.error?.detail) {
                setError(auth.error.detail as string)
            }
        }, [auth.error])
    )

    React.useEffect(
        React.useCallback(() => {
            if (auth.user) {
                navigate(`/`)
            }
        }, [auth.user])
    )

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault()
        const data = new FormData(event.currentTarget)

        const username = data.get('username')?.toString()
        const password = data.get('password')?.toString()

        if (username === undefined || password === undefined) {
            return
        }

        if (auth.login) {
            auth.login({ username, password })
        }
    }

    return (
        <Container component="main" maxWidth="xs">
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center'
                }}
            >
                <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                    <LockOutlined />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Login to your book club adventure
                </Typography>
                <Box component="form" onSubmit={handleSubmit} sx={{ mt: 3 }}>
                    <Grid container spacing={2}>
                        {error && (
                            <Grid item xs={12} textAlign="center" color="red" marginBottom={2}>
                                {error}
                            </Grid>
                        )}
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                id="username"
                                label="Username"
                                name="username"
                                autoComplete="username"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="password"
                                label="Password"
                                type="password"
                                id="password"
                                autoComplete="password"
                            />
                        </Grid>
                    </Grid>
                    <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
                        Login
                    </Button>
                </Box>
            </Box>
        </Container>
    )
}
