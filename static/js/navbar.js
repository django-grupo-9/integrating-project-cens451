let scrollPosition = null;
let windowWidth = null;

const icon = document.querySelector('#iconNavId');
const menuMobile = document.querySelector('#navMobileId');
const navbar = document.querySelector('#navId');
const header = document.querySelector('header');
const dropdownItem = document.querySelector('.nav-item.dropdown');
const navbarBackgroundColor = window.getComputedStyle(navbar).backgroundColor;

hideNavbar = function(width){
    if (width > 850) {
        navbar.classList.remove('navigationHidden');
        navbar.classList.add('navigation');
    } else {
        navbar.classList.remove('navigation');
        navbar.classList.add('navigationHidden');
    }
}

hideIcon = function (width) {
    if (width > 850) {
        icon.classList.remove('iconNavbar');
        icon.classList.remove('icon-active')
        icon.classList.add('iconNavbarHidden');

    } else {
        icon.classList.add('iconNavbar')
        icon.classList.remove('iconNavbarHidden')
    }
}

hideMenuMobile = function (width) {
    if (width < 850) {
        menuMobile.classList.add('mobile-nav-leave-to')
    } else {
        if (icon.classList.contains('icon-active')) {
            menuMobile.classList.remove('mobile-nav-enter-active',
            'mobile-nav-enter-to')
            menuMobile.classList.add('mobile-nav-leave-to',
            'mobile-nav-leave-active')
            
        } else {
            menuMobile.classList.remove('mobile-nav-enter-active',
            'mobile-nav-enter-to')
        }
        
    }
}

formatPage = function (e) {
    windowWidth = window.innerWidth;
    hideNavbar(windowWidth);
    hideIcon(windowWidth);
    hideMenuMobile(windowWidth);
}

showMobileMenu = function () {
    console.log('click')
    if (icon.classList.contains('icon-active')) {
        // hide
        icon.classList.remove('icon-active');
        menuMobile.classList.remove('mobile-nav-enter-active')
        menuMobile.classList.add('mobile-nav-leave-active')
        menuMobile.classList.remove('mobile-nav-enter-to')
        menuMobile.classList.add('mobile-nav-leave-to')
        header.classList.remove('scrolled-nav')
    } else {
        // show
        icon.classList.add('icon-active');
        menuMobile.classList.add('mobile-nav-enter-active')
        menuMobile.classList.remove('mobile-nav-leave-to');
        menuMobile.classList.add('mobile-nav-enter-to');
        header.classList.add('scrolled-nav')
    }
}

updateScroll = function () {
    scrollPosition = window.scrollY;
    if (scrollPosition > 50) {
        header.classList.add('scrolled-nav')
    } else {
        header.classList.remove('scrolled-nav')
    }
}

window.addEventListener('load', formatPage)
window.addEventListener('scroll', updateScroll);
window.addEventListener('resize', formatPage)
icon.addEventListener('click', showMobileMenu)


dropdownItem.style.backgroundColor = navbarBackgroundColor;