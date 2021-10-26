//responsive sidenav
var openMenu = document.querySelector(".menu");

openMenu.addEventListener("click", function(){
    document.querySelector(".sidebar").style.display = "inline";
})
var closeMenu = document.querySelector(".fa-times");
closeMenu.addEventListener("click", function(){
    document.querySelector(".sidebar").style.display = "none";
})


//active nav

var sidebarContainer = document.getElementById("navItems");                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

var navItems = sidebarContainer.getElementsByClassName("nav");

var navLength = navItems.length;

for(let i = 0; i< navLength; i++ ){
    navItems[i].addEventListener("click", function(){
        var activeNav = document.getElementsByClassName("active");
        activeNav[0].className = activeNav[0].className.replace(" active", "");
        this.className+= " active";
    })
}
