document.addEventListener('DOMContentLoaded', function() {
  const inputs = document.querySelectorAll('input[type="text"]');
  const radios = document.querySelectorAll('input[type="radio"]');
  const submitButton = document.getElementById('botao');

  function checkForm() {
    const allInputsFilled = Array.from(inputs).every(input => input.value.trim() !== '');
    const allRadiosSelected = Array.from(radios).some(radio => radio.checked);
    
    // Habilitar ou desabilitar o botão dependendo do estado dos inputs e radios
    if (allInputsFilled && allRadiosSelected) {
      submitButton.disabled = false;
    } else {
      submitButton.disabled = true;
    }
  }

  // Adiciona os eventos de input e change para verificar quando os valores mudam
  inputs.forEach(input => input.addEventListener('input', checkForm));
  radios.forEach(radio => radio.addEventListener('change', checkForm));

  // Chama a função inicialmente para garantir que o botão esteja no estado correto
  checkForm();
});