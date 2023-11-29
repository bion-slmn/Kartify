
$(document).ready(function () {
  $('div.card, #laptop, #desktop, #all').click(function () {
    $('html, body').animate({
      scrollTop: $('#anchorContent').offset().top
    }, 2000);
    let url;
    const clickedId = $(this).attr('id');

    if (clickedId !== 'laptop' && clickedId !== 'desktop' && clickedId !== 'all') {
      url = 'http://localhost:5000/api/v1/search/' + clickedId;
    } else {
      url = 'http://localhost:5000/api/v1/' + clickedId;
    }

    $('div.flex-content').empty(); // empty the child contents

    $.get(url, function (data, status) {
      const keys = Object.keys(data);
      keys.forEach(function (key, index) {
        const item = data[key];
        const itemVendor = item.vendor;
        const itemLink = item.link;
        const imgUrl = item.img_link;
        const itemName = item.name;
        const itemPrice = item.price;
        const article = `
<article class='ItemCard' id=''>
<a class='ItemLink' href='${itemLink}'>
<h3 class='ItemName'>${itemName}</h3>
<div class='ItemImage'>
<img src='${imgUrl}' alt='Image of ${itemName}'>
</div>
<div class='ItemInfo'>
<div class='ItemVendor'>Vendor: ${itemVendor}</div>
<div class='ItemPrice'>KSH: ${itemPrice}</div>
</div>
</a>
</article>`;
        $('div.flex-content').append(article);
      });
    });
  });
});
