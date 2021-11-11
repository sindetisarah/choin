function open(e){
    e.preventDefault()
document.getElementById("edit").addEventListener('click', function(){

    document.querySelector(".metric-modal").style.display = "block";
    
    } )
}
function close(e){
    e.preventDefault()
document.getElementById("close").addEventListener('click', function(){
    
document.querySelector(".metric-modal").style.display = "none";
    
})
    console.log("hello")
}

    
// document.querySelector("#close-modal").addEventListener('click', function(){
    
// document.querySelector(".add-metric-modal").style.display = "none";
    
// })


// addEventListener('click', function(){
    
// document.querySelector(".add-metric-modal").style.display = "none";
    
// })
     