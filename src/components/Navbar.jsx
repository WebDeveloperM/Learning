import React from 'react';
import {IoIosNotificationsOutline} from "react-icons/io";
import {IoSettingsOutline} from "react-icons/io5";

function Navbar(props) {
    return (
        <nav className="navbar navbar-expand-lg">
            <div className="container-fluid">
                <div className={"navbar-brand"}>
                    <form className="d-flex" role="search">
                        <input className="form-control search-input" type="search"
                               placeholder="Search class, Documents, Activies ..." aria-label="Search"/>
                    </form>
                </div>
                <div className={"d-flex align-center g-10"}>
                    <IoIosNotificationsOutline className={"nav-icon is_disabled"}/>
                    <IoSettingsOutline className={"nav-icon is_disabled"}/>
                    <div className={"navbar-avatar is_disabled"}>
                        <img src="user.png" alt=""/>
                    </div>
                </div>
            </div>
        </nav>
    );
}

export default Navbar;