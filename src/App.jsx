import React, {createContext, useEffect, useState} from 'react';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Navbar from "./components/Navbar/Navbar";
import Footer from "./components/Footer/Footer";
import HomePage from "./pages/HomePage";
import SignUp from "./pages/SignUp";
import SignIn from "./pages/SignIn";
import ProductDetail from "./pages/ProductDetail";
import {ToastContainer} from "react-toastify";
import Cart from "./pages/Cart";
import Checkout from "./pages/Checkout";

export const UserContext = createContext(null)


function App(props) {
    const [user, setUser] = useState({
        jwt: '',
        active: false,
        user: {},
    })

    useEffect( _ => {
        setUser(prev => {
            return {
                ...prev,
                active: Boolean(localStorage.getItem('active')),
                user: JSON.parse(localStorage.getItem('user'))
            }
        })
    }, [] )

    return (
        <React.StrictMode>
            <BrowserRouter>
                <UserContext.Provider value={ {user, setUser} }>
                    <ToastContainer></ToastContainer>
                    <Navbar/>
                    <Routes>
                        <Route path='/' element={<HomePage/>} />
                        <Route path='/signup' element={<SignUp/>}/>
                        <Route path='/signin' element={<SignIn/>}/>
                        <Route path='/product/:id' element={<ProductDetail/>}/>
                        <Route path='/basket' element={<Cart/>}/>
                        <Route path='/checkout' element={<Checkout/>}/>
                    </Routes>
                    <Footer/>
                </UserContext.Provider>
            </BrowserRouter>
        </React.StrictMode>
    );
}

export default App;