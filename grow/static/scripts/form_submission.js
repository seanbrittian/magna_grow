/*
$(document).ready(function() {
  $('form').submit(function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var formData = $(this).serialize(); // Serialize the form data

    $.ajax({
      url: 'form-submit/', // Replace 'form' with the appropriate URL endpoint
      type: 'POST',
      data: formData,
      success: function(response) {
            console.log(formData)
            location.reload();
        // Handle the success response here
      },
      error: function(xhr, status, error) {
        // Handle the error response here
      }
    });
  });
});*/
$(document).ready(function() {
  $('form').submit(function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var formData = $(this).serialize(); // Serialize the form data

    $.ajax({
      url: 'form-submit/', // Replace 'form-submit/' with the appropriate URL endpoint
      type: 'POST',
      data: formData,
      success: function(response) {
        // Handle the success response here
        console.log(formData);

        // Show the custom modal
        $('#customModal').show();

        // Count down from 5 and close the modal after 5 seconds
        var count = 5;
        var countdownInterval = setInterval(function() {
          if (count === 0) {
            clearInterval(countdownInterval);
            $('#customModal').hide(); // Close the custom modal
                   location.reload();
          } else {
            $('#countdown').text('Closing in ' + count + ' seconds');
            count--;

          }
        }, 1000);
        },
      error: function(xhr, status, error) {
        // Handle the error response here
      }
    });
  });

  // Close the custom modal when the close button is clicked
  $('.close').click(function() {
    $('#customModal').hide();
  });
});