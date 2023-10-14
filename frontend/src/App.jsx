import {createContext, useState} from "react";
import "bootstrap/dist/css/bootstrap.css"
import {BrowserRouter} from "react-router-dom";
import "./assets/css/index.css"
import Login from "./pages/Login";
import Main from "./Main";

export const BASE_CONTEXT = createContext(null)

function App() {
    const [user, setUser] = useState({
        active: true,
        user: null,
        type: null
    })


    return (
        <BrowserRouter>
            <BASE_CONTEXT.Provider value={{user, setUser}}>
                {
                    user.active ? <Main/> : <Login/>
                }
            </BASE_CONTEXT.Provider>
        </BrowserRouter>
    );
}


export default App;
