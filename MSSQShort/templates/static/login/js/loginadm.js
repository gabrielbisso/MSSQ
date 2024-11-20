function chamarpagina() {
    alert("TESTE")
    window.open("resultados");
}

document.addEventListener("DOMContentLoaded", function () {
    
    const usuarioCorreto = "Admin";
    const senhaCorreta = "12345";

    const usuarioInput = document.getElementById("usuario");
    const senhaInput = document.getElementById("senha");
    const botaoLogin = document.getElementById("botao");

    function validarCampos() {
        const usuario = usuarioInput.value.trim(); // Remove espaços extras
        const senha = senhaInput.value.trim();

        if (usuario === usuarioCorreto && senha === senhaCorreta) {
            botaoLogin.disabled = false; // Habilita o botão
        } else {
            botaoLogin.disabled = true; // Desabilita o botão
        }
    }

    // Adiciona eventos de "keyup" aos campos de entrada
    usuarioInput.addEventListener("keyup", validarCampos);
    senhaInput.addEventListener("keyup", validarCampos);

    function chamarpagina() {
        window.open("questionario1");
    }
});



