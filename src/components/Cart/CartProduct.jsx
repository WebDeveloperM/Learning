import React, {useState} from 'react';
import 'bulma/css/bulma.css'


function CartProduct(props) {
    const [count, setCount] = useState(0)
    const [cart, setCart] = useState(false)

    return (
        <>
            <tr>
                <th>
                    <figure className='image'>
                        {props.product.attributes.Thumbnail.data.map(
                                value => <img src={`http://localhost:1337${value.attributes.url}`} style={{ width: '205px', height: '175px' }}/>
                            ) }
                    </figure>
                </th>
                <td>{props.product.attributes.Title}</td>
                <td>{props.product.attributes.Price} сум</td>
                <td>
                    <div className="quantity ml-1 m-0">
                        <p className=''>{count > 0 && cart === true ? `${count}` : '0'}</p>
                        <button className='button p-0 mb-2' style={{width: '15px', height: '15px', bottom: '17px'}} onClick={ () => {
                            setCart(true)
                            setCount(prevState => prevState + 1)}
                        }><nav className='mb-1'>+</nav></button>
                        <button className='button p-0 mb-2' style={{width: '15px', height: '15px', bottom: '17px'}} onClick={ () => setCount( prevState => prevState > 0 && prevState - 1 ) }><nav className='mb-1'>-</nav></button>
                    </div>
                </td>
                <td>
                    <a style={{fontStyle: '20px', color: 'black'}}>
                        <ion-icon name="trash-outline"></ion-icon>
                    </a>
                    {count > 0 ? count * props.product.attributes.Price : '0'} <br/> сум
                </td>
            </tr>
        </>
    );
}

export default CartProduct;