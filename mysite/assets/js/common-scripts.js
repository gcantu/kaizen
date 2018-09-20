$(function() {

// EVENTS
$('#id_finish').on('change', function() {
  var selectedItem = $(this).val();
  var option = "Stain"
  var fieldId = "#stain-field"

  showField(selectedItem, option, fieldId);
});

$('#main-edit-button').on('click', function() { // add/remove tax from proposal
   $(".edit-button").removeClass("hidden");
});


$('#line-item-edit-button').on('click', function() { // add/remove tax from proposal
   $(".line-item-table-buttons").removeClass("hidden");
});


$('#tax-button').on('click', function() { // add/remove tax from proposal
   $("table[id=total-table]").toggle();
});


$('#id_mount').on('change', function() {
  var selectedItem = $(this).val();
  var option = "Ext"
  var fieldId = ".trim-field"

  showField(selectedItem, option, fieldId);
});


$('#id_shutter_type').on('change', function() { // hide/unhide height-center, height-left and height-right fields
  var selectedItem = $(this).val();

  if (selectedItem > 3 && selectedItem < 6) {
    val = 10
  } else {
    val = 5
  }

  var option = 10
  var fieldId = "#height-left-right-field"

  // showField(val, option, fieldId);
  showField(selectedItem);
});


// FUNCTIONS
function showField(val){ // function to render hidden fields in line item form
  var val = val;

  if (val > 2 && val < 6) {
    $(".height-center-field").removeClass("hidden");
    $(".height-field").addClass("hidden");
  } else {
    $(".height-center-field").addClass("hidden");
    $(".height-field").removeClass("hidden");
  }

  if (val > 3 && val < 6) {
    $("#height-left-right-field").removeClass("hidden");
  } else {
    $("#height-left-right-field").addClass("hidden");
  }
};


// load letterhead
$(function () {
    var url = $("#letterhead").attr("letterhead-url");

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#letterhead").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });
});


// make notes textarea smaller
document.getElementById("id_notes").rows = "5";




}); // Document is ready
