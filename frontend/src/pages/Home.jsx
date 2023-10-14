import React from 'react';

function Home(props) {
    return (
        <div className={"row mt-4 home-blocks"}>
            <div className={"col-lg-3 home-block is_disabled"}>
                <img src="./banne.png" alt=""/>
            </div>
            <div className={"col-lg-3 home-block is_disabled"}>
                <img src="./banne.png" alt=""/>
            </div>
            <div className={"col-lg-3 home-block is_disabled"}>
                <img src="./banne.png" alt=""/>
            </div>
            <div className={"col-lg-3 home-block is_middle is_disabled"}>
                <img src="./banne.png" alt=""/>
            </div>
            <div className={"col-lg-3 home-block is_disabled"}>
                <img src="./banne.png" alt=""/>
            </div>
        </div>
    );
}

export default Home;