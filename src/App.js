import React, {useEffect, useState} from "react";

// The react.js application.
// In index.html, the <div class="root"></root> is the section modified by this code.
// The code is responsible for getting activity data from scrape/games.csv and generating corresponding HTML.
function App() {
    const [name, setName] = useState("Empty name");
    useEffect(() => {
        fetch('/hello').then(res => res.json()).then(data => {
          setName(data.result);
        });
        }, []
    );

    const activities = <div class="activity">Activity A</div>;
    return (
        <div>
            <p>{name}</p>
            activities
        </div>
    );
}

export default App;
