import React, {createContext, useContext, useState} from 'react';
import "./assets/css/main.css"
import {Route, Routes, useLocation} from "react-router-dom";
import Home from "./pages/Home";
import axios from "axios";
import {BASE_API, SIGN_IN, USERS} from "./urls";
import Lessons from "./pages/Lessons";

export const TYPES = {
    teacher: "Teacher",
    student: "Student"
}
export const BASE_CONTEXT = createContext(null)

function App(props) {
    const location = useLocation()
    const [hidden, setHidden] = useState(null)
    const [baseState, setBaseState] = useState({
        user: null,
        active: false,
        type: TYPES.student
    })
    const [password, setPassword] = useState("")
    const [email, setEmail] = useState("")

    function handle(e) {
        e.preventDefault()
        axios.post(BASE_API + USERS + SIGN_IN, {
            email, password, type: TYPES.student
        })
            .then(res => {
                setBaseState(prevState => ({...prevState, active: true}))
                console.log(res)
            })
            .catch(res => console.log(res))
    }

    return (
        <BASE_CONTEXT.Provider value={{baseState, setBaseState}}>
            {!baseState.active
                ? <div className={"welcome"}>
                    <div className={"welcome-left"}>
                        {hidden === "left" ? <form onSubmit={e => handle(e)} className={"welcome-form"}>
                            <input onInput={e => setEmail(e.target.value)} className={"input"} type="email"
                                   placeholder={"email"}/>
                            <input onInput={e => setPassword(e.target.value)} className={"input"} type="password"
                                   placeholder={"password"}/>
                            <input className={"button"} type="submit"/>
                        </form> : <button onClick={e => {
                            setHidden("left")
                        }}>Student
                        </button>}
                    </div>
                    <div className={"welcome-right"}>
                        {hidden === "right" ? <form onSubmit={e => handle(e)} className={"welcome-form"}>
                            <input onInput={e => setEmail(e.target.value)} className={"input"} type="email"
                                   placeholder={"email"}/>
                            <input onInput={e => setPassword(e.target.value)} className={"input"} type="password"
                                   placeholder={"password"}/>
                            <input className={"button"} type="submit"/>
                        </form> : <button onClick={e => {
                            setHidden("right")
                        }}>Teacher
                        </button>}
                    </div>
                </div> : <Home/>}
        </BASE_CONTEXT.Provider>

    );
}

export default App;