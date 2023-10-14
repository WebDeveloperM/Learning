import React from 'react';
import {IoLogOut} from "react-icons/io5";
import Navbar from "./components/Navbar";
import {Route, Routes} from "react-router-dom";
import Home from "./pages/Home";
import Lessons from "./pages/Lessons";
import Statistics from "./pages/Statistics";
import Login from "./pages/Login";

function Main(props) {
    return (
        <div className={"row layout"}>
            <div className={"col-md-3 left-side"}>
                <div className={"left-side-list"}>
                    <ul>
                        <li>Home</li>
                        <li>Lessons</li>
                        <li>Statistics</li>
                        <li className={"soon-1"}>Coming soon...</li>
                        <li className={"soon-2"}>Coming soon...</li>
                        <li className={"soon-3"}>Coming soon...</li>
                    </ul>
                </div>
                <div className={"logout"}>
                    <button className={"logout-button"}>
                        <IoLogOut/>
                        logout
                    </button>
                </div>
            </div>
            <div className={"col-md-9 right-side"}>
                <Navbar/>
                <div className={"banner is_blur"}>
                    <div className={"banner-text"}>
                        <h1>Welcome back, Adelyone Iropadun</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus aliquam inventore
                            laboriosam praesentium veritatis. Assumenda facilis officia vel veritatis
                            voluptas!</p>
                    </div>
                    <div className={"banner-image"}>
                        <img src="banne.png" alt=""/>
                    </div>
                </div>
                <section className={"scrolling-block"}>
                    <Routes>
                        <Route path={"/"} element={<Home/>}/>
                        <Route path={"/lessons"} element={<Lessons/>}/>
                        <Route path={"/statistics"} element={<Statistics/>}/>
                        <Route path={"/login"} element={<Login/>}/>
                    </Routes>
                </section>
            </div>
        </div>
    );
}

export default Main;