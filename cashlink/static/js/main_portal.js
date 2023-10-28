// Get the viewport height and multiply by 1% to get the value for a vh unit
let vh = window.innerHeight * 0.01;

// Set the value above to in the --vh custom property to the root of the document
document.documentElement.style.setProperty("--vh", `${vh}px`);

// Listen for the resize event on windows screen to perform the same action above
window.addEventListener("resize", () => {
     let vh = window.innerHeight * 0.01;
     document.documentElement.style.setProperty("--vh", `${vh}px`);
});


// STOP FORM RESUBMISSION AFTER RELOAD
if(window.history.replaceState) {
     window.history.replaceState(null, null, window.location.href)
}

// Function collapse or expand the sidebar
let sidebar = document.querySelector('.sidebar');
// let headerLogo = document.getElementById('header_logo');
let menuLinks = document.getElementsByClassName('side_menu_link')
sidebar.addEventListener('mouseenter', openSidebar);
sidebar.addEventListener('mouseleave', closeSidebar);

function openSidebar() {
    sidebar.style.width = '200px';
    // headerLogo.style.marginLeft = '210px';
    for (var i = 0; i < menuLinks.length; i++) {
        menuLinks[i].style.opacity = '1';
    }

}
function closeSidebar() {
    sidebar.style.width = '65px';
    // headerLogo.style.marginLeft = '100px';
    for (var i = 0; i < menuLinks.length; i++) {
        menuLinks[i].style.opacity = '0';
    }

}


// Snipper Loader Function
function showLoader() {
    loader.style.display = "flex";
    fetch("url").then((response) => {
         if (response) {
              loader.style.display = "none";
         }
    })      
};

// Disable right-click navigation on the entire page
document.addEventListener('contextmenu', event => event.preventDefault());

