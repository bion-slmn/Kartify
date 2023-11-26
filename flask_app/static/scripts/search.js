$(function () {
    
    const searchInput = $("#searchInput");

    function getItems () {
        let name = searchInput.val();
        $.ajax({
            type: "GET",
            url: "http://localhost:5000/api/v1/search/"+name,
            success: function (data) {
                const itemsDiv = $("#searchResults")
                const keys = Object.keys(data)
                keys.forEach((key, index) => {
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
                        "            <img src=" + imgUrl + " alt='Image of " + itemName + "'>",
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
                    if (index === 1) {
                        console.log(article);
                    }
                    itemsDiv.append(article);
                })
            },
            fail: function (error) {console.log(error)}
        })
    }
    $("#searchButton").click(() => getItems());
    getItems();
})
