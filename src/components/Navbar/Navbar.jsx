import React, {useContext} from 'react';
import 'bulma/css/bulma.css'
import {UserContext} from "../../App";
import {NavLink} from "react-router-dom";


function Navbar(props) {
    const {user, setUser} = useContext(UserContext)


    function logout() {
        localStorage.setItem('active', 'false')
        localStorage.setItem('jwt', '')
        setUser(prev => {
            return {...prev, active: false}
        })
    }

    return (
        <nav className='navbar'>
            <div className='navbar-start'>

            </div>
            <div className='navbar-end'>
                {user.active && user.jwt.length !== 0
                    ? <div className={'navbar-item buttons'}>
                        <NavLink to={'/basket'}>
                             <button className='button navbar-item is-primary'>Basket</button>
                        </NavLink>
                        <button className='button navbar-item is-danger' onClick={logout}>sign out</button>
                    </div>
                    : <div className='navbar-item buttons'>
                        <button className='button is-info'>
                            <NavLink to='/signup'>
                                sign Up
                            </NavLink>
                        </button>
                        <button className='button is-primary'>
                            <NavLink to={'/signin'}>
                                sign In
                            </NavLink>
                        </button>
                    </div>}


            </div>
        </nav>
    );
}

export default Navbar;