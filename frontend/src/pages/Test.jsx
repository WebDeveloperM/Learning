import React, {useEffect, useState} from 'react';
import "../assets/css/test.css"
import {useParams} from "react-router-dom";

const tests = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const questions = [
    {
        id: 1,
        title: "1+1=?",
        options: [
            {
                id: 1,
                title: "3",
                correct: false,
            },
            {
                id: 2,
                title: "5",
                correct: false,
            },
            {
                id: 3,
                title: "4",
                correct: true,
            },
            {
                id: 4,
                title: "7",
                correct: false,
            }
        ]
    }
]

function Test(props) {
    const [select, setSelect] = useState()
    const {science_id} = useParams()

    useEffect(() => {

    }, []);

    return (
        <section className={'test'}>
            <div className={"test-side-bar"}>
                <div className={"test-name"}>
                    Mathematics
                </div>
                {tests.map(value => <div onClick={e => {
                }} className={"test-item"}>
                    {value}. Lorem ipsum dolor.
                </div>)}
            </div>
            <div className={"test-content"}>
                <h1>Generalization for the 3rd quarter</h1>
                <div style={{width: "70%"}}>
                    <div className={"test-question"}>
                        1. question
                        <br/>
                        <b>1. How many times do I need to increase
                            the number 7 to get 2800?</b>
                    </div>
                    <div className={"test-options"}>
                        <div className={"option"}>
                            <button>A</button>
                            <span>400 times</span>
                        </div>
                        <div className={"option"}>
                            <button>B</button>
                            <span>4 times</span>
                        </div>
                        <div className={"option"}>
                            <button>C</button>
                            <span>40 times</span>
                        </div>
                        <div className={"option"}>
                            <button>D</button>
                            <span>4000 times</span>
                        </div>
                    </div>
                    <div className={"arrows"}>
                        <button className={"prev"}>prev</button>
                        <button className={"next"}>next</button>
                    </div>
                </div>
            </div>
        </section>
    );
}

export default Test;