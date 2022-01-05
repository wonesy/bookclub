import React from 'react'
import { Outlet, useNavigate } from 'react-router-dom'
import { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar'
import {
    Drawer as MuiDrawer,
    AppBar as MuiAppBar,
    styled,
    Toolbar,
    IconButton,
    Typography,
    Badge,
    Divider,
    List,
    ListItem,
    ListItemIcon,
    ListItemText
} from '@mui/material'
import { ChevronLeft, Menu, Notifications, MenuBook, EmojiEvents } from '@mui/icons-material'
import { Box } from '@mui/system'
import { useAuth } from '../context/auth_context'

export type RouteDefinition = {
    display: string
    link: string
    icon: React.ReactElement
}

export const sideBarRoutes: RouteDefinition[] = [
    { display: 'My Club', link: '/club', icon: <MenuBook /> },
    { display: 'Awards', link: '/awards', icon: <EmojiEvents /> }
]

const drawerWidth: number = 240

interface AppBarProps extends MuiAppBarProps {
    open?: boolean
}

const AppBar = styled(MuiAppBar, {
    shouldForwardProp: prop => prop !== 'open'
})<AppBarProps>(({ theme, open }) => ({
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen
    }),
    ...(open && {
        marginLeft: drawerWidth,
        width: `calc(100% - ${drawerWidth}px)`,
        transition: theme.transitions.create(['width', 'margin'], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.enteringScreen
        })
    })
}))

const Drawer = styled(MuiDrawer, { shouldForwardProp: prop => prop !== 'open' })(
    ({ theme, open }) => ({
        '& .MuiDrawer-paper': {
            position: 'relative',
            whiteSpace: 'nowrap',
            width: drawerWidth,
            transition: theme.transitions.create('width', {
                easing: theme.transitions.easing.sharp,
                duration: theme.transitions.duration.enteringScreen
            }),
            boxSizing: 'border-box',
            ...(!open && {
                overflowX: 'hidden',
                transition: theme.transitions.create('width', {
                    easing: theme.transitions.easing.sharp,
                    duration: theme.transitions.duration.leavingScreen
                }),
                width: theme.spacing(7),
                [theme.breakpoints.up('sm')]: {
                    width: theme.spacing(9)
                }
            })
        }
    })
)

function DashboardContent() {
    const [open, setOpen] = React.useState(true)
    const toggleDrawer = () => {
        setOpen(!open)
    }

    return (
        <Box sx={{ display: 'flex' }}>
            <AppBar position="absolute" open={open}>
                <Toolbar
                    sx={{
                        pr: '24px' // keep right padding when drawer closed
                    }}
                >
                    <IconButton
                        edge="start"
                        color="inherit"
                        aria-label="open drawer"
                        onClick={toggleDrawer}
                        sx={{
                            marginRight: '36px',
                            ...(open && { display: 'none' })
                        }}
                    >
                        <Menu />
                    </IconButton>
                    <Typography
                        component="h1"
                        variant="h6"
                        color="inherit"
                        noWrap
                        sx={{ flexGrow: 1 }}
                    >
                        Dashboard
                    </Typography>
                    <IconButton color="inherit">
                        <Badge badgeContent={4} color="secondary">
                            <Notifications />
                        </Badge>
                    </IconButton>
                </Toolbar>
            </AppBar>
            <Drawer variant="permanent" open={open}>
                <Toolbar
                    sx={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'flex-end',
                        px: [1]
                    }}
                >
                    <IconButton onClick={toggleDrawer}>
                        <ChevronLeft />
                    </IconButton>
                </Toolbar>
                <Divider />
                <List>
                    {sideBarRoutes.map(r => (
                        <ListItem button key={r.link}>
                            <ListItemIcon>{r.icon}</ListItemIcon>
                            <ListItemText primary={r.display} />
                        </ListItem>
                    ))}
                </List>
            </Drawer>
            <Box
                component="main"
                sx={{
                    backgroundColor: theme =>
                        theme.palette.mode === 'light'
                            ? theme.palette.grey[100]
                            : theme.palette.grey[900],
                    flexGrow: 1,
                    height: '100vh',
                    overflow: 'auto'
                }}
            >
                <Toolbar />
                <Outlet />
            </Box>
        </Box>
    )
}

export default function Layout() {
    const { user } = useAuth()
    const navigate = useNavigate()

    React.useEffect(
        React.useCallback(() => {
            if (!user || !user.username) navigate('/login')
        }, [user]),
        []
    )

    return user?.username ? <DashboardContent /> : null
}
