import React, { useState, useEffect } from 'react';
import { Link, animateScroll as scroll } from "react-scroll";
import '../Style/Header.css'

function Header() {
  const [click, setClick] = useState(false);
  const [button, setButton] = useState(true);
  const [navbar, setNavbar] = useState(false);

  const handleClick = () => setClick(!click);

  const closeMobileMenu = () => {
    setClick(false);
  }

  const scrollToTop = () => {
    scroll.scrollToTop();
    closeMobileMenu();
  };
  const showButton = () => {
    if (window.innerWidth <= 960) {
      setButton(false);
      setNavbar(true);
    } else {
      setButton(true);
    }
  };

  useEffect(() => {
    showButton();
  }, []);

  window.addEventListener('resize', showButton);

  const changeBackground = () => {
      if(window.scrollY >= 100){
        setNavbar(true);
      }
      else {
        if(window.innerWidth <= 960){
          setNavbar(true);
        }
        else{
          setNavbar(false);
        }
        
      }
  }
  window.addEventListener('scroll', changeBackground);
  return (
    <>
      <nav className={navbar ? 'navbar active' : "navbar"}>
        <div className='navbar-container'>
          <div className='menu-icon' onClick={handleClick}>
            <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
          </div>
          <ul className={click ? 'nav-menu active' : 'nav-menu'}>
            <li className='nav-item'>
              <Link className='nav-links' onClick={scrollToTop}>
                Home
              </Link>
            </li>
            <li className='nav-item'>
              <Link
                activeClass="active"
                to="project"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
                className='nav-links'
                onClick={closeMobileMenu}
              >
                Project
              </Link>
            </li>
            <li className='nav-item'>
            </li>
          </ul>
        </div>
      </nav>
    </>
  );
}

export default Header;