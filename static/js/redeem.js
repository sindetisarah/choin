var updateBtn = document.getElementsByClassName('update-cart')
let updateBtnLngth = updateBtn.length

for (let i = 0; i < updateBtnLngth; i++) {
    updateBtn[i].addEventListener('click', function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'action:', action);
        updateUserOrder(productId, action)
    })

}

function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getToken('csrftoken');

function updateUserOrder(productId, action) {
    var url = "http://127.0.0.1:8000/student/update_item/"
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        .then(response => response.json)
        .then(data => {
            console.log('data:', data)
            location.reload()
        })
        .catch(error => alert(error.toString()))
}

document.querySelector('.close').addEventListener('click',
    function() {
        document.querySelector('.card').style.display = 'none';
    })








// document.querySelector(".minus-btn").setAttribute("disabled", "disabled");

// var valueCount

// var price = document.getElementById("choins").value;
// console.log(price);

// function choinTotal() {
//     var total = parseFloat(valueCount) * parseFloat(price);
//     // document.getElementById("choins").value = total
// }
// document.querySelector(".plus-btn").addEventListener("click", function() {
//     valueCount = document.getElementById("quantity").value;
//     valueCount++;
//     document.getElementById("quantity").value = valueCount;
//     if (valueCount > 1) {
//         document.querySelector(".minus-btn").removeAttribute("disabled");
//         document.querySelector(".minus-btn").classList.remove("disabled")
//     }


//     choinTotal()
// })

// document.querySelector(".minus-btn").addEventListener("click", function() {

//     valueCount = document.getElementById("quantity").value;

//     valueCount--;

//     document.getElementById("quantity").value = valueCount

//     if (valueCount == 1) {
//         document.querySelector(".minus-btn").setAttribute("disabled", "disabled")
//     }
//     choinTotal()
// })

// //purchase modal

// // document.querySelector('.fa-shopping-cart').addEventListener('click', function(){
// //     document.querySelector('.purchase-modal').style.display = "inline"

// //     var tbl = document.createElement('table');


// //   var tbdy = document.createElement('tbody');
// //   for (var i = 0; i < 1; i++) {
// //     var tr = document.createElement('tr');
// //     for (var j = 0; j < 1; j++) {
// //       if (i == 2 && j == 1) {
// //         break
// //       } else {
// //         var td = document.createElement('td');


// //         i == 1 && j == 1 ? td.setAttribute('rowSpan', '2') : null;
// //         tr.appendChild(td)
// //       }
// //     }
// //     tbdy.appendChild(tr);
// //   }
// //   tbl.appendChild(tbdy);
// //   document.querySelector('.purchase').appendChild(tbl)

// // })

// // document.querySelector('.close').addEventListener('click', function(){
// //     document.querySelector('.purchase-modal').style.display = "none"
// // })

// //selected 
// // function selectedItem(){
// //    var cart= document.querySelectorAll('.fa-shopping-cart');
// //    for(let i = 0; i <cart.length; i++){
// //        if(cart[i].checked){
// //            document.querySelector('.purchase').style.backgroundColor = 'red'
// //        }
// //    }
// // }