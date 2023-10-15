import React, {useEffect, useState} from 'react';
import axios from "axios";
import {BASE_API, MAIN, SCIENCE} from "../urls";
import "../assets/css/lessons.css"

function Lessons(props) {
    const [data, setData] = useState([])
    useEffect(() => {
        axios.get(BASE_API + MAIN + SCIENCE).then(res => {
            setData(res.data)
        }).catch(res => {
            console.log(res)
        })
    }, []);

    return (
        <div className={"lessons"}>
            {data && data.map(value => <div className={"lesson-item"}>
                <img src={"http://localhost:8000" + value.photo} alt=""/>
                <h1>{value.title}</h1>
            </div>)}
        </div>
    );
}

export default Lessons;