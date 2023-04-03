let scrollPosition = null;
let windowWidth = null;

const icon = document.querySelector('#iconNavId');
const menuMobile = document.querySelector('#mobileNavId');
const navbar = document.querySelector('#navId');
const header = document.querySelector('header')

hideNavbar = function(width){
    if (width > 768) {
        navbar.classList.remove('navigationHidden');
        navbar.classList.add('navigation');
    } else {
        navbar.classList.remove('navigation');
        navbar.classList.add('navigationHidden');
    }
}

hideIcon = function (width) {
    if (width > 768) {
        icon.classList.remove('iconNavbar');
        icon.classList.remove('icon-active')
        icon.classList.add('iconNavbarHidden');

    } else {
        icon.classList.add('iconNavbar')
        icon.classList.remove('iconNavbarHidden')
    }
}

hideMenuMobile = function (width) {
    if (width > 768) {
        if (icon.classList.contains('icon-active')) {
            menuMobile.classList.remove('mobile-nav-enter-active',
            'mobile-nav-enter-to')
            menuMobile.classList.add('mobile-nav-leave-to',
            'mobile-nav-leave-active')
        } else {
            menuMobile.classList.remove('mobile-nav-enter-active',
            'mobile-nav-enter-to')
        }

    } else {

        menuMobile.classList.add('mobile-nav-leave-to')
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
    } else {
        // show
        icon.classList.add('icon-active');
        menuMobile.classList.add('mobile-nav-enter-active')
        menuMobile.classList.remove('mobile-nav-leave-to');
        menuMobile.classList.add('mobile-nav-enter-to');
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