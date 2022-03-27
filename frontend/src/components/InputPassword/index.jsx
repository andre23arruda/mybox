import React from 'react'

// images
import './InputPassword.scss'
import eye from '../../assets/eye.svg'
import eyeSlash from '../../assets/eye-slash.svg'


function InputPassword({ password, setPassword, showPassword, setShowPassword }) {
    return (
        <div className="password-container">
            <input
                type={ showPassword ? 'text' : 'password' }
                placeholder="********"
                value={ password }
                onChange={ e => setPassword(e.target.value) }
            />

            <span className="show-password" onClick={ () => setShowPassword(!showPassword) }>
                <img src={ showPassword ? eye : eyeSlash } width="25" alt="Show password" />
            </span>
        </div>
    )
}

export default InputPassword
