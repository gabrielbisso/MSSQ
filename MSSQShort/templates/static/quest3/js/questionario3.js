document.addEventListener('DOMContentLoaded', function() {
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  const textarea = document.getElementById('outros');
  const submitButton = document.getElementById('botao');

  function checkForm() {
      // Check if at least one checkbox is checked
      const isAnyCheckboxChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);
      // Check if the textarea is filled
      const isTextareaFilled = textarea.value.trim() !== '';

      // Enable or disable the button depending on the state of checkboxes and textarea
      if (isAnyCheckboxChecked || isTextareaFilled) {
          submitButton.disabled = false;
      } else {
          submitButton.disabled = true;
      }
  }

  // Attach event listeners to checkboxes and textarea
  checkboxes.forEach(checkbox => checkbox.addEventListener('change', checkForm));
  textarea.addEventListener('input', checkForm);

  // Initial check to set the button state correctly on page load
  checkForm();
});
