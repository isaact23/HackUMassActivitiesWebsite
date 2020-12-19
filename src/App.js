import React, {useEffect, useState} from "react";

// Use Flask to call python and scrape internet data, then
// generate HTML for each activity found. Called by index.js.
function App() {
    // Call app.py to scrape internet for data
    const [data, setData] = useState("Empty name");
    useEffect(() => {
        fetch('/scrape').then(res => res.json()).then(data => {
          setData(data);
        });
        }, []
    );

    // Generate an activity HTML element for each entry in the JSON returned by app.py
    var activities = [];
    for (const [key, value] of Object.entries(data)) {
        activities.push(
            <a href={value.url}>
                <div className="activity">
                    <h2>{value.type}</h2>
                    {value.name}
                </div>
            </a>
        );
    }

    // Return the array of HTML activity elements.=
    return activities;
}

export default App;
