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


$('#tax-button').on('click', function() { // add/remove tax from proposal
   $("table[id=total-table]").toggle();
});


$('#id_mount').on('change', function() {
  var selectedItem = $(this).val();
  var option = "Ext"
  var fieldId = ".trim-field"

  showField(selectedItem, option, fieldId);
});


$('#id_shutter_type').on('change', function() { // hide/unhide height-center field
  var selectedItem = $(this).val();

  if (selectedItem > 2 && selectedItem < 6) {
    val = 10
  } else {
    val = 5
  }

  var option = 10
  var fieldId = "#height-center-field"

  showField(val, option, fieldId);
});


$('#id_shutter_type').on('change', function() { // hide/unhide height-left and height-right fields
  var selectedItem = $(this).val();

  if (selectedItem > 3 && selectedItem < 6) {
    val = 10
  } else {
    val = 5
  }

  var option = 10
  var fieldId = "#height-left-right-field"

  showField(val, option, fieldId);
});


// FUNCTIONS
function showField(i, o, f){ // function to render hidden fields in line item form
  var i = i;
  var o = o;
  var f = f;

  if (i == o) {
    $(f).removeClass("hidden");
  } else {
    $(f).addClass("hidden");
  }
};


// make notes textarea smaller
document.getElementById("id_notes").rows = "5";




}); // Document is ready
