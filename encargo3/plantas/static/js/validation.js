$(document).ready(function() {
    $('.form').submit(function(e) {
      e.preventDefault();
      var name = $('#name').val();
      var email = $('#email').val();
      var phone = $('#phone').val();
      var subject = $('#subject').val();
      var message = $('#message').val();
  
      // Validar los campos requeridos
      if (name == '' || email == '' || phone == '' || subject == '' || message == '') {
        alert('Por favor, complete todos los campos requeridos');
        return false;
      }
  
      // Validar el formato de correo electrónico
      var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (!emailRegex.test(email)) {
        alert('Por favor, ingrese una dirección de correo electrónico válida');
        return false;
      }
  
      // Validar el formato de teléfono
      var phoneRegex = /^\d{10}$/;
      if (!phoneRegex.test(phone)) {
        alert('Por favor, ingrese un número de teléfono válido (10 dígitos)');
        return false;
      }
  
      // Si todo es válido, enviar el formulario
      alert('Formulario enviado exitosamente!');
      return true;
    });
  });
  