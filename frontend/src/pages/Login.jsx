import React, {useContext, useState} from 'react';
import {useLocation, useNavigate, useNavigation} from "react-router-dom";
import {BASE_CONTEXT} from "../App";
import axios from "axios";
import {BASE_API, LOGIN} from "../urls";


const TYPE = {
    teacher: "Teacher",
    people: "Student"
}

function Login(props) {
    const location = useLocation()
    const navigate = useNavigate()
    const [type, setType] = useState()
    const [values, setValues] = useState({
        email: "",
        phone: "",
        type: "",
        password: ""
    })

    const {user, setUser} = useContext(BASE_CONTEXT)

    async function login_handle(event) {
        event.preventDefault()
        await axios.post(BASE_API + LOGIN, values).then(res => {
            console.log(res)
        }).catch(e => {
            console.log(e)
        })

    }

    return (
        <section>
            {
                location.pathname === "/login/auth"
                    ? user.type === TYPE.teacher ? <section className={"login login-back"}>
                        <form className={"login-form"} onSubmit={login_handle}>
                            <input type="text" onInput={e => setValues(prev => {
                                return {...prev, phone: e.target.value}
                            })} className={"form-control"} placeholder={"telephone number"}/>
                            <input type="email" onInput={e => setValues(prev => {
                                return {...prev, email: e.target.value}
                            })} className={"form-control"} placeholder={"email"}/>
                            <input onInput={e => setValues(prev => {
                                return {...prev, password: e.target.value}
                            })} type="password" className={"form-control"} placeholder={"password"}/>
                            <button className={"login-button small"}>Login</button>
                        </form>
                    </section> : <section className={"login login-back people"}>
                        <form className={"login-form people-form"} onSubmit={login_handle}>
                            <input type="text" onInput={e => setValues(prev => {
                                return {...prev, phone: e.target.value}
                            })} className={"form-control"} placeholder={"telephone number"}/>
                            <input type="email" onInput={e => setValues(prev => {
                                return {...prev, email: e.target.value}
                            })} className={"form-control"} placeholder={"email"}/>
                            <input onInput={e => setValues(prev => {
                                return {...prev, password: e.target.value}
                            })} type="password" className={"form-control"} placeholder={"password"}/>
                            <button className={"login-button small button-white"}>Login</button>
                        </form>
                    </section>
                    : <section className={"login"}>
                        <div className="login-left">
                            <button className="login-button" onClick={e => {
                                setType(TYPE.people)
                                setUser(prevent => {
                                    return {...prevent, type: TYPE.people}
                                })
                                navigate("login/auth")
                            }}>{TYPE.people}</button>
                        </div>
                        <div className="login-right">
                            <button className="login-button button-white" onClick={e => {
                                setType(TYPE.teacher)
                                setUser(prevent => {
                                    return {...prevent, type: TYPE.teacher}
                                })
                                navigate("login/auth")
                            }}>{TYPE.teacher}</button>
                        </div>
                    </section>
            }
        </section>
    );
}

export default Login;