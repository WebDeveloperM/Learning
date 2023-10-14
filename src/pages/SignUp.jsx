import React from 'react';
import SignUpForm from "../components/SingUpForm/SignUpForm";

function SignUp(props) {
    return (
        <div className='columns is-justify-content-center'>
            <div className='column is-5'>
                <SignUpForm/>
            </div>
        </div>
    );
}

export default SignUp;