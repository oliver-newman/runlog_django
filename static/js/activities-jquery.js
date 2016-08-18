$(document).ready(function() {
  if (!$('#id_runToday').is(":checked")) {
    $('.runField').toggle();
  }
  if (!$('#id_bikeToday').is(":checked")) {
    $('.bikeField').toggle();
  }
    
  $('#id_runToday').change(function() {
    $('.runField').toggle();
  });
  $('#id_bikeToday').click(function() {
    $('.bikeField').toggle();
  });
});
