import { useAuth0 } from "@auth0/auth0-react";
import logo from './logo.svg';
import './App.css';

function App() {

  const { user, loginWithRedirect, isAuthenticated, logout } = useAuth0();

  console.log("Current user: ", user)
  return (
    <div className="App">
      {isAuthenticated && <h3> Hello {user.name} </h3>}
      <header className="App-header">
        {
          isAuthenticated ? (
            <button onClick={(e) => logout()}>Logout</button>
          ) : (
            <button onClick={(e) => loginWithRedirect()}> 
            Login With Redirect
            </button>
          )
        }

      </header>
    </div>
  );
}

export default App;
