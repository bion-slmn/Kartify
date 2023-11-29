$(document).ready(function(){
$('#laptop, #desktop, #all').click(function(){
let clickedId = $(this).attr('id');
const url = 'http://localhost:5000/api/v1/' + clickedId;
$.get(url, function(data, status){
const keys = Object.keys(data);
$(".content").empty();
keys.forEach(function(key, index){
const item = data[key];
const itemVendor = item["vendor"];
const itemLink = item["link"];
const imgUrl = item["img_link"];
const itemName = item["name"];
const itemPrice = item["price"];
const article = $([
"<article class='ItemCard' id=''>",
"    <a class='ItemLink' href='" + itemLink + "'>",
"        <h3 class='ItemName'>" + itemName + "</h3>",
"        <div class='ItemImage'>",
"            <img src='" + imgUrl + "' alt='Image of " + itemName + "'>",
"        </div>",
"        <div class='ItemInfo'>",
"            <div class='ItemReview'>Review stars here</div>",
"            <div class='ItemVendor'> Vendor: " + itemVendor + "</div>",
"            <div class='ItemAvailability'> Availability: availability status</div>",
"            <div class='ItemDelivery'> Delivery: delivery status</div>",
"            <div class='ItemPrice'>" + itemPrice + "</div>",
"        </div>",
"    </a>",
"</article>"
].join('\n'));
$("#searchResults").append(article);
});
});
});
});

