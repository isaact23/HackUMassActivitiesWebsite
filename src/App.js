import GenActivities from "./Activities";
import Leftnav from "./Leftnav";
import React from "react";

export default function App() {

    // Get the selected filters from Leftnav checkboxes
    const filters = Leftnav.filters;
    console.log(filters);

    // Return the array of HTML activity elements.
    return (
        <div>
            <Leftnav />
            {GenActivities(filters)}
        </div>
    );
}