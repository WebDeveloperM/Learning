import React, {useContext} from 'react';
import 'bulma/css/bulma.css'
import {useState, useEffect} from "react";
import CartProduct from "./CartProduct";
import axios from "axios";
import {UserContext} from "../../App";
import {Link} from "react-router-dom";


function CartContent() {
    const [data, setData] = useState(null)
    const [isLoading, setIsLoading] = useState(true)

    useEffect(_ => {
        const user = JSON.parse(localStorage.getItem('user'))
        axios.get(`http://localhost:1337/api/users?populate=baskets&filters[id]=${user.user.id}`)
            .then(result => {
                setData(result.data)
            })
    }, [])

    return (
        <div>
            <div className="card mb-4 p-4 has-text-weight-bold is-size-4">
                <a className="button has-text-left is-danger">Back to main page</a>
                <a className="button has-text-right is-info ml-4">Checkout</a>

                <div className="columns has-text-centered">
                    <div className="column">
                        <div className="content">Items:</div>
                    </div>
                    <div className="column">
                        <div className="content">Total: {data ? data.price : '0'} sum</div>
                    </div>
                </div>
            </div>
            <div className="card p-5">
                <div className="content">
                    <table className="table has-text-centered">
                        <thead>
                        <tr>
                            <th></th>
                            <th>Item</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                        </thead>
                        <tbody>
                        { isLoading && <h1>Loading.....</h1>}
                        </tbody>
                    </table>
                    { data && <Link to={'/checkout'} className={'button is-success is-fullwidth'}>
                        Checkout
                    </Link> }
                </div>
            </div>
        </div>
    )
}

export default CartContent;