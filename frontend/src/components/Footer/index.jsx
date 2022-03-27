import React from 'react'

// styles and images
import './Footer.scss'


function Footer(){
    return (
        <footer className="page-footer">
            &copy;{ new Date().getFullYear() } ²Arruda. Todos os direitos reservados.
        </footer>
    )
}

export default Footer