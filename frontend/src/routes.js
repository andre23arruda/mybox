import React from 'react'
import { BrowserRouter, Redirect, Route } from 'react-router-dom'

// pages
import Login from './pages/Login'
import Main from './pages/Main'
import Page404 from './pages/Page404'


function Routes(){
    return (
        <BrowserRouter>
            <Route exact path="/">
                <Redirect to="/my-files" />
            </Route>

            <Route exact path='/login' component={ Login } />

            <Route exact path='/my-files' component={ Main } />

            <Route component={ Page404 } />
        </BrowserRouter>
    )
}

export default Routes
