import React, { Component, Fragment } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  handleClick() {
    console.log('this is:', this);
  }

  componentDidMount() {
    fetch("api/event")
      .then(res => {
        if (res.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return res.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <Fragment>

        <h1>Add a new event</h1>

        <form>
          <p>Title:
            <input type="text"/>
          </p>
          <p>Description:
            <input type="text"/>
          </p>
          <p>Location:
            <input type="text"/>
          </p>
          <p>Start Date/Time:
            <input type="datetime-local"/>
          </p>
          <p>End Date/Time:
            <input type="datetime-local"/>
          </p>
        </form>

        <button onClick={() => this.handleClick()}>
          Create Event
        </button>

        <ul>
          <p>Your upcoming events:</p>
          {this.state.data.map(event => {
            return (
              <li key={event.id}>
                {event.summary} - {event.location} - {event.start}
              </li>
            );
          })}
        </ul>

      </Fragment>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
