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

$('#divider-button').on('click', function() { // add/remove tax from proposal
   $(".divider-field").toggle();
});


$('#id_mount').on('change', function() {
  var selectedItem = $(this).val();
  var option = "Ext"
  var fieldId = ".trim-field"

  showField(selectedItem, option, fieldId);
});


$('#id_shutter_type').on('change', function() { // hide/unhide height-center, height-left and height-right fields
  var selectedItem = $(this).val();

  showMeasureField(selectedItem);
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

function showMeasureField(val){ // function to render hidden fields in line item form
  var val = val;

  if (val > 2 && val < 6) {
    $(".height-center-field").removeClass("hidden");
  } else {
    $(".height-center-field").addClass("hidden");
  }

  if (val > 3 && val < 6) {
    $(".height-lr-field").removeClass("hidden");
    $(".height-field").addClass("hidden");
  } else {
    $(".height-lr-field").addClass("hidden");
    $(".height-field").removeClass("hidden");
  }

  if (val == 6) {
    $(".height-dk-field").removeClass("hidden");
  } else {
    $(".height-dk-field").addClass("hidden");
  }

};


}); // Document is ready
