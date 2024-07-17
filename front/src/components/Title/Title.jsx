import React, { useState, useEffect } from 'react';

import "./Title.css"

function Title({ type }) {
    return (
        <div className="titleContainer">
            <h1>Web Scraping {type}</h1>
            <div className="divisor"></div>
        </div>
    )
}

export default Title;