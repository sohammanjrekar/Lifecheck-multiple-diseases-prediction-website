import logo from './logo.svg';
import './App.css';
import Carousel from './Components/Carousel';
import Form from './Components/Form';
import Header from "./Components/NavBar"
import { Grid } from '@material-ui/core';

function App() {

  return (
    <div className="App">
     <Header></Header>
      <Carousel></Carousel>
      <br/><br/>
      <Grid container spacing={10}>
      <Grid item xs={8} style={{marginLeft: "15%"}}>
        <Form></Form>
      </Grid>

      </Grid>
  
      <br/><br/><br/>
      <br/><br/><br/>
      <br/><br/><br/>
      <br/>
      
    </div>
  );
}

export default App;
