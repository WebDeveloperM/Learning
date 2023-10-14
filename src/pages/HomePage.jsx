import React, {useContext, useEffect, useState} from 'react';
import {Slider} from "infinite-react-carousel";
import axios from "axios";
import {NavLink} from "react-router-dom";
import {UserContext} from "../App";
import {toast} from "react-toastify";
import 'react-toastify/dist/ReactToastify.css'

function HomePage(props) {
    const [data, setData] = useState(null)
    const {user} = useContext(UserContext)

    useEffect(() => {
        axios.get('http://localhost:1337/api/products?populate=photos').then(
            res => {
                setData(res.data)
                console.log(res.data)
            }
        )
    }, [])

    async function addToCart(product) {
        console.log(user)
        await axios.post('http://localhost:1337/api/baskets', {
            data: {
                owner: user.user.user,
                product: product,
                quantity: 1,
                total_price: product.attributes.price
            }
        }).then(
            res => {
                toast.success('Товар добавлен!!!')
                console.log(res)
            }
        )
    }

    return (
        <div className='container is-fullwidth'>
            <Slider autoplay={true} autoplaySpeed={1500} arrows={true}>
                <img alt={'qwhfius'} src='../assets/log.png'/>
                <img alt={'qwhfius'} src='../assets/log.png'/>
                <img alt={'qwhfius'} src='../assets/log.png'/>
                <img alt={'qwhfius'} src='../assets/log.png'/>
            </Slider>
            <div className='my-6 columns is-justify-content-space-between is-multiline'>
                {data && data.data.map(
                    value => <div key={value.id} className='column is-3'>
                        <div className="card">
                            <div className="card-image">
                                <Slider>
                                    {value.attributes.photos.data.map(item => <figure className='image'>
                                        <img src={'http://localhost:1337' + item.attributes.url} alt="kartina"/>
                                    </figure>)}
                                </Slider>
                            </div>
                            <div className="card-content">
                                {value.attributes.description}
                            </div>
                            <div className="card-footer">
                                <div className="card-footer-item">
                                    <p><NavLink
                                        to={`/product/${value.id}`}>{value.attributes.title}</NavLink> - {value.attributes.price}$
                                    </p>
                                </div>
                                {user.active && <div className={'card-footer-item'}>
                                    <button onClick={_ => addToCart(value)} className={'button is-success'}>BUY</button>
                                </div>}
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default HomePage;