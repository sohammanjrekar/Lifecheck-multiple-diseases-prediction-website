import React, { Component } from 'react'
import "../Style/Form.css"
import axios from 'axios'
import { Progress } from 'react-sweet-progress';
import "react-sweet-progress/lib/style.css";
import Alert from '@material-ui/lab/Alert';
import { TemplatePlaceholder } from '@devexpress/dx-react-core';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

export default class Form extends Component {
    state={
        Features:[],
        form: {

        },
        result: [],
        show: false
    }

    componentDidMount() {
        axios.get("/scoreJson").then(response => {
            this.setState({Features:response.data.result})
          })
         
      }

      handleChange = feature => (event) => {
          console.log(this.state.form)

          let copyForm = { ...this.state.form};
        
          copyForm[feature] = [event.target.value]
        this.setState({
            form: copyForm
          })
    }

    handleSelect = feature => (event) => {
        console.log(event.target.value)
        console.log(feature)
        let copyForm = { ...this.state.form};
        copyForm[feature] = [event.target.value]
        this.setState({
            form: copyForm
          })
          
    }

    onChangeValue = feature => (event) => {
        let copyForm = { ...this.state.form};
        copyForm[feature] = [event.target.value]
        this.setState({
            form: copyForm
          })
    }
    
    onSubmit = () => {
        console.log(this.state.form);
        let copyForm = { ...this.state.form};
        
        let sorted = this.sortDict(copyForm);
        this.setState({form: sorted})
        axios.post("/scoreFile" ,this.state.form).then(response => {
           this.setState({result: response.data.result, show: true});
          })

    }

    sortDict = (dict) => {
        var keys = Object.keys(dict); // or loop over the object to get the array
        let numbers = []
        // keys will be in any order
       // maybe use custom sort, to change direction use .reverse()
        for(let i = 0; i < keys.length; i++){
            let result = parseInt(keys[i].split("_")[1])
            numbers.push(result);
        }
        numbers.sort((a, b) => a - b); 
        // keys now will be in wanted order
        let newDict = {}
        for (var i=0; i<numbers.length; i++) { // now lets iterate in sort order
            var value = dict['Feature_'+numbers[i]];
            newDict['Feature_'+numbers[i]] = value;
            /* do something with key & value here */
} 
        console.log(newDict);
        return newDict;
    }
    render() {
        return (
            <div id="project">
                <div class="container">
                {this.state.Features.map((feature,i) => (
                        feature.type==="textBox" ? 
                        <Paper elevation={3} style={{color:"white",background:"transparent",width:"100%",marginLeft:"auto",marginRight:"auto"}}>
                        <div class="labels">
                        <label id="name-label" for="name">{feature.name}</label>
                        </div>
                      <div class="input-tab">
                        <input class="input-field" type="number" id="name" name="name" placeholder="Enter Value" onChange={this.handleChange(feature.name)} required autofocus />
                        </div>
                        <br/> <br/> 
                        </Paper>:

                        
                        feature.type==="selectBox" ? 
                        <Paper elevation={3} style={{color:"white",background:"transparent",width:"100%",marginLeft:"auto",marginRight:"auto"}}>
                            <div class="labels">
                            <label for="dropdown">{feature.name}</label></div>
                            <div class="input-tab">
                            <select id="dropdown" name="site" onChange={this.handleSelect(feature.name)}>
                                <option disabled value selected>Select an option</option>
                                    {feature.values.map((value,selected)=>{
                                         return(<option value={selected}>{value}</option>
                                    )
                                    })}
                            </select>
                             </div>
                             <br/> <br/> 
                        </Paper>
                        :
                        feature.type ==="radioButton" ? 
                        <Paper elevation={3} style={{color:"white",background:"transparent",width:"100%",marginLeft:"auto",marginRight:"auto"}}>
                        <div class="labels">
                        <label>{feature.name}</label></div>
                      <div class="input-tab" onChange={this.onChangeValue(feature.name)}>
                      
                      <input type="radio" name={feature.name} value="1" />{feature.values[1]}<br/>
                        <input type="radio" name={feature.name} value="0"/>{feature.values[0]} <br/>
                        
                            </div>       
                            </Paper>
                        :
                        null 

        ))}
        <input type="submit" value="Submit" onClick={this.onSubmit}/>
        </div>
        <br/>
        <br/>
        {console.log(this.state.result)}
        {this.state.show === false ? <Alert severity="warning">Please fill all fields.</Alert> : null
    }
{this.state.show === true ?
<div>   Disease 1
                    <Progress
                                type="circle"
                                width={120}
                                percent={Math.round(this.state.result[0]*100)}
                            /> Disease 2
                            <Progress
                                type="circle"
                                width={120}
                                percent={Math.round(this.state.result[1]*100)}
                            /> Disease 3
                            <Progress
                                type="circle"
                                width={120}
                                percent={Math.round(this.state.result[2]*100)}
                            />
                            Disease 4
                            <Progress
                                type="circle"
                                width={120}
                                percent={Math.round(this.state.result[3]*100)}
                            />
                            </div>
          : null }
    </div>

        )
    }
}
