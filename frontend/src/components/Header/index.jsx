import React from 'react'

// styles and images
import './Header.scss'
import logo from '../../assets/logo.svg'


function Header({ title }) {
    return (
        <div className="header">
            <img className="logo" src={ logo } alt="Rocketbox" />
            <h2>{ title }</h2>
        </div>
    )
}

export default Header