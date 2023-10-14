import React, {useState} from 'react';
import Calendar from "react-calendar";
import 'react-calendar/dist/Calendar.css';
import '../assets/css/calendar.css'

function Lessons(props) {
    const [value, setValue] = useState(null)
    const [active, setActive] = useState(false)
    function handle(event) {
        console.log(event)
        setValue(event)
        setActive(true)
    }

    return (
        <div className={"calendar-block"}>
            <div className={"modal-block " + (active && "modal-active")} onClick={e => {
                e.stopPropagation()
                setActive(false)
            }}>
                <div className={"modal-content"}>
                    <h1>\</h1>
                </div>
            </div>
            <Calendar onChange={handle} value={value} />
        </div>
    );
}

export default Lessons;