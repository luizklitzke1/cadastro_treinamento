//Script para declaração e controle da validação dos forumários de salas e espaços de facé em tempo real
// Separado do padrão de HTML para melhor customização e controle

//Variável que garante que todos os campos sejam válidos 
var formValid = {
    nome : false,
};


//Torna todos os valores válidos caso estiver apenas editando
if ($("#form_editar").length){
    formValid = { 
        nome : true,
    };
    checkForm();
}

//Verifica se todos os campos estão válidos
function checkForm(){

    var check = true;
    
    if (!formValid.nome){
        check = false;
    };

    //Fora do loop para evitar problemas com sync 
    if (check){
        $('#btnAd').removeAttr('disabled');
        return true;
    }
    else{
        $('#btnAd').attr('disabled', true);
        return false;
    }
    
    };

//Muda a mensagem de erro nos inputs
function msg(id,message){
    $(id).text(message).show;
}

//Mostra a div com a msg
function show(id){
    $(id).show();
}

//Padrão de verificação dos caracteres de texto
//var textEsp = new RegExp(/^[a-zA-Z0-9]+$/);

//Verificação customizada do nome
var testeLetters = new RegExp(/^[\s\p{L}]*$/ui);

$("#campoNome").on('input', function() {
    var input= $(this);

    if (input.val().length <3){
        msg("#inv-nome","O nome deve ter no mínimo 3 caracteres!");
        formValid["nome"] = false;
    }
    else {
        if (testeLetters.test(input.val())){
            formValid["nome"] = true;
        }
        else{
            msg("#inv-nome","O nome deve conter apenas letras!");
            formValid["nome"] = false;
        };
    }   

    if (formValid["nome"]){
        $("#inv-nome").hide();
        input.removeClass("invalid").addClass("valid");
    }
    else{
        show("#inv-nome");
        input.removeClass("valid").addClass("invalid");
        
    };
    checkForm();
    
});




