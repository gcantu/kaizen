$(function() {

  // EVENTS
  $('.lineitem-addheading').on('click',function() {
    $('.card-body').toggle(300);
  }); // collapse when click on add appointment

  // FUNCTIONS
  $("#id_line_item_set-0-product").change(function () {
      var url = $("#lineItemForm").attr("line-item-url");  // get the url of the `load_line_item` view
      var productId = $(this).val();  // get the selected country ID from the HTML input

      $.ajax({
        url: url,                     // set the url of the request (= localhost:8000/proposal/ajax/load-line-item)
        data: {
          'product_var': productId    // add the product id to the GET parameters
        },
        success: function (data) {    // `data` is the return of the `load_line_item` view function
          $("#lineItemList").append(data);  // render form selections in proposal template WIP
        }
      }); // AJAX request

    }); // listen to product field change in form

}); // Document is ready
