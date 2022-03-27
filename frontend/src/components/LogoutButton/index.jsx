import React from 'react'
import { useHistory } from 'react-router-dom'

// styles and images
import './LogoutButton.scss'
import logout from '../../assets/logout.svg'



function LogoutButton() {
    const history = useHistory()

    function handleLogout() {
        localStorage.setItem('token', '')
        history.push('/login')
    }

    return (
        <div className="logout-button">
            <button type="button" onClick={ handleLogout }>
                <img className="icon" src={ logout } alt="Logout" />
            </button>
        </div>
    )
}

export default LogoutButton