function showMessage(elementId, message) {
    document.getElementById(elementId).innerText = message;
    setTimeout(function () {
        document.getElementById(elementId).innerText = "";
    }, 3000); 
}

// function submitContactForm() {
   
// }
    // AJAX request to submit the form
 

    $(document).on('submit','.contact-form',function(e) {
        e.preventDefault();

        var name = document.getElementById('name').value;
        var email = document.getElementById('email').value;
        var phone = document.getElementById('phone').value;
        var message = document.getElementById('message').value;
    
        if (name == "") {
            showMessage('nameMessage', 'Please enter your name');
            return false;
        }
    
    
      
        

        var validRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
      
        if (email == "") {
            showMessage('emailMessage', 'Please enter your email');
            return false;
        }
    
        else if (!email.match(validRegex)) {
            showMessage('emailMessage', 'Please enter your valid email');
            return false;
        }
      
        
        if (phone == "") {
            showMessage('phoneMessage', 'Please enter your phone number');
            return false;
        }
    
        if(phone.length !==10){
            showMessage('phoneMessage','phone number must be 10 digit');
            return false;
        }
        if (message == "") {
            showMessage('messageMessage', 'Please write a message');
            return false;
        }
        var data = {
            name: name,
            email: email,
            phone: phone,
            message: message,
        };
    
    
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/contact',
        data:data,
       
        success: function(response) {
            console.log(response)
            if (response.n == 0) {
                $('#msg1').html(response.msg)
                setTimeout(function() {
                  document.getElementById("msg1").innerText = "";
              }, 3000); 
            } else {
                $('#msg2').html(response.msg)
                setTimeout(function() {
                  document.getElementById("msg2").innerText = "";
              }, 3000); 
            }
        },
    });

    return false; 

});

