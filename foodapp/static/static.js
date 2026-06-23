function calculateTotal(price) {
    let qty = document.getElementById("qty").value;
    let total = price * qty;

    if (!qty || qty <= 0) {
        document.getElementById("total").innerText = "Total: ₹0";
    } else {
        document.getElementById("total").innerText = "Total: ₹" + total;
    }
}