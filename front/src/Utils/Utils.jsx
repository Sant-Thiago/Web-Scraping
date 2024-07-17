import React from "react";

export const handleInputValueOne = (event, setInputForm) => {
    const { value } = event.target;
    setInputForm(value);
};

export default {
    handleInputValue: (event) => {
        const { name, value } = event.target;
        setInputForm({
            ...inputForm,
            [name]: value
        });
    }
};
