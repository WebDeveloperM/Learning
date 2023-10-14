import React, {useEffect, useState} from 'react';
import {useParams} from "react-router-dom";
import axios from "axios";
import {Slider} from "infinite-react-carousel";

function ProductDetail(props) {
    const [product, setProduct] = useState(null)
    const {id} = useParams()

    useEffect(_ => {
        axios.get(`http://localhost:1337/api/products/${id}?populate=photos`)
            .then(res => {
                setProduct(res.data.data)
            })
    }, [])

    if (product) {
        return (
            <div className={'container'}>
                <div className='columns is-justify-content-space-between'>
                    <div className='column is-6'>
                        <Slider>
                            {product.attributes.photos.data.map(
                                value => <img src={`http://localhost:1337${value.attributes.url}`} alt=""/>
                            )}
                        </Slider>
                    </div>
                    <div className={'column box p-6 is-5'}>
                        <div className={'block is-flex is-justify-content-space-between'}>
                            <h1 className={'subtitle'}>{product.attributes.title}</h1>
                            <div className="buttons">
                                <button className={'button is-small is-primary'}>Favourite</button>
                                <button className={'button is-small is-info'}>Add to cart</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    return (
        <h1 className={'title has-text-centered'}>Loading...</h1>
    )
}

export default ProductDetail;