import {BrowserRouter as Router, Route, Switch, BrowserRouter} from 'react-router-dom';
import Home from './Home';
import Register from './Register';
import Login from './Login';

export default function AppRoutes() {
    return(
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={Home} />
                <Route path="/register" component={Register} />
                <Route path="/login" component={Login} />
            </Switch>
        </BrowserRouter>
        )
    }