document.querySelector('.close').addEventListener('click',
    function() {
        document.querySelector('.modal-content').style.display = "none"
    })
document.getElementById('login').addEventListener('click',
    function() {
        document.querySelector('.modal-content').style.display = "flex";
    });