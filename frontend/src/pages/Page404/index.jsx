import React from 'react'
import { Link } from 'react-router-dom'

// utils
import { title } from '../../utils'

// images and styles
import './Page404.scss'


function Page404() {
    title('Página não encontrada')

    return (
        <div className="container-404">
            <h1>
                Ooops! <br />
                Parece que essa página não existe
            </h1>

            <Link className="back-link" to='/my-files'>
                Voltar
            </Link>
        </div>
    )
}

export default Page404
