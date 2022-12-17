import $ from 'jquery'
import '../Style/Carousel.scss'
import {TweenMax} from 'gsap'
import { Button} from '@material-ui/core'

import React, { Component } from 'react'

let counter=1;

function moveDown(currentSlide) {
  
  var nextSlide = currentSlide.next();
  var currentSlideUp = currentSlide.find('.txt');
  var currentSlideDown = currentSlide.find('.img');
  var nextSlideUp = nextSlide.find('.img');
  var nextSlideDown = nextSlide.find('.txt');
  let currentCopy = currentSlide.find('.copy'); 
  let nextCopy = nextSlide.find('.copy'); 
  
  if( nextSlide.length !== 0 ) {

    counter = counter + 1;
    
    if( counter % 2 === 0 ) {

      TweenMax.to( currentSlideUp, 0.4, { y: '-100%', delay:0.15 });
      TweenMax.to( currentSlideDown, 0.4, { y: '100%', delay:0.15 });
      
    } else {
      TweenMax.to( currentSlideUp, 0.4, { y: '100%', delay:0.15 });
      TweenMax.to( currentSlideDown, 0.4, { y: '-100%', delay:0.15 });
    }
    
    TweenMax.to( currentCopy, 0.3, {autoAlpha: 0, delay:0.15});
    TweenMax.to( nextCopy, 0.3, {autoAlpha: 1, delay:1});
    TweenMax.to( nextSlideUp, 0.4, { y: '0%', delay:0.15 });
    TweenMax.to( nextSlideDown, 0.4, { y: '0%', delay:0.15 });
    
    $(currentSlide).removeClass('active');
    $(nextSlide).addClass('active');
    
  } 
}

function moveUp(currentSlide) {
  
  var prevSlide = currentSlide.prev();
  var currentSlideUp = currentSlide.find('.img');
  var currentSlideDown = currentSlide.find('.txt');
  var prevSlideUp = prevSlide.find('.txt');
  var prevSlideDown = prevSlide.find('.img');
  let currentCopy = currentSlide.find('.copy');
  let prevCopy = prevSlide.find('.copy'); 
  
  if( prevSlide.length !== 0 ) {
    
    counter = counter - 1;
    
    if( counter % 2 === 0 ) {
      
      
      TweenMax.to( currentSlideUp, 0.4, { y: '-100%', delay:0.15 });
      TweenMax.to( currentSlideDown, 0.4, { y: '100%', delay:0.15 });

      
    }else {
      TweenMax.to( currentSlideUp, 0.4, { y: '100%', delay:0.15 });
      TweenMax.to( currentSlideDown, 0.4, { y: '-100%', delay:0.15 });
    }
    
    TweenMax.to( currentCopy, 0.3, {autoAlpha: 0, delay:0.15});
    TweenMax.to( prevCopy, 0.3, {autoAlpha: 1, delay:1});
    TweenMax.to( prevSlideUp, 0.4, { y: '0%', delay:0.15 });
    TweenMax.to( prevSlideDown, 0.4, { y: '0%', delay:0.15 });
    
    $(currentSlide).removeClass('active');
    $(prevSlide).addClass('active');
    
  }
  
}

function hideNav() {
  
  if( counter === $('.slide').length) {    
    TweenMax.to($('.nav-down'),0.5, {autoAlpha: 0, delay:0.5} );
  }else {
     TweenMax.to($('.nav-down'),0.5, {autoAlpha: 1, delay:0.5} );
  }
  if( counter === 1) {    
    TweenMax.to($('.nav-up'),0.5, {autoAlpha: 0, delay:0.5} );
  }else {
     TweenMax.to($('.nav-up'),0.5, {autoAlpha: 1, delay:0.5} );
  }
  
}

function SlideUp() {
  
  var currentSlide = $('.active');
  moveUp(currentSlide);
  hideNav();
};
function SlideDown() {
  
  var currentSlide = $('.active');
  moveDown(currentSlide);
  hideNav();
};

export default class Carousel extends Component {


  componentDidMount(){

     counter=1;

  }



