import React, {useContext, useState} from 'react';
import axios from "axios"
import {UserContext} from "../../App";

function SignUpForm(props) {
    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [cpassword, setCpassword] = useState('')
    const [data, setData] = useState(null)
    const { setUser } = useContext(UserContext)

    async function handleSubmit(event) {
        event.preventDefault()
        if (password === cpassword) {
             await axios.post('http://localhost:1337/api/auth/local/register', {
                        username: username,
                        email: email,
                        password: password
                    })
                .then(result => {
                    setData(result)
                    setUser( prev => {
                        return {
                            ...prev,
                            jwt: result.data.jwt,
                            active: true,
                            username: result.data.username,
                            id: result.data.id
                        }
                    } )
                    localStorage.setItem('active', 'true')
                    localStorage.setItem('jwt', result.data.jwt)
                    localStorage.setItem('user', JSON.stringify(result.data.user))
                }).catch(e => {
                    console.log(e)
                })
            return
        }
        alert('ваши пароли не совпадают')
    }

    return (
        <div className='box px-6 py-4'>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder='username'
                    className='input'
                    value={username}
                    onInput={e => setUsername(e.target.value)}
                    required={true}/>
                <input type="email"
                       placeholder='email'
                       className='input'
                       value={email}
                       onInput={e => setEmail(e.target.value)}
                       required={true}/>
                <input type="password"
                       placeholder='password'
                       className='input'
                       value={password}
                       onInput={e => setPassword(e.target.value)}
                       required={true}/>
                <input type="password"
                       placeholder='confirm password'
                       className='input'
                       value={cpassword}
                       onInput={e => setCpassword(e.target.value)}
                       required={true}/>
                <button className='button is-info'>Create Me</button>
            </form>
        </div>
    );
}

export default SignUpForm;