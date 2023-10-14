import React, {useContext, useEffect, useState} from 'react';
import axios from "axios";
import {Link} from "react-router-dom";
import {UserContext} from "../App";
import {toast} from "react-toastify";

function Checkout(props) {
    const [data, setData] = useState()
    const [info, setInfo] = useState({
        name: '',
        email: '',
        address: '',
        telephone: '',
    })
    const { user } = useContext(UserContext)

    useEffect(_ => {
        const user = JSON.parse(localStorage.getItem('user'))
        axios.get(`http://localhost:1337/api/users?populate=baskets.product&filters[id]=${user.user.id}`)
            .then(result => {
                setData(result.data[0].baskets)
                console.log(user.user)
            })
    }, [])

    async function createCheckout(e) {
        let check = false
        e.preventDefault()
        await axios.post('http://localhost:1337/api/checkouts', {
            data: {
                ...info,
                user: JSON.parse(localStorage.getItem('user')),
                products: data,
            }
        }).then(res => {
            toast.success('Ваши товары оформлены!!!')
            setInfo({
                name: '',
                address: '',
                telephone: '',
                email: ''
            })
            check = true
            console.log(res)
        }).catch(e => toast.error(e))
        if (check) {
            for (const item of data) {
                await axios.delete(`http://localhost:1337/api/baskets/${item.id}`)
            }
        }
    }

    return (
        <div className='columns is-justify-content-space-between'>
            <div className='column is-5'>
                <form onSubmit={createCheckout}>
                    <input
                        required={true}
                        minLength={5}
                        onInput={e => setInfo({...info, name: e.target.value})}
                        value={info.name}
                        type="text"
                        className='input'
                        placeholder='name'/>
                    <input
                        required={true}
                        minLength={5}
                        onInput={e => setInfo({...info, email: e.target.value})}
                        value={info.email}
                        type="email"
                        className='input'
                        placeholder='email'/>
                    <input
                        required={true}
                        minLength={5}
                        onInput={e => setInfo({...info, address: e.target.value})}
                        value={info.address}
                        type="text"
                        className='input'
                        placeholder='address'/>
                    <input
                        required={true}
                        minLength={5}
                        onInput={e => setInfo({...info, telephone: e.target.value})}
                        value={info.telephone}
                        type="text"
                        className='input'
                        placeholder='phone number'/>
                    <button className='button is-info is-fullwidth'>checkout</button>
                </form>
            </div>
            <div className='column is-6'>
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
                            </tbody>
                        </table>
                        {data && <Link to={'/checkout'} className={'button is-success is-fullwidth'}>
                            Checkout
                        </Link>}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Checkout;