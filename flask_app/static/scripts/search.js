$(function () {

    const searchInput = $("#searchInput");

    function getItems () {
        let name = searchInput.val();
        let vendor;
        let link;

        let value = $('#filterBy').val();
        let searchLink = "http://localhost:5000/api/v1/search/";
        let catergoryLink = "http://localhost:5000/api/v1/";
        name = name.toLowerCase();

        if (name.includes('laptop') || name.includes('desktop')) {
            if (name.includes('laptop')) {
                name = 'laptop';
            } else {
                name = 'desktop';
            }
            if (value === 'VendorGroup') {
                link = catergoryLink + name;
            } else {
                link = catergoryLink + name + '/' + value;
            }
        }

        else if (value != 'VendorGroup') {
            vendor = value;
            link = searchLink + name + '/' + vendor;
        }
        else {
            link = searchLink + name;
        }
        //	    alert(link)
        $.ajax({
            type: "GET",
            url: link,
            success: function (data) {
                const itemsDiv = $("#searchResults");
                itemsDiv.empty(); // clear the previous search items
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
                        "        <div class='ItemImage'>",
                        "            <img src=" + imgUrl + " alt='Image of " + itemName + "'>",
                        "        </div>",
                        "        <div class='ItemInfo'>",
                        "        <span class='ItemName'>" + itemName + "</span>",
                        "            <span class='ItemVendor'>From " + itemVendor + "</span>",
                        "            <span class='ItemPrice'> KSH " + itemPrice + "</span>",

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
            fail: function (error) { console.log(error) }
        })
    }
    $("#searchButton").click(() => getItems());
    getItems();
})
