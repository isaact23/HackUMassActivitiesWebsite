import React from 'react';


class Activity extends React.Component {
    render() {
        return React.createElement('h1', null, 'Hello World!!!');
    }
}

ReactDOM.render(
    React.createElement(Activity, null, null),
    document.getElementById('root')
);