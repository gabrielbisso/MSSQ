document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input[type="text"]');
    const submitButton = document.getElementById('botao');
  
    function checkForm() {
      const allInputsFilled = Array.from(inputs).every(input => input.value.trim() !== '');
      
      // Habilitar ou desabilitar o botão dependendo do estado dos inputs e radios
      if (allInputsFilled) {
        submitButton.disabled = false;
      } else {
        submitButton.disabled = true;
      }
    }
// Adiciona os eventos de input e change para verificar quando os valores mudam
inputs.forEach(input => input.addEventListener('input', checkForm));
  
// Chama a função inicialmente para garantir que o botão esteja no estado correto
checkForm();
});