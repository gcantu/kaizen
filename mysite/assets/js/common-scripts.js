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

$('#divider-button').on('click', function() { // add/remove divider field in line item form
   $(".divider-field").toggle();
});

$('#measurement-guide-button').on('click', function() { // show measurement guide in line item form
   $(".shutter-model-img-section").toggle();
   $(".shutter-model-img-guide-section").toggle();
});


$('#id_mount').on('change', function() {
  var selectedItem = $(this).val();
  var option = "Ext"
  var fieldId = ".trim-field"

  showField(selectedItem, option, fieldId);
});


$('#id_shutter_type').on('change', function() { // render shutter model image
  var model = "/static/img/model" + $(this).val() + ".png";
  var guide = "/static/img/model" + $(this).val() + "_m.png";

  $('.shutter-model-img').prop('src', model);
  $('.shutter-model-img-guide').prop('src', guide);

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

  if (val > 5) {
    $(".height-center-field").removeClass("hidden");
  } else {
    $(".height-center-field").addClass("hidden");
  }

  if (val == 7 || val == 8 || val == 12) {
    $(".height-field").addClass("hidden");
  } else {
    $(".height-field").removeClass("hidden");
  }

  if (val > 11) {
    $(".height-lr-field").removeClass("hidden");
  } else {
    $(".height-lr-field").addClass("hidden");
  }

  if (val == 15) {
    $(".height-m-field").removeClass("hidden");
  } else {
    $(".height-m-field").addClass("hidden");
  }

  if (val == 4) {
    $(".panel-field").addClass("hidden");
    $(".mount-field").addClass("hidden");
    $(".louver-field").addClass("hidden");
    $(".door-field").removeClass("hidden");
  } else {
    $(".panel-field").removeClass("hidden");
    $(".mount-field").removeClass("hidden");
    $(".louver-field").removeClass("hidden");
    $(".door-field").addClass("hidden");
  }

  if (val == 4 || val == 6 || val == 8 || val == 13 || val == 15) {
    $(".tpost-field").addClass("hidden");
  } else {
    $(".tpost-field").removeClass("hidden");
  }

};


}); // Document is ready
