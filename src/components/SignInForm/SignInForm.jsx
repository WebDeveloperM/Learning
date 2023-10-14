import React, {useContext, useEffect, useState} from 'react';
import axios from "axios";
import {UserContext} from "../../App";

function SignInForm(props) {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState(false)
    const {setUser} = useContext(UserContext)

    useEffect( _ => {
        error && alert('Email или пароль не верный')
    }, [error])

    async function handleSubmit(e) {
        e.preventDefault()
        if (email && password) {
            await axios.post('http://localhost:1337/api/auth/local', {
                identifier: email,
                password: password,
            }).then(
                res => {
                    document.cookie = `jwt=${res.data.jwt}`
                    document.cookie = `active=${true}`
                    localStorage.setItem('active', 'true')
                    localStorage.setItem('user', JSON.stringify(res.data))
                    setUser( prev => {
                        return {
                            ...prev,
                            jwt: res.data.jwt,
                            active: true
                        }
                    } )
                }
            ).catch( e => setError(true) )
            setEmail('')
            setPassword('')
            return
        }
        alert('Заполните поля')
    }

    return (
        <div className='column is-5 box px-6 py-4'>
            <form action="" onSubmit={handleSubmit}>
                <input className='input' type="email" onInput={ event => setEmail(event.target.value)} value={email} placeholder='username'/>
                <input className='input' type="password" onInput={ event => setPassword(event.target.value)} value={password}  placeholder='password'/>
                <button className='button is-info'>Login</button>
            </form>
        </div>
    );
}

export default SignInForm;