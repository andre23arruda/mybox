import React, { useState } from 'react'
import { useHistory } from 'react-router'

// utils
import { googleLogin, postApi } from '../../services/api'
import { title } from '../../utils'

// components
import InputPassword from '../../components/InputPassword'
import Footer from '../../components/Footer'
import GoogleLogin from 'react-google-login'

// styles and images
import './Login.scss'
import logo from '../../assets/logo.svg'


function Login() {
    title('Entrar')
    const history = useHistory()

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [showPassword, setShowPassword] = useState(false)

    async function responseGoogle(response) {
        const { token } = await googleLogin(response.accessToken)
        if (token) {
            localStorage.setItem('token', `JWT ${ token }`)
            history.push('/my-files')
        } else {
            alert(`Erro no login. Tente novamente`)
        }
    }

    async function formLogin(event) {
        event.preventDefault()
        const data = {
            username,
            password,
        }
        postApi(`login/`, data)
        .then(({data, response_status}) => {
            if (response_status >= 400) {
                alert(`Erro no login. Tente novamente`)
            } else if (200 < response_status < 300) {
                localStorage.setItem('token', `JWT ${ data.token }`)
                history.push('/my-files')
            }
        })
    }

    function validateForm() {
        return username && password
    }

    return (
        <div className="login-page">
            <form onSubmit={ formLogin }>
                <img
                    className="logo"
                    src={ logo }
                    alt="Mybox"
                />

                <input
                    type="text"
                    placeholder="Your username"
                    value={ username }
                    onChange={ e => setUsername(e.target.value) }
                />

                <InputPassword
                    password={ password }
                    setPassword={ setPassword }
                    showPassword={ showPassword }
                    setShowPassword={ setShowPassword }
                />

                <button
                    type="submit"
                    disabled={ !validateForm() }
                >
                    Entrar
                </button>

                <span className="divider">
                    <hr />
                    <b>OR</b>
                    <hr />
                </span>

                <div className="oauth-container">
                    <GoogleLogin
                        clientId={ process.env.REACT_APP_GOOGLE_ID }
                        buttonText="LOGIN WITH GOOGLE"
                        onSuccess={ responseGoogle }
                        onFailure={ responseGoogle }
                    />
                </div>
            </form>

            <Footer />
        </div>
    )
}

export default Login
