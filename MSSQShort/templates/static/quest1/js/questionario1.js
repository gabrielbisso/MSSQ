document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('input[type="text"]');
    const radios = document.querySelectorAll('input[type="radio"]');
    const submitButton = document.getElementById('botao');

    // Configuração dos steps
    $(document).ready(function () {
        $(".form .button").click(function () {
            const button = $(this);
            const currentSection = button.closest(".section"); // Ajustado para usar closest corretamente com jQuery
            const currentSectionIndex = currentSection.index();
            const headerSection = $('.steps li').eq(currentSectionIndex);

            // Verifica se todos os campos da seção atual estão preenchidos
            if (!validateCurrentSection(currentSection)) {
                alert("Por favor, preencha todos os campos antes de continuar.");
                return;
            }

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
        // Verifica se o argumento é um elemento DOM ou jQuery e ajusta
        if (section instanceof jQuery) {
            section = section[0]; // Converte para elemento DOM se for jQuery
        }

        const inputsInSection = section.querySelectorAll('input[type="text"]');
        const radiosInSection = section.querySelectorAll('input[type="radio"]');

        const allInputsFilled = Array.from(inputsInSection).every(input => input.value.trim() !== '');
        const atLeastOneRadioSelected = Array.from(radiosInSection).some(radio => radio.checked);

        return allInputsFilled && atLeastOneRadioSelected;
    }

    // Valida todos os campos para habilitar/desabilitar o botão
    function checkForm() {
        const allInputsFilled = Array.from(inputs).every(input => input.value.trim() !== '');
        const atLeastOneRadioSelected = Array.from(radios).some(radio => radio.checked);

        submitButton.disabled = !(allInputsFilled && atLeastOneRadioSelected);
    }

    // Adiciona eventos de input e change para validação em tempo real
    inputs.forEach(input => input.addEventListener('input', checkForm));
    radios.forEach(radio => radio.addEventListener('change', checkForm));

    // Chama a função inicialmente para garantir que o botão esteja no estado correto
    checkForm();
});
