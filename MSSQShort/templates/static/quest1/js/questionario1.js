document.addEventListener('DOMContentLoaded', function() {
  const inputs = document.querySelectorAll('input[type="text"]');
  const radios = document.querySelectorAll('input[type="radio"]');
  const submitButton = document.getElementById('botao');

  // Configuração dos steps
  $(document).ready(function () {
    $(".form .button").click(function () {
        const button = $(this);
        const currentSection = button.parents(".section");
    console.log("Seção Atual: ", currentSection);
        const currentSectionIndex = currentSection.index();
        const headerSection = $('.steps li').eq(currentSectionIndex);
        const nextSection = currentSection.next();
        console.log("Próxima Seção: ", nextSection);  

        // Verifica se todos os campos da seção atual estão preenchidos
        if (!validateCurrentSection(currentSection)) {
            alert("Por favor, preencha todos os campos antes de continuar.");
            return;
        }

$(".form .section").first().addClass("is-active");
console.log($(".form .section").first());  // Verifique no console se a primeira seção está sendo selecionada corretamente


        // Inicializa a visibilidade da primeira seção
$(".form .section").first().addClass("is-active");

// Navegação entre seções
currentSection.removeClass("is-active").next().addClass("is-active");
headerSection.removeClass("is-active").next().addClass("is-active");

// Reinicia o formulário no final
if (currentSectionIndex === $('.form .section').length - 1) {
   $(document).find(".form .section").first().addClass("is-active");
   $(document).find(".steps li").first().addClass("is-active");
}
});

// Impede o envio padrão do formulário
$(".form").submit(function (e) {
e.preventDefault();
});
});

// Valida campos da seção atual
function validateCurrentSection(section) {
const inputsInSection = section.find('input[type="text"]');
const radiosInSection = section.find('input[type="radio"]');

const allInputsFilled = Array.from(inputsInSection).every(input => input.value.trim() !== '');
const atLeastOneRadioSelected = Array.from(radiosInSection).some(radio => radio.checked);

return allInputsFilled && atLeastOneRadioSelected;
}

// Valida todos os campos para habilitar/desabilitar o botão
function checkForm() {
const allInputsFilled = Array.from(inputs).every(input => input.value.trim() !== '');
const allRadiosSelected = Array.from(radios).some(radio => radio.checked);

submitButton.disabled = !(allInputsFilled && allRadiosSelected);
}

// Adiciona eventos de input e change para validação em tempo real
inputs.forEach(input => input.addEventListener('input', checkForm));
radios.forEach(radio => radio.addEventListener('change', checkForm));

// Chama a função inicialmente para garantir que o botão esteja no estado correto
checkForm();
});