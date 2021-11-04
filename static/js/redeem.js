document.querySelector(".minus-btn").setAttribute("disabled", "disabled");

var valueCount

var price = document.getElementById("choins").value;
console.log(price);

function choinTotal() {
    var total = parseFloat(valueCount) * parseFloat(price);
    document.getElementById("choins").value = total
}
document.querySelector(".plus-btn").addEventListener("click", function() {
    valueCount = document.getElementById("quantity").value;
    valueCount++;
    document.getElementById("quantity").value = valueCount;
    if (valueCount > 1) {
        document.querySelector(".minus-btn").removeAttribute("disabled");
        document.querySelector(".minus-btn").classList.remove("disabled")
    }


    choinTotal()
})

document.querySelector(".minus-btn").addEventListener("click", function() {

    valueCount = document.getElementById("quantity").value;

    valueCount--;

    document.getElementById("quantity").value = valueCount

    if (valueCount == 1) {
        document.querySelector(".minus-btn").setAttribute("disabled", "disabled")
    }
    choinTotal()
})