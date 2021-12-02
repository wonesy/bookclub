import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Layout from './components/Layout'

export default function BookClubRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Layout />}>
                <Route index element={<Home />} />
            </Route>
            <Route path="/login" element={<Login />} />
        </Routes>
    )
}
