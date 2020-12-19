import React, {useEffect, useState} from "react";

// The react.js application.
// In index.html, the <div class="root"></root> is the section modified by this code.
// The code is responsible for getting activity data from scrape/games.csv and generating corresponding HTML.
function App() {
    const [placeholder, setPlaceholder] = useState('Hi');
    useEffect(() => {
        fetch('/hello').then(res => res.json()).then(data => {
          setPlaceholder(data.result);
        });}, []
    );

    const activities = <div class="activity">Activity A</div>;
    return (
        <block>
            <p>{placeholder}</p>
            activities
        </block>
    );
}

export default App;
