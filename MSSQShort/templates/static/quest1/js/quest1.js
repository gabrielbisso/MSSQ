document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('input[type="text"]');
    const radios = document.querySelectorAll('input[type="radio"]');
    const submitButton = document.getElementById('botao');
    const idadeInput = document.getElementById('idadeInput');
    const sexoRadios = document.querySelectorAll('input[type="radio"][name="sexo"]');
    const submitButtoninicio = document.getElementById('botaoprox');

    // Configuração dos steps
    $(document).ready(function () {
        $(".form .button").click(function () {
            const currentSection = document.querySelector(".section.is-active"); // Encontre a seção com a classe 'is-active'
            if (!currentSection) {
                console.error("A seção ativa não foi encontrada.");
                return; // Se a seção ativa não for encontrada, não faz nada
            }

            const currentSectionIndex = Array.from(document.querySelectorAll('.form .section')).indexOf(currentSection); // Índice da seção ativa
            const nextSection = currentSection.nextElementSibling;

            // Verifica se todos os campos da seção atual estão preenchidos
            if (!validateCurrentSection(currentSection)) {
                alert("Por favor, preencha todos os campos antes de continuar.");
                return;
            }

            // Navegação entre seções
            currentSection.classList.remove("is-active");
            if (nextSection) {
                nextSection.classList.add("is-active");
            }

            const headerSection = $('.steps li').eq(currentSectionIndex);
            headerSection.removeClass("is-active").next().addClass("is-active");

            // Reinicia o formulário no final
            if (!nextSection) {
                $(".form .section").first().addClass("is-active");
                $(".steps li").first().addClass("is-active");
            }
        });

        // Impede o envio padrão do formulário
        $(".form").submit(function (e) {
            e.preventDefault();
        });
    });

    // Valida campos da seção atual
    function validateCurrentSection(section) {
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

    function checkFormButtonInicio() {
        // Verifica se o campo idade foi preenchido corretamente
        const isIdadeFilled = idadeInput.value.trim() !== '';

        // Verifica se pelo menos um rádio de sexo foi selecionado
        const isSexoSelected = Array.from(sexoRadios).some(radio => radio.checked);

        // Habilita o botão somente quando ambos os campos estiverem válidos
        submitButtoninicio.disabled = !(isIdadeFilled && isSexoSelected);
    }

    function chamarpagina()
    {
        window.open("questionario1");
    }


    // Adiciona eventos de input e change para validação em tempo real
    inputs.forEach(input => input.addEventListener('input', checkForm)); // Para campos de texto
    radios.forEach(radio => radio.addEventListener('change', checkForm)); // Para botões de rádio

    idadeInput.addEventListener('input', checkFormButtonInicio); // Para campo de idade
    sexoRadios.forEach(radio => radio.addEventListener('change', checkFormButtonInicio)); // Para botões de rádio

    // Chama a função inicialmente para garantir que o botão esteja no estado correto
    checkForm();
    checkFormButtonInicio();
});