  render() {
    return (
      <div className="base">
        <h1 style={{color:"white"}}>INFORMATION</h1>
  <div className="slider-content">

 
    
    
    
    <div className="nav-wrapperc">
      <div className="nav-arrows">
        <div className="nav-up">
             <Button style={{  borderWidth:1,
    borderColor:'rgba(0,0,0,0.2)',
    alignItems:'center',
    justifyContent:'center',
    width:50,
    height:60,
    backgroundColor:"#a8a8a8",   
    color:"white",
    borderRadius:50,fontSize:'40px',fontWeight:'bold'}} onClick={SlideUp}>&#8593;</Button>
         </div>  
        <div className="nav-line"></div>
        <div className="nav-down">
           <Button style={{  borderWidth:1,
            borderColor:'rgba(0,0,0,0.2)',
            alignItems:'center',
            justifyContent:'center',
            width:50,
            height:60,
            backgroundColor:"#a8a8a8",
            color:"white",
            borderRadius:50,fontSize:'40px',fontWeight:'bold'}} onClick={SlideDown}>&#8595;</Button>
        </div>
      </div>
    </div>
    
    <div className="slider-wrapper">
      <div className="slider-container">                       
        <div className="slide active" data-order="1">
            <div className="slide-content txt">
              <div className="txt-wrapper">
                <span className="subtitle">What is Data Science</span>
                <p className="excerpt">
                Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data and apply knowledge and actionable insights from data across a broad range of application domains. Data science is related to data mining, machine learning and big data.
                </p>
              </div>
            </div>
            <div className="slide-content img">
              <img style={{objectFit:"scale-down"}} src="./DataScience.png" alt="" />
            </div>
          </div>  
        <div className="slide" data-order="2">
            <div className="slide-content txt">
              <div className="txt-wrapper">
                <span className="subtitle">Applications Of Data Science</span>
                 <p className="excerpt"> Data Science has many applications such as:
                    <ol>
                      <li>Healthcare</li>
                      <li>Targeted Advertising</li>
                      <li>Website Recommendations</li>
                      <li>Advanced Image Recognition</li>
                      <li>Speech Recognition</li>
                    </ol>
                  </p>
  
              </div>
            </div>
            <div className="slide-content img">
              <img style={{objectFit:"scale-down"}} src="./DataScienceApplications.jpeg" alt="" />
            </div>
          </div>  
        <div className="slide " data-order="3">
            <div className="slide-content txt">
              <div className="txt-wrapper">
                <span className="subtitle">Data Science in Healthcare</span>
                <p className="excerpt">Traditionally, medicine solely relied on the discretion advised by the doctors. For example, a doctor would have to suggest suitable treatments based on a patient’s symptoms.

However, this wasn’t always correct and was prone to human errors. However, with the advancements in computers and in particular, Data Science, it is now possible to obtain accurate diagnostic measures.

There are several fields in healthcare such as medical imaging, drug discovery, genetics, predictive diagnosis and several others that make use of data science. </p>
              </div>
            </div>
            <div className="slide-content img">
              <img style={{objectFit:"scale-down"}} src="./DataScienceHealthCare.png" alt="" />
            </div>
          </div>  
        <div className="slide " data-order="4">
            <div className="slide-content txt">
              <div className="txt-wrapper">
                <span className="subtitle">Predictive Analytics in Healthcare</span>
                <p className="excerpt">
                Healthcare is an important domain for predictive analytics. It is one of the most popular topics in health analytics. A predictive model uses historical data, learns from it, finds patterns and generates accurate predictions from it.

It finds various correlations and association of symptoms, finds habits, diseases and then makes meaningful predictions.
                </p>
              </div>
            </div>
            <div className="slide-content img">
              <img style={{objectFit:"scale-down"}} src="./Predictive.jpg" alt="" />
            </div>
          </div>
        <div className="slide " data-order="5">
            <div className="slide-content txt">
              <div className="txt-wrapper">
                <span className="subtitle">Our Model</span>
                <p className="excerpt">
                  We created a model with logistic regression for disease prediction. We trained our model with the dataset that provided to us. Our model has success rate close to 90%.
                </p>
              </div>
            </div>
            <div className="slide-content img">
              <img style={{objectFit:"scale-down"}} src="./Our Model.png" alt="" />
            </div>
          </div>
      </div>
    </div>
  </div>
  </div>
    )
  }
}



