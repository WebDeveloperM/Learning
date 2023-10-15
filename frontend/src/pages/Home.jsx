import React, {useContext} from 'react';
import {BASE_CONTEXT} from "../App";
import "../assets/css/home.css"
import {NavLink, Route, Routes, useLocation} from "react-router-dom";
import Lessons from "./Lessons";
import Results from "./Results";
import Test from "./Test";

function Home(props) {
    const location = useLocation()
    const {baseState} = useContext(BASE_CONTEXT)


    return (
        <div className={"home"}>
            <div className="side-bar">
                <div className={"side-bar-logo"}>
                    <img src="logo.svg" alt=""/>
                    <div className={"side-bar-user"}>
                        <img src="user.png" alt=""/>
                        <div>
                            <h4>Грозный Иван Васильевич</h4>
                            <p>example@gmail.com</p>
                        </div>
                    </div>
                </div>
                <div className={"side-bar-links"}>
                    <NavLink to={"/"} className={location.pathname === "/" && "active"}>Home</NavLink>
                    <NavLink to={"/lessons"} className={location.pathname === "/lessons" && "active"}>Lessons</NavLink>
                    <NavLink to={"/result"} className={location.pathname === "/result" && "active"}>Results</NavLink>
                </div>
                <div className={"side-bar-logout"}>
                    <span>Logout</span>
                </div>
            </div>
            <div className="content">
                {location.pathname === "/" && <div className={"home-inner"}>
                    <h1>Welcome to the «iLearn» Personal Account!</h1>
                    <h3>As a tutor or student, you can make a schedule here, send
                        homework or store information, and much more.</h3>
                    <button>About project</button>
                    <img src="banner.png" alt=""/>
                </div>}
                <Routes>
                    <Route path={"/lessons"} element={<Lessons/>}/>
                    {/*<Route path={"/lessons/:id"} element={<Lessons/>}/>*/}
                    {/*<Route path={"/lessons/:id/test"} element={<Lessons/>}/>*/}
                    <Route path={"/results"} element={<Results/>}/>
                    <Route path={"/test/:science_id"} element={<Test/>}/>
                </Routes>
            </div>
        </div>
    );
}

export default Home